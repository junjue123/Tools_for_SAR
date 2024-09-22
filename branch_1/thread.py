import os
import sys
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, imgpath, savepath, operation, method):
        super().__init__()
        self.imgpath = imgpath
        self.savepath = savepath
        self.operation = operation
        self.method = method
        self.base_path = self.get_base_path()

    def get_base_path(self):
        # 获取程序根目录
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller 打包后的路径
            return os.path.dirname(sys.argv[0])
        else:
            # 开发环境中的路径
            return os.path.dirname(os.path.abspath(__file__))

    def run(self):
        try:
            if os.path.isdir(self.imgpath):
                # 输入路径为文件夹，遍历文件夹中的图像文件
                for filename in os.listdir(self.imgpath):
                    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                        img_path = os.path.join(self.imgpath, filename)
                        self.process_image(img_path)
            elif os.path.isfile(self.imgpath):
                # 输入路径为具体图片的路径，直接对该图片进行操作
                self.process_image(self.imgpath)
            else:
                raise ValueError("Input path is neither a file nor a directory")
        except Exception as e:
            print(f"Error occurred: {e}")
            self.finished.emit(f"Error: {str(e)}")  # Emit error message

    def process_image(self, img_path):
        try:
            # 获取输入图片的名称
            img_name = os.path.splitext(os.path.basename(img_path))[0]

            # 构建输出路径
            output_folder = os.path.join(self.savepath, img_name)
            os.makedirs(output_folder, exist_ok=True)

            # 使用字典映射来简化代码,将路径替换为自己的路径，此处为相对路径
            operations = {
                "SAR_Ship_Detection": {
                    "大场景图片": ("",
                                   ["python", "demo/huge_image_demo_1.py", "--output_path", output_folder])
                },
                "optical_Ship_Detection": {
                    "大场景图片": ("",
                                   ["python", "demo/huge_image_demo_2.py", "--output_path", output_folder])
                }
            }
            if self.operation in operations and self.method in operations[self.operation]:
                print(f"Selected operation: {self.operation}, method: {self.method}")
                details = operations[self.operation][self.method]
                # 直接使用 base_path 作为 parent_dir
                parent_dir = os.path.dirname(self.base_path)

                # 打印执行的指令和所在的路径
                print(f"Command to execute: {' '.join(details[1] + [img_path])}")
                print(f"Working directory: {parent_dir}")
                # 执行命令
                result = subprocess.run(details[1] + [img_path], cwd=parent_dir, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
                if len(details) == 4:
                    subprocess.run(details[3], cwd=os.path.join(parent_dir, details[2]), check=True, creationflags=subprocess.CREATE_NO_WINDOW)
                self.finished.emit(self.savepath)  # Emit signal after work is done
            else:
                raise ValueError("Operation or method not supported")
        except Exception as e:
            print(f"Error occurred: {e}")
            self.finished.emit(f"Error: {str(e)}")  # Emit error message
