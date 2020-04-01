#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 13:45
# @Author  : Rainogong
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import os
import random
import time
import subprocess

import cv2
import numpy as np

def start_onmyoji()
    os.system('adb shell am start -D -n com.netease.onmyoji.mi/com.netease.onmyoji.Launcher')

#解决cv2.imread()不能读入中文路径问题，这里转换中文格式
def cv2_repath(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img

def adb_connect():
    # os.system('adb connect 192.168.1.139:5555')
    os.system('adb connect 192.168.2.182:5555')
def get_screenshot_img():
    # 使用subprocess的Popen调用adb shell命令，并将结果保存在PIPE管道中
    process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
    # 读取管道中的数据
    screenshot = process.stdout.read()
    # 将读取字节流数据的回车换行换成'\n'
    binary_screenshot = screenshot.replace(b'\r\n', b'\n')
    # 使用numpy和imdecode将二进制数据转换成cv2的mat图片格式
    img_screenshot = cv2.imdecode(np.frombuffer(binary_screenshot, np.uint8), cv2.IMREAD_COLOR)
    return img_screenshot

def creat_screenshot_file():
    os.system('adb connect 192.168.2.182:5555')
    os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png screencap.png')

def recog_png(temple_png, show):
#    img = cv2.imread(img_png, cv2.IMREAD_COLOR)
    img = get_screenshot_img()
    temple = cv2.imread(temple_png, cv2.IMREAD_COLOR)
    w, h = temple.shape[-2::-1]
    result = cv2.matchTemplate(img, temple, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print('recong_png max_val = ' + str(max_val))
    if show == 1:
        cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (7,249,151), 6)
        cv2.imshow('img', img)
        cv2.waitKey(0)
    return max_val, max_loc, w, h

def click(threshold, max_val, max_loc, w, h):
    urx = max_loc[0] + w
    ury = max_loc[1] + h
    centx = (max_loc[0] + urx)/2
    centy = (max_loc[1] + ury)/2
    if max_val > threshold:
        command = 'adb shell input tap ' + str(centx) + ' ' + str(centy)
        os.system(command)
        print(command)

def make_group():
    get_screenshot_img()
    max_val, max_loc, w, h = recog_png('png\juanzhou.png', 0)
    click(0.5, max_val, max_loc, w, h)
    time.sleep(2)
    max_val, max_loc, w, h = recog_png('png\zudui.png', 0)
    click(0.75, max_val, max_loc, w, h)

def shiju():
    get_screenshot_img()
    max_val, max_loc, w, h = recog_png('png\shiju.png', 0)
    click(0.9, max_val, max_loc, w, h)
    time.sleep(1)
    get_screenshot_img()
    pipei_flage, max_loc, w, h = zidongpipei()
    if pipei_flage == 1:
        click(0.9, max_val, max_loc, w, h)


def nianshou():
    get_screenshot_img()
    max_val, max_loc, w, h = recog_png('png\\nianshou.png', 1)

def jinbiyaoguai():
    get_screenshot_img()
    max_val, max_loc, w, h = recog_png('png\\jinbiyaoguai.png', 1)

def jingyanyaoguai():
    get_screenshot_img()
    max_val, max_loc, w, h = recog_png('png\\jingyanyaoguai.png', 1)

def zidongpipei():
    get_screenshot_img()
    max_val, max_loc, w, h = recog_png('png\\zidongpipei.png', 0)
    pipei_flag = 0
    if max_val > 0.9:
        pipei_flag = 1
    return pipei_flag, max_loc, w, h



# make_group()
# get_screenshot()
# get_start('screencap.png', 'png\huazhou.png')

#shiju()
#nianshou()
#jinbiyaoguai()
#jingyanyaoguai()
#zidongpipei()
#adb_connect()
img = get_screenshot_img()
cv2.imwrite('screencap.png', img)
#cv2.imshow('1', img)
#cv2.waitKey(0)



