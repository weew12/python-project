# -*- coding: utf-8 -*-

"""
   File Name：     卡号定位
   Description :    对特定的建行卡定位切割出卡号区域并且二值化处理
   Author :        枫weew12
   date：          2019/4/13
   Change Activity:2019/4/13
"""
import cv2

img_path = r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\card\6.jpeg'

img = cv2.imread(img_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image_gary', gray)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(gray, (9, 9),0)
cv2.imshow('image_blurred', blurred)
cv2.waitKey(0)

gradX = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=1, dy=0)
gradY = cv2.Sobel(blurred, ddepth=cv2.CV_32F, dx=0, dy=1)
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
cv2.imshow('image_gradient', gradient)
cv2.waitKey(0)

blurred1 = cv2.GaussianBlur(gradient, (9, 9),0)
(_, thresh) = cv2.threshold(blurred1, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('image_blurred1', blurred1)
cv2.waitKey(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (40, 40))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('ket', closed)
cv2.waitKey(0)

# 腐蚀
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
erosion = cv2.erode(closed, kernel2, iterations=6)
cv2.imshow('ket2', erosion)
cv2.waitKey(0)

# 膨胀
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT,(6, 6))
dil = cv2.dilate(erosion, kernel3, iterations=15)
cv2.imshow('ket3', dil)
cv2.waitKey(0)

temp = dil.copy()

# 边框裁剪
_, contours, hierarchy = cv2.findContours(temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 画出轮廓
cv2.drawContours(img, contours, 1, (0, 200, 0), 2)
x, y, w, h = cv2.boundingRect(contours[4])
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 200), 2)

# 卡号区域
img_save = img[y:y+h, x:x+w]
cv2.imshow('Cge', img_save)
cv2.waitKey()

# 卡号二值化
img_save1  = cv2.cvtColor(img_save, cv2.COLOR_BGR2GRAY)
(_, img_bin) = cv2.threshold(img_save1, 126, 255, cv2.THRESH_BINARY)
cv2.imshow('Cg', img_bin)
cv2.waitKey()

kernel4 = cv2.getStructuringElement(cv2.MORPH_RECT,(2, 2))
erosion = cv2.erode(img_save1, kernel4, iterations=4)
cv2.imshow('C', erosion)
cv2.waitKey()

height, width = erosion.shape
for i in range(height):
    for j in range(width):
        if erosion[i, j] > 50:
            erosion[i, j] = 255
cv2.imshow('res', erosion)
cv2.waitKey(0)

kernel4_ = cv2.getStructuringElement(cv2.MORPH_RECT,(2, 2))
erosion = cv2.dilate(erosion, kernel4_, iterations=4)
cv2.imshow('res', erosion)
cv2.waitKey(0)

# 腐蚀
# 无噪声卡号
test_img = erosion.copy()

kernel_tes = cv2.getStructuringElement(cv2.MORPH_RECT,(1, 1))
erosion = cv2.erode(test_img, kernel_tes, iterations=3)
cv2.imshow('l', erosion)
cv2.waitKey(0)

# cv2.imwrite('test.jpg', erosion)
# 字符切割
# 垂直投影
height, width = erosion.shape
for i in range(height):
    for j in range(width):
        if erosion[i, j] != 255:
            erosion[i, j] = 0

cv2.imshow('ett', erosion)
cv2.waitKey(0)
cv2.imwrite('test.jpg', erosion)