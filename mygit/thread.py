import os
from PyQt5.QtCore import QThread, pyqtSignal

class Worker(QThread):
    # 定义信号，用于发送结果
    finished = pyqtSignal(str)

    def __init__(self, imgpath, savepath, operation):
        super().__init__()
        self.imgpath = imgpath
        self.savepath = savepath
        self.operation = operation

    def run(self):
        if self.operation == "Airport_Detection":
            # 执行耗时的操作
            os.chdir("Airport_Detection/code")
            os.chdir("code1")
            os.system("python main.py " + self.imgpath)
            os.chdir("..")
            os.chdir("code2")
            os.system("python dbs.py " + " --output_path " + self.savepath)
            os.chdir("..")
            os.chdir("..")
            os.chdir("..")

        if self.operation == "Sea_or_Land":
            os.chdir("Sea_Land_Division")
            os.system("python seg_QL1.py " + self.imgpath + " --output_path " + self.savepath)
            os.chdir("..")

        if self.operation == "Ship_Detection":
            os.chdir("Ship_Detection/demo")
            os.system("python image_demo.py " + self.imgpath + " oriented_rcnn_r50_fpn_6x_ssdd_le90.py latest.pth "
                      + "--output_path " + self.savepath)
            os.chdir("..")
            os.chdir("..")

        if self.operation == "Ship_Identification":
            os.chdir("Ship_Identification")
            os.system("python test.py " + self.imgpath + " --output_path " + self.savepath)
            os.chdir("..")

        if self.operation == "Aircraft_Detection":
            os.chdir("Aircraft_Detection/faster_rcnn")
            os.system("python predict.py " + self.imgpath + " --output_path " + self.savepath)
            os.chdir("..")
            os.chdir("..")

        if self.operation == "Aircraft_Identification":
            os.chdir("Aircraft_Identification")
            os.system("python test.py " + self.imgpath + " --output_path " + self.savepath)
            os.chdir("..")

        # 完成后发送信号
        self.finished.emit(self.savepath)

