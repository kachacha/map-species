# -*-coding:utf-8-*-

from random import randint, choice

from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 随机ASCII码生成数字或大小写字母
def rnd_char():
    return chr(choice([randint(48, 57), randint(65, 90), randint(97, 122)]))


# 背景颜色
def rnd_color():
    return randint(64, 255), randint(64, 255), randint(64, 255)


# 验证码颜色
def ran_color2():
    return randint(32, 127), randint(32, 127), randint(32, 127)


def random_images(image_name):
    num = 5  # 生成num位的验证码
    width = 50 * num  # 图宽
    height = 60  # 图高
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象 .tff为字体文件 可自定义
    font = ImageFont.truetype("Typeface/Arial Black.ttf", 50)
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
    image.save(image_name + '.png', 'PNG')


if __name__ == '__main__':
    random_images("asd123")
