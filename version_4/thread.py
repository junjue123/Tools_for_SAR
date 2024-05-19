import os
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

            # 使用字典映射来简化代码
            operations = {
                "Airport_Detection": {
                    "机场检测方法1": ("Airport_Detection/code/code1", ["python", "main.py"], "code2",
                                ["python", "dbs.py"])
                },
                "Sea_or_Land": {
                    "海陆分割算法1": (
                    "Sea_Land_Division", ["python", "seg_QL1.py", "--output_path", output_folder])
                },
                "Ship_Detection": {
                    "水平框检测": ("Ship_Detection/horizontal",
                                   ["python", "predict.py", "--output_path", output_folder]),
                    "旋转框检测": ("Ship_Detection/rotated/demo",
                                   ["python", "image_demo.py", "--output_path", output_folder])
                },
                "Ship_Identification": {
                    "舰船识别算法1": (
                    "Ship_Identification", ["python", "test.py", "--output_path", output_folder])
                },
                "Aircraft_Detection": {
                    "飞机检测算法1": ("Aircraft_Detection/faster_rcnn",
                                ["python", "predict.py", "--output_path", output_folder])
                },
                "Aircraft_Identification": {
                    "飞机识别算法1": (
                    "Aircraft_Identification", ["python", "test.py", "--output_path", output_folder])
                }
            }
            if self.operation in operations and self.method in operations[self.operation]:
                details = operations[self.operation][self.method]
                # 执行命令
                subprocess.run(details[1] + [img_path], cwd=details[0], check=True)
                if len(details) == 4:
                    subprocess.run(details[3], cwd=os.path.join(details[0], details[2]), check=True)
                self.finished.emit(self.savepath)  # Emit signal after work is done
            else:
                raise ValueError("Operation or method not supported")
        except Exception as e:
            print(f"Error occurred: {e}")
            self.finished.emit(f"Error: {str(e)}")  # Emit error message