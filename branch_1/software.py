import sys
import mainwindow

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # 实例化，传参
    app = QApplication(sys.argv)

    # 创建对象
    mainWindow = QMainWindow()

    # 创建ui，引用untitled文件中的Ui_MainWindow类
    ui = mainwindow.Ui_MainWindow()

    # 调用Ui_MainWindow类的setupUi，创建初始组件
    ui.setupUi(mainWindow)

    # 创建窗口
    mainWindow.show()

    # 进入程序的主循环
    sys.exit(app.exec_())