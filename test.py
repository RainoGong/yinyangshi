#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 22:25
# @Author  : Rainogong
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import cv2
import os

"""
img = cv2.imread('png\卷轴.png', cv2.IMREAD_COLOR)
print(img)
cv2.imshow('juanzhou', img)
cv2.waitKey(0)
"""

os.system('adb connect 192.168.1.139:5555')
os.system('adb shell am start -D -n com.netease.onmyoji.mi/com.netease.onmyoji.Launcher')