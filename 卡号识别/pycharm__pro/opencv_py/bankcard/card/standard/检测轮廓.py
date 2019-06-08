# -*- coding: utf-8 -*-

"""
   File Name：     检测轮廓
   Description :
   Author :        枫weew12
   date：          2019/4/16
   Change Activity:2019/4/16:
"""
import cv2
import 图片叠加清晰化

img = 图片叠加清晰化.get_img()

img1 = cv2.imread(r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\card\test.jpeg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找二值化图中的轮廓
image, contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))  # 结果应该为

cv2.imshow('test', cv2.drawContours(img1, contours, -1, (0, 0, 255), 2))
cv2.waitKey(0)


