# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QWidget, QApplication

from thread import Worker
import demo_rc
import methods
import os


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 541)
        MainWindow.showMaximized()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(30, 30))
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/校徽.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Ship_or_Aircraft = QtWidgets.QComboBox(self.centralwidget)
        self.Ship_or_Aircraft.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ship_or_Aircraft.sizePolicy().hasHeightForWidth())
        self.Ship_or_Aircraft.setSizePolicy(sizePolicy)
        self.Ship_or_Aircraft.setMinimumSize(QtCore.QSize(300, 50))
        self.Ship_or_Aircraft.setMaximumSize(QtCore.QSize(601, 200))
        self.Ship_or_Aircraft.setMouseTracking(False)
        self.Ship_or_Aircraft.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Ship_or_Aircraft.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Ship_or_Aircraft.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.Ship_or_Aircraft.setObjectName("Ship_or_Aircraft")
        self.verticalLayout_2.addWidget(self.Ship_or_Aircraft, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Functions = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Functions.sizePolicy().hasHeightForWidth())
        self.Functions.setSizePolicy(sizePolicy)
        self.Functions.setMinimumSize(QtCore.QSize(300, 50))
        self.Functions.setMaximumSize(QtCore.QSize(600, 200))
        self.Functions.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Functions.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.Functions.setObjectName("Functions")
        self.verticalLayout_2.addWidget(self.Functions, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Image_Choose = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_Choose.sizePolicy().hasHeightForWidth())
        self.Image_Choose.setSizePolicy(sizePolicy)
        self.Image_Choose.setMinimumSize(QtCore.QSize(300, 50))
        self.Image_Choose.setMaximumSize(QtCore.QSize(600, 200))
        self.Image_Choose.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Image_Choose.setObjectName("Image_Choose")
        self.verticalLayout_2.addWidget(self.Image_Choose, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start.sizePolicy().hasHeightForWidth())
        self.Start.setSizePolicy(sizePolicy)
        self.Start.setMinimumSize(QtCore.QSize(300, 50))
        self.Start.setMaximumSize(QtCore.QSize(600, 200))
        self.Start.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Start.setObjectName("Start")
        self.verticalLayout_2.addWidget(self.Start, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setObjectName("label_output")
        self.verticalLayout_2.addWidget(self.label_output)
        self.out_info = QtWidgets.QLabel(self.centralwidget)
        self.out_info.setMinimumSize(QtCore.QSize(100, 100))
        self.out_info.setMaximumSize(QtCore.QSize(900, 600))
        self.out_info.setFrameShape(QtWidgets.QFrame.Box)
        self.out_info.setText("")
        self.out_info.setObjectName("out_info")
        self.verticalLayout_2.addWidget(self.out_info)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 1)
        self.verticalLayout_2.setStretch(8, 6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.inputimg = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputimg.sizePolicy().hasHeightForWidth())
        self.inputimg.setSizePolicy(sizePolicy)
        self.inputimg.setMaximumSize(QtCore.QSize(900, 600))
        self.inputimg.setFrameShape(QtWidgets.QFrame.Box)
        self.inputimg.setObjectName("inputimg")
        self.verticalLayout_3.addWidget(self.inputimg)
        self.outputimg = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputimg.sizePolicy().hasHeightForWidth())
        self.outputimg.setSizePolicy(sizePolicy)
        self.outputimg.setMaximumSize(QtCore.QSize(900, 600))
        self.outputimg.setFrameShape(QtWidgets.QFrame.Box)
        self.outputimg.setObjectName("outputimg")
        self.verticalLayout_3.addWidget(self.outputimg)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.Image_Choose.clicked.connect(self.ImageChoose)
        self.Start.clicked.connect(self.QtStart)
        MainWindow.resizeEvent = self.ResizeEvent
        self.Ship_or_Aircraft.mousePressEvent = self.onComboClicked
        self.Ship_or_Aircraft_already_filled = False
        self.Ship_or_Aircraft.currentTextChanged.connect(self.update_functions)

        self.imgpath = ""
        self.savepath = ""
        self.outputpath = ""

    def onComboClicked(self, event):
        QtWidgets.QComboBox.showPopup(self.Ship_or_Aircraft)
        if not self.Ship_or_Aircraft_already_filled:
            font = QFont()
            font.setFamily("Arial")
            font.setBold(True)
            font.setPointSize(9)
            self.Ship_or_Aircraft.setFont(font)
            self.Ship_or_Aircraft.addItems(['舰船', '飞机'])
            self.Ship_or_Aircraft_already_filled = True

    def update_functions(self, text):
        font = QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(9)
        self.Functions.setFont(font)
        # 根据第一个下拉列表的选择更新第二个下拉列表的内容
        if text == '舰船':
            self.Functions.clear()
            self.Functions.addItems(['海陆分割', '舰船检测', '舰船识别'])
        elif text == '飞机':
            self.Functions.clear()
            self.Functions.addItems(['机场检测', '飞机检测', '飞机识别'])

    def ImageChoose(self):
        if self.imgpath != "":
            self.imgpath = ""
            self.savepath = ""
            self.outputpath = ""
            self.inputimg.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">输入图片</span></p></body></html>")
            self.outputimg.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">输出图片</span></p></body></html>")
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "","All Files(*)",None,QFileDialog.DontUseNativeDialog)
        if file_path == "":
            pass
        else:
            print(file_path)
            self.imgpath = file_path
            self.showinputimg()
        print("Image_Choose")

    def QtStart(self):
        function = self.Functions.currentText()
        if function == "海陆分割":
            self.Sea_or_Land()
        elif function == "舰船检测":
            self.Ship_Detection()
        elif function == "舰船识别":
            self.Ship_Identification()
        elif function == "机场检测":
            self.Airport_Detection()
        elif function == "飞机检测":
            self.Aircraft_Detection()
        elif function == "飞机识别":
            self.Aircraft_Identification()
        else:
            methods.message_functionchoose()

    def Save_path(self):
        self.outputpath = ""
        save_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/", QFileDialog.ShowDirsOnly)
        if save_path == ".":
            pass
        else:
            print(save_path)
            self.savepath = save_path
        print("Save_path")


    def Airport_Detection(self):
        imgpath = self.imgpath
        if self.savepath == "":
            savepath = "../../../output/Airport_Detection/output.jpg"
            self.outputpath = "output/Airport_Detection/output.jpg"
        else:
            savepath = self.savepath + "/Airport_Detection/output.jpg"
            self.outputpath = savepath
        if methods.message_button(imgpath, savepath):
            self.thread = Worker(imgpath, savepath, "Airport_Detection")
            self.thread.finished.connect(self.onAirportDetectionFinished)
            self.thread.start()
        print("Airport_Detection")

    def Sea_or_Land(self):
        imgpath = self.imgpath
        if self.savepath == "":
            savepath = "../output/Sea_or_Land/output.jpg"
            self.outputpath = "output/Sea_or_Land/output.jpg"
        else:
            savepath = self.savepath + "/Sea_or_Land/output.jpg"
            self.outputpath = savepath
        if methods.message_button(imgpath, savepath):
            self.thread = Worker(imgpath, savepath, "Sea_or_Land")
            self.thread.finished.connect(self.onAirportDetectionFinished)
            self.thread.start()
        print("Sea_or_Land")

    def Ship_Detection(self):
        imgpath = self.imgpath
        if self.savepath == "":
            savepath = "../../output/Ship_Detection/output.jpg"
            self.outputpath = "output/Ship_Detection/output.jpg"
        else:
            savepath = self.savepath + "/Ship_Detection/output.jpg"
            self.outputpath = savepath
        if methods.message_button(imgpath, savepath):
            self.thread = Worker(imgpath, savepath, "Ship_Detection")
            self.thread.finished.connect(self.onAirportDetectionFinished)
            self.thread.start()
        print("Ship_Detection")

    def Ship_Identification(self):
        imgpath = self.imgpath
        if self.savepath == "":
            savepath = "../output/Ship_Identification/output.jpg"
            self.outputpath = "output/Ship_Identification/output.jpg"
        else:
            savepath = self.savepath + "/Ship_Identification/output.jpg"
            self.outputpath = savepath
        if methods.message_button(imgpath, savepath):
            self.thread = Worker(imgpath, savepath, "Ship_Identification")
            self.thread.finished.connect(self.onAirportDetectionFinished)
            self.thread.start()
        print("Ship_Identification")

    def Aircraft_Detection(self):
        imgpath = self.imgpath
        if self.savepath == "":
            savepath = "../../output/Aircraft_Detection/output.jpg"
            self.outputpath = "output/Aircraft_Detection/output.jpg"
        else:
            savepath = self.savepath + "/Aircraft_Detection/output.jpg"
            self.outputpath = savepath
        if methods.message_button(imgpath, savepath):
            self.thread = Worker(imgpath, savepath, "Aircraft_Detection")
            self.thread.finished.connect(self.onAirportDetectionFinished)
            self.thread.start()
        print("Aircraft_Detection")

    def Aircraft_Identification(self):
        imgpath = self.imgpath
        if self.savepath == "":
            savepath = "../output/Aircraft_Identification/output.jpg"
            self.outputpath = "output/Aircraft_Identification/output.jpg"
        else:
            savepath = self.savepath + "/Aircraft_Identification/output.jpg"
            self.outputpath = savepath
        if methods.message_button(imgpath, savepath):
            self.thread = Worker(imgpath, savepath, "Aircraft_Identification")
            self.thread.finished.connect(self.onAirportDetectionFinished)
            self.thread.start()
        print("Aircraft_Identification")

    def onAirportDetectionFinished(self):
        # 线程完成后执行的操作
        self.showoutputimg()
        self.read_output_txt()

    def ResizeEvent(self, event):
        if self.imgpath:
            self.showinputimg()
            self.showoutputimg()
        super(Ui_MainWindow, self).resizeEvent(event)

    def showinputimg(self):
        if self.imgpath:
            input_img = QtGui.QPixmap(self.imgpath).scaled(self.inputimg.width(), self.inputimg.height())
            self.inputimg.setPixmap(input_img)
            self.inputimg.setScaledContents(True)

    def showoutputimg(self):
        if self.outputpath:
            output_img = QtGui.QPixmap(self.outputpath).scaled(self.outputimg.width(), self.outputimg.height())
            self.outputimg.setPixmap(output_img)
            self.outputimg.setScaledContents(True)

    def read_output_txt(self):
        self.out_info.clear()
        txt_path = os.path.splitext(self.outputpath)[0] + '.txt'
        if os.path.exists(txt_path):
            with open(txt_path, 'r') as f:
                content = f.read()
                self.out_info.setText(content)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tools_for_SAR"))
        self.title.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:27pt; font-weight:600;\">SAR图像检测识别工具</span></p></body></html>"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">选择</span><span style=\" font-size:10pt; font-weight:600;\">目标</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">选择具体功能</span></p></body></html>"))
        self.Image_Choose.setText(_translate("MainWindow", "选择图片"))
        self.Start.setText(_translate("MainWindow", "开始"))
        self.label_output.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">输出信息</span></p></body></html>"))
        self.inputimg.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">输入图片</span></p></body></html>"))
        self.outputimg.setText(_translate("MainWindow",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">输出图片</span></p></body></html>"))
        self.inputimg.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.outputimg.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.out_info.setStyleSheet("background-color: rgb(255, 255, 255);")

