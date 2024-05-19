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
            # 使用字典映射来简化代码
            operations = {
                "Airport_Detection": {
                    "default": ("Airport_Detection/code/code1", ["python", "main.py", self.imgpath], "code2",
                                ["python", "dbs.py", "--output_path", self.savepath])
                },
                "Sea_or_Land": {
                    "default": (
                    "Sea_Land_Division", ["python", "seg_QL1.py", self.imgpath, "--output_path", self.savepath])
                },
                "Ship_Detection": {
                    "水平框检测": ("Ship_Detection/horizontal",
                                   ["python", "predict.py", self.imgpath, "--output_path", self.savepath]),
                    "旋转框检测": ("Ship_Detection/rotated/demo",
                                   ["python", "image_demo.py", self.imgpath, "oriented_rcnn_r50_fpn_6x_ssdd_le90.py", "latest.pth", "--output_path",
                                    self.savepath])
                },
                "Ship_Identification": {
                    "default": (
                    "Ship_Identification", ["python", "test.py", self.imgpath, "--output_path", self.savepath])
                },
                "Aircraft_Detection": {
                    "default": ("Aircraft_Detection/faster_rcnn",
                                ["python", "predict.py", self.imgpath, "--output_path", self.savepath])
                },
                "Aircraft_Identification": {
                    "default": (
                    "Aircraft_Identification", ["python", "test.py", self.imgpath, "--output_path", self.savepath])
                }
            }
            if self.operation in operations and self.method in operations[self.operation]:
                details = operations[self.operation][self.method]
                # 执行命令
                subprocess.run(details[1], cwd=details[0], check=True)
                if len(details) == 4:
                    subprocess.run(details[3], cwd=os.path.join(details[0], details[2]), check=True)
                self.finished.emit(self.savepath)  # Emit signal after work is done
            else:
                raise ValueError("Operation or method not supported")
        except Exception as e:
            print(f"Error occurred: {e}")
            self.finished.emit(f"Error: {str(e)}")  # Emit error message
