# -*- coding: utf-8 -*-

"""
   File Name：     图片叠加清晰化
   Description :
   Author :        枫weew12
   date：          2019/4/16
   Change Activity:2019/4/16:
"""
# coding=utf-8
import cv2
import numpy as np

def get_img():
    img = cv2.imread(r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\card\test.jpeg', 0)

    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)# 转回uint8
    absY = cv2.convertScaleAbs(y)

    dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    # cv2.imshow("absX", absX)
    # cv2.imshow("absY", absY)

    cv2.imshow("Result", dst)

    cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img2 = dst.copy()
    img3 = cv2.add(dst, img2)
    cv2.imshow('diejia', img3)
    cv2.waitKey(0)


    img4 = cv2.add(img3, img2)
    cv2.imshow('diejia4', img4)
    cv2.waitKey(0)

    img5 = cv2.add(img4, img2)
    cv2.imshow('diejia45', img5)
    cv2.waitKey(0)

    return img5

