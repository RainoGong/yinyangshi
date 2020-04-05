#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 22:25
# @Author  : Rainogong
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import cv2
import os
import win32gui
import win32ui
import win32con
import win32api
import numpy as  np
from ctypes import windll
from PIL import Image




"""
img = cv2.imread('png\卷轴.png', cv2.IMREAD_COLOR)
print(img)
cv2.imshow('juanzhou', img)
cv2.waitKey(0)
"""
""""
os.system('adb connect 192.168.1.139:5555')
os.system('adb shell am start -D -n com.netease.onmyoji.mi/com.netease.onmyoji.Launcher')
"""

""""
hwnd = win32gui.FindWindow(None, '阴阳师-网易游戏')
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
width = right - left
height = bottom - top

hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()
saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
saveDC.SelectObject(saveBitMap)
# saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)
saveBitMap.SaveBitmapFile(saveDC, "img_Winapi.bmp")
"""

def get_screen_size():
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    return screen_width, screen_height
def get_window_onmyoji():
    hwnd = win32gui.FindWindow(None, '阴阳师-网易游戏')
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    return hwnd, width, height, left, top
def move_window_onmyoji_bl():
    hwnd = get_window_onmyoji()[0]
    win32gui.SetForegroundWindow(hwnd)
    screen_width, screen_height = get_screen_size()
    # onmyoji默认窗口大小1152*679， 现有屏幕分辨率为2K
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, screen_height, 1152, 679, win32con.SWP_SHOWWINDOW)
def move_window_onmyoji_ul():
    hwnd = get_window_onmyoji()[0]
    win32gui.SetForegroundWindow(hwnd)
    # screen_width, screen_height = get_screen_size()
    # onmyoji默认窗口大小1152*679， 现有屏幕分辨率为2K
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 1152, 679, win32con.SWP_SHOWWINDOW)
def get_image_onmyoji():
    hwnd, width, height, loc_x, loc_y = get_window_onmyoji()
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bitmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息,下面是获取了显示器的分辨率,之前已有函数实现，这里只是给出另一个参考方法
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    screen_width = MoniterDev[0][2][2]
    screen_height = MoniterDev[0][2][3]
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, 1152, 679)
    # 高度saveDC，将截图保存在saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0， 1440）长宽为（1152，679）的图片
    # 下面的程序截图是黑屏，所以这里换一种方式
    """
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (loc_x, loc_y), win32con.SRCCOPY)
    # 保存图像
    saveBitMap.SaveBitmapFile(saveDC, 'onmyoji.png')
    # 获取图像
    image = saveBitMap.GetBitmapBits(False)
    image_unit8 = np.array(image).astype(dtype="uint8")
    image_unit8.shape = (height, width, 4)
    return image_unit8
    # return loc_x, loc_y
    """
    # 这里直接能输出后台程序图像
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    print(result)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    im.save('im.png')
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    if result == 1:
        img_screenshot = np.array(im).astype(dtype="uint8")

        return img_screenshot

move_window_onmyoji_ul()
while(True):
    img = get_image_onmyoji()
    cv2.imshow('1', img)
    cv2.waitKey(2)
#get_image_onmyoji()

