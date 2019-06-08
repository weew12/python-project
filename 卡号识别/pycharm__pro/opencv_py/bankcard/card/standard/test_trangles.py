# -*- coding: utf-8 -*-

import cv2
import numpy as np

def drawRotatedRect(rect, image):
   box = cv2.boxPoints(rect)
   x0, y0 = box[0]
   for i in range(3):
      x, y = box[i]
      x1, y1 = box[i + 1]
      cv2.line(image, (x, y), (x1, y1), (0, 0, 255), 2)
      if i is 2:
         cv2.line(image, (x1, y1), (x0, y0), (0, 0, 255), 2)

img = cv2.imread(r'C:\Users\ASUS\Desktop\pycharm__pro\opencv_py\bankcard\card\1.jpeg')
# 图像预处理
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)
# 寻找轮廓
_, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 得到矩形框的相关参数
rect = cv2.minAreaRect(contours[1])
x, y = rect[0]
w, h = rect[1]
angle = rect[2]
print('center:'+str(int(x))+','+str(int(y))+' w,h:'+str(int(w))+','+str(int(h))+' angle:'+str(int(angle)))
# 画出旋转的矩形框
drawRotatedRect(rect, img)

cv2.imshow('Contours Image', img)
cv2.waitKey()
cv2.destroyAllWindows()()