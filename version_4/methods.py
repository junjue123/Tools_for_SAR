from PyQt5.QtWidgets import QMessageBox

#警告框
def message_button(imgpath,savepath):
	if imgpath == "":
		message_imgchoose()
		return False
	else:
		if savepath == "":
			message_savedirchoose()
		return True

def message_imgchoose():
	msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '没选择图片！')
	msg_box.exec_()

def message_savedirchoose():
	msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '没选择保存路径！')
	msg_box.exec_()

def message_functionchoose():
	msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '没选择功能！')
	msg_box.exec_()


