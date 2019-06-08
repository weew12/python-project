# -*- coding: utf-8 -*-

"""
   File Name：     t2
   Description :
   Author :        枫weew12
   date：          2019/4/16
   Change Activity:2019/4/16:
"""
import cv2

img1 = cv2.imread(r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\card\test.jpeg', 0)

# 反相
im = img1.copy()
height, width = im.shape
for i in range(height):
    for j in range(width):
        im[i, j] = 255 - im[i, j]
cv2.imshow('ttt', im)
cv2.waitKey(0)

img2 = cv2.add(im, im)
cv2.imshow('tt', im)
cv2.waitKey(0)

img3 = cv2.add(img2, im)
cv2.imshow('t', img3)
cv2.waitKey(0)

str = 'ddd'
str.strip('d')