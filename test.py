#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 22:25
# @Author  : Rainogong
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import cv2

img = cv2.imread('png\卷轴.png', cv2.IMREAD_COLOR)
print(img)
cv2.imshow('juanzhou', img)
cv2.waitKey(0)