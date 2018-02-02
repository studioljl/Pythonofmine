import os
from PIL import Image
from PIL import ImageDraw
import time

VERSION='0.1'

def debug():
    im = Image.open('1.png')
    print(im.format,im.size,im.mode)
    draw = ImageDraw.Draw(im)
    draw.line((0,0,540,980),fill=128)
    draw.line((0,0,1000,80),fill=128)
    im.show()

def deal():
    img = Image.open('1.png')
    img = img.convert('RGB')
    src = img.load()
    data = src[540,980]
    print(data)
    if data[0]== 0 and data[1]== 122 and data[2]==255:
        print("AD未开始")
        print("开始AD")
        os.system('adb shell input tap 540 980')
    else:
        print("AD running")
        os.system('adb shell input tap 1000 80')


def main():

    print('程序版本号：{}'.format(VERSION))
    os.system('adb version')
    os.system('adb devices')
    while True:
        try:
            os.system('adb shell screencap -p /sdcard/1.png')
            print('Screencap successed')
            os.system('adb pull /sdcard/1.png .')
            deal()
        except:
            print('Screencap failed')
            return
        
        time.sleep(5)


if __name__ == '__main__':
    main()