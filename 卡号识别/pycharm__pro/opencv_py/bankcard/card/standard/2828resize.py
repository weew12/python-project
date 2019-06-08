# -*- coding: utf-8 -*-

"""
   File Name：     2828resize
   Description :
   Author :        枫weew12
   date：          2019/4/17
   Change Activity:2019/4/17:
"""
import cv2

img = cv2.imread(r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\pic0.jpg')
cv2.imshow('test1', img)
cv2.waitKey(0)

img2 = cv2.resize(img,(28, 28))
cv2.imshow('test2', img2)
cv2.imwrite('tt.jpg',img2)
cv2.waitKey(0)
