#!/usr/bin/python3
# -*-coding:utf-8-*-
"""
Py40 PyQt5 tutorial

This project provides a graph generator.

author: ZF
last edited: 2020-01-16
"""
import subprocess
import sys
import time
from random import randint, choice

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QFileDialog, QLineEdit, \
    QMessageBox


# 随机ASCII码生成数字或大小写字母
def rnd_char():
    return chr(choice([randint(48, 57), randint(65, 90), randint(97, 122)]))


# 背景颜色
def rnd_color():
    return randint(64, 255), randint(64, 255), randint(64, 255)


# 验证码颜色
def ran_color2():
    return randint(32, 127), randint(32, 127), randint(32, 127)


def random_images(r_path, image_name):
    num = 5  # 生成num位的验证码
    width = 50 * num  # 图宽
    height = 60  # 图高
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象 .tff为字体文件 可自定义
    font = ImageFont.truetype("arial", 50)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color())
    # 生成验证码
    for k in range(num):
        draw.text((50 * k + randint(1, 10), randint(0, 5)), rnd_char(), font=font, fill=ran_color2())
    # 对图片进行模糊处理
    image = image.filter(ImageFilter.GaussianBlur)
    image.save(r_path + "\\" + image_name + '.png', 'PNG')


class BashOrBat:
    # copy /b .\test.jpg + .\获取数据集坐标.zip test.png
    def __init__(self, **__args):
        # print(__args)
        self.get__image_timestamp = __args.get("get__image_timestamp", "")  # 获取的复制图片时间戳（只有随机生成图片时有内容）
        self.seed_pictures_path = __args.get("seed_pictures_path", "")  # 获取的复制图片路径/名称
        self.seed_file_path = __args.get("seed_file_path", "")  # 获取的复制文件路径
        self.get_pictures = __args.get("get_image", "")  # 最终生成图片名称

    def subprocess_check_output(self, *args):
        p = subprocess.Popen(*args, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        msg = []
        for line in out.splitlines():
            msg.append(line.decode(encoding='gbk'))
        if p.returncode != 0:
            print("Non zero exit code:%s executing: %s" % (p.returncode, args))
        return msg

    def running(self):
        # print(os.popen("echo Hello World").read()) tmp = os.popen("copy /b
        # E:\\data_source_project\\tools2\map-species\\newImage-157907751121118.png +
        # E:\\data_source_project\\tools2\\map-species\\inherit.zip getTest.png").readlines()
        picture_suffix_list = [".png", ".PNG", ".jpg", ".JPG", ".jpeg", ".JPEG", ".bmp", ".rgb", ".tif"]
        get_pictures_pass = False
        for __suffix in picture_suffix_list:
            if __suffix in self.get_pictures:
                get_pictures_pass = True
                break
            else:
                continue

        if not get_pictures_pass:
            self.get_pictures = self.get_pictures + ".png"
        if str(sys.platform) in ["win32", "win64"]:
            self.seed_file_path = str(self.seed_file_path).replace("/", "\\")
            if self.get__image_timestamp:
                r_path = str(self.seed_file_path).replace(str(self.seed_file_path).split("\\")[-1], "")
                try:
                    random_images(r_path, self.seed_pictures_path)
                    self.seed_pictures_path = r_path + "\\" + self.seed_pictures_path + ".png"
                except Exception as e:
                    return False, "创建随机图片错误！" + str(e)
            else:
                self.seed_pictures_path = str(self.seed_pictures_path).replace("/", "\\")
            try:
                tmp = self.subprocess_check_output(
                    "copy /b \"" +
                    self.seed_pictures_path +
                    "\" + \"" +
                    self.seed_file_path +
                    "\" " +
                    self.get_pictures)
            except Exception as e:
                return False, "运行命令错误！" + "\"" + self.seed_pictures_path + \
                       "\" + \"" + self.seed_file_path + "\" " + self.get_pictures + "----" + str(e)
            # self.seed_pictures_path = self.seed_pictures_path.replace("/", "\\")
            if self.get__image_timestamp:
                try:
                    del_tmp = self.subprocess_check_output("del \"" + self.seed_pictures_path + "\"")
                    # print(del_tmp)
                except:
                    pass
        else:
            self.seed_file_path = str(self.seed_file_path).replace("/", "\\")
            if self.get__image_timestamp:
                r_path = str(self.seed_file_path).replace(str(self.seed_file_path).split("\\")[-1], "")
                random_images(r_path, self.seed_pictures_path)
                self.seed_pictures_path = r_path + "\\" + self.seed_pictures_path + ".png"
            tmp = self.subprocess_check_output(
                "cat " +
                self.seed_pictures_path +
                " " +
                self.seed_file_path +
                " > " +
                self.get_pictures)
            # self.seed_pictures_path = self.seed_pictures_path.replace("/", "\\")
            if self.get__image_timestamp:
                try:
                    del_tmp = self.subprocess_check_output("rm -f " + self.seed_pictures_path)
                    # print(del_tmp)
                except:
                    pass
        for __s in tmp:
            if "已复制" in __s.__str__():
                return True, "恭喜你创建图种成功，接着下一个吧！"
            elif "命令语法不正确" in __s.__str__() or "指定的路径无效" in __s.__str__():
                return False, "命令错误:" + str(tmp)
        return True, "恭喜你创建图种成功，接着下一个吧！"


class MapSpecies(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def critical(self, set_text):
        QMessageBox.critical(self, '错误', set_text, QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        # msgBox = QMessageBox()
        # msgBox.setWindowTitle('错误')
        # msgBox.setIcon(QMessageBox.Critical)
        # msgBox.setText(set_text)
        # msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        # msgBox.setDefaultButton(QMessageBox.Yes)
        # msgBox.setDetailedText('这是详细的信息：学点编程吧，我爱你！')
        # reply = msgBox.exec()

        # if reply == QMessageBox.Retry:
        #     self.la.setText('你选择了Retry！')
        # elif reply == QMessageBox.Abort:
        #     self.la.setText('你选择了Abort！')
        # else:
        #     self.la.setText('你选择了Ignore！')

    def information_dialog(self, set_text):
        QMessageBox.information(self, '提示', set_text, QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)

    def initUI(self):
        # todo 架子搭建
        self.setGeometry(690, 300, 520, 200)
        # w.resize(250, 150)
        # w.move(300, 300)
        self.setWindowTitle('图种创建工具')
        self.setWindowIcon(QIcon('images/favicon.ico'))
        self.get__image_timestamp = ""
        self.to__image = ""
        # todo 提示信息
        self.lb0 = QLabel('重要提示：', self)
        self.lb0.move(20, 10)
        self.lb0.setStyleSheet('background-color: rgb(255, 251, 100)')
        self.lb0.setFont(QFont("微软雅黑", 15, QFont.Bold))
        self.lb00 = QLabel('建议用压缩文件建种，否则解种可能乱码！', self)
        self.lb00.move(120, 10)
        self.lb00.setStyleSheet('background-color: rgb(255, 251, 100)')
        self.lb00.setFont(QFont("微软雅黑", 15, QFont.StyleItalic))
        # todo 产出文件名对话框
        self.lb1 = QLabel('最终文件名称（.PNG）：', self)
        self.lb1.move(20, 50)
        self.to__image = 'toImage-' + str(time.time()).replace('.', '') + '.png'
        self.lb6 = QLabel(self.to__image, self)
        self.lb6.move(160, 50)
        self.bt1 = QPushButton('修改', self)
        self.bt1.move(400, 45)
        self.bt1.clicked.connect(self.showDialog)
        # todo 打开文件（图片）
        self.lbFileImage = QLabel('选择图片（种子图片）：', self)
        self.lbFileImage.move(20, 80)
        self.lineFileImage = QLineEdit(self)
        self.lineFileImage.setText("///")
        self.lineFileImage.setReadOnly(True)
        self.lineFileImage.setGeometry(160, 75, 170, 20)
        self.btFileImage = QPushButton('打开文件', self)
        self.btFileImage.move(350, 75)
        self.btRandomImage = QPushButton('随机生成', self)
        self.btRandomImage.move(430, 75)
        self.btRandomImage.clicked.connect(self.showDialog)
        self.btFileImage.clicked.connect(self.openfile)
        # fname = QFileDialog.getOpenFileName(self, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
        # todo 打开文件（种子）
        self.lbFile = QLabel('选择文件（种子文件）：', self)
        self.lbFile.move(20, 110)
        self.lineFile = QLineEdit(self)
        self.lineFile.setText("///")
        self.lineFile.setReadOnly(True)
        self.lineFile.setGeometry(160, 105, 170, 20)
        self.btFile = QPushButton('打开文件', self)
        self.btFile.move(400, 105)
        self.btFile.clicked.connect(self.openfile)
        # todo 生成种子
        self.generateTn = QPushButton('生成种子', self)
        self.generateTn.resize(75, 30)
        self.generateTn.move(300, 150)
        self.generateTn.clicked.connect(self.seed_generation)
        # todo 退出按钮
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(75, 30)
        qbtn.move(400, 150)

        # todo 展示
        self.show()

    # try:
    #     if len(sys.argv) < 2:
    #         raise ValueError
    #     else:
    #         title = " ".join(sys.argv[1:])
    # except ValueError:
    #     title = "学点编程吧出品"
    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, '修改最终图片名称', '文件名称：')
            if ok:
                self.lb6.setText(text)
                self.to__image = text
            else:
                self.critical("修改最终图片名称失败，请重试！")
        elif sender == self.btRandomImage:
            self.get__image_timestamp = str(time.time()).replace('.', '')
            # random_images.random_images("Image-" + get_timestamp)
            self.lineFileImage.setText("Image-" + self.get__image_timestamp)

    def openfile(self):
        sender = self.sender()
        if sender == self.btFileImage:
            fname = QFileDialog.getOpenFileName(self, '打开文件', './', ("Images (*.png *.xpm *.jpg)"))
            if fname[0]:
                file_path = fname[0].__str__()
                self.lineFileImage.setText(file_path)
                self.get__image_timestamp = ""
            else:
                self.critical("导入图片失败，请重新填入！")
        elif sender == self.btFile:
            fname = QFileDialog.getOpenFileName(self, '打开文件', './')
            if fname[0]:
                file_path = fname[0].__str__()
                self.lineFile.setText(file_path)
            else:
                self.critical("导入文件失败，请重新填入！")

    def seed_generation(self):
        sender = self.sender()
        if sender == self.generateTn:
            to_data = {
                "get__image_timestamp": self.get__image_timestamp,
                "seed_pictures_path": self.lineFileImage.text(),
                "seed_file_path": self.lineFile.text(),
                "get_image": self.to__image
            }
            # print(to_data)
            __bool, re_message = BashOrBat(**to_data).running()
            if __bool:
                # if True:
                print("创建成功")
                self.get__image_timestamp = ""
                self.lineFileImage.setText("///")
                self.lineFile.setText("///")
                self.to__image = 'toImage-' + str(time.time()).replace('.', '') + '.png'
                self.lb6.setText(self.to__image)
                self.information_dialog(re_message)
            else:
                # self.critical("创建图种失败，请查看配置参数，重新填入！")
                self.critical(re_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapSpecies()
    sys.exit(app.exec_())
