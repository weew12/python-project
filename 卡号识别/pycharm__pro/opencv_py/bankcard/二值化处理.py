# -*- coding: utf-8 -*-

"""
   File Name：     二值化处理
   Description :
   Author :        枫weew12
   date：          2019/4/13
   Change Activity:2019/4/13:
"""

import cv2
import numpy as np

# 原始图片的灰度图
img_gray = cv2.imread(r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\card\1.jpeg', 0)
cv2.imshow('image_gary', img_gray)
cv2.waitKey(0)

#二值化图片
img_2 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('bin_img', img_2[1])
cv2.waitKey(0)

# # 翻转
#
# img_3 = img_gray.copy()
# height, width = img_3.shape
# for i in range(height):
#     for j in range(width):
#         img_3[i, j] = 255 - img_3[i, j]
#
# cv2.imshow('image3', img_3)
# cv2.waitKey(0)

# 测试图
img4 = img_gray.copy()
height, width = img4.shape

for i in range(height):
    for j in range(width):
        if img4[i, j] > 150:
            pass
        else:
            img4[i, j] = 0

cv2.imshow('test', img4)
cv2.waitKey(0)
