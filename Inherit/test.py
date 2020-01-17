# coding=utf-8

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 550)
        self.setWindowTitle('关注微信公众号：学点编程吧--标准输入对话框')

        self.lb1 = QLabel('姓名：', self)
        self.lb1.move(20, 20)

        self.lb2 = QLabel('年龄：', self)
        self.lb2.move(20, 80)

        self.lb3 = QLabel('性别：', self)
        self.lb3.move(20, 140)

        self.lb4 = QLabel('身高（cm）：', self)
        self.lb4.move(20, 200)

        self.lb5 = QLabel('基本信息：', self)
        self.lb5.move(20, 260)

        self.lb6 = QLabel('学点编程', self)
        self.lb6.move(80, 20)

        self.lb7 = QLabel('18', self)
        self.lb7.move(80, 80)

        self.lb8 = QLabel('男', self)
        self.lb8.move(80, 140)

        self.lb9 = QLabel('175', self)
        self.lb9.move(120, 200)

        self.tb = QTextBrowser(self)
        self.tb.move(20, 320)

        self.bt1 = QPushButton('修改姓名', self)
        self.bt1.move(200, 20)

        self.bt2 = QPushButton('修改年龄', self)
        self.bt2.move(200, 80)

        self.bt3 = QPushButton('修改性别', self)
        self.bt3.move(200, 140)

        self.bt4 = QPushButton('修改身高', self)
        self.bt4.move(200, 200)

        self.bt5 = QPushButton('修改信息', self)
        self.bt5.move(200, 260)

        self.show()

        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)
        self.bt4.clicked.connect(self.showDialog)
        self.bt5.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        sex = ['男', '女']
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '修改姓名', '请输入姓名：')
            if ok:
                self.lb6.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getInt(self, '修改年龄', '请输入年龄：', min=1)
            if ok:
                self.lb7.setText(str(text))
        elif sender == self.bt3:
            text, ok = QInputDialog.getItem(self, '修改性别', '请选择性别：', sex)
            if ok:
                self.lb8.setText(text)
        elif sender == self.bt4:
            text, ok = QInputDialog.getDouble(self, '修改身高', '请输入身高：', min=1.0)
            if ok:
                self.lb9.setText(str(text))
        elif sender == self.bt5:
            text, ok = QInputDialog.getMultiLineText(self, '修改信息', '请输入个人信息：')
            if ok:
                self.tb.setText(text)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = Example()
    # sys.exit(app.exec_())
    import os

    print(os.getenv("SystemDrive"))