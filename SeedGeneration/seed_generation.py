#!/usr/bin/python3
# -*-coding:utf-8-*-
import os
import sys

from RandomImages import random_images


class BashOrBat:
    # copy /b .\test.jpg + .\获取数据集坐标.zip test.png
    def __init__(self, **__args):
        # print(__args)
        self.get__image_timestamp = __args.get("get__image_timestamp", "")  # 获取的复制图片时间戳（只有随机生成图片时有内容）
        self.seed_pictures_path = __args.get("seed_pictures_path", "")  # 获取的复制图片路径/名称
        self.seed_file_path = __args.get("seed_file_path", "")  # 获取的复制文件路径
        self.get_pictures = __args.get("get_image", "")  # 最终生成图片名称

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
            if self.get__image_timestamp:
                random_images.random_images(self.seed_pictures_path)
                self.seed_pictures_path = str(sys.path[0]) + "\\" + self.seed_pictures_path + ".png"
            tmp = os.popen(
                "copy /b \"" +
                self.seed_pictures_path +
                "\" + \"" +
                self.seed_file_path +
                "\" " +
                self.get_pictures).readlines()
            # self.seed_pictures_path = self.seed_pictures_path.replace("/", "\\")
            try:
                del_tmp = os.popen("del \"" + self.seed_pictures_path + "\"").readlines()
                # print(del_tmp)
            except:
                pass
        else:
            if self.get__image_timestamp:
                random_images.random_images(self.seed_pictures_path)
                self.seed_pictures_path = str(sys.path[0]) + "/" + self.seed_pictures_path + ".png"
            tmp = os.popen(
                "cat " +
                self.seed_pictures_path +
                " " +
                self.seed_file_path +
                " > " +
                self.get_pictures).readlines()
            # self.seed_pictures_path = self.seed_pictures_path.replace("/", "\\")
            try:
                del_tmp = os.popen("rm -f " + self.seed_pictures_path).readlines()
                # print(del_tmp)
            except:
                pass
        for __s in tmp:
            if "已复制" in __s.__str__():
                return True
            elif "命令语法不正确" in __s.__str__() or "指定的路径无效" in __s.__str__():
                return False
        return True


if __name__ == '__main__':
    print(BashOrBat().running())
