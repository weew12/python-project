# -*- coding: utf-8 -*-

"""
   File Name：     pitture_file
   Description :
   Author :        枫weew12
   date：          2019/5/12
   Change Activity:2019/5/12
"""
import cv2

filename = ''

for i in range(1, 19):
    name = './pic/' + str(i) + '.jpg'

    img = cv2.imread(name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img2 = gray.copy()

    height, width = img2.shape

    print(height, width)

    for i in range(height):
        for j in range(width):
            img2[i, j] = 255 - img2[i, j]


    cv2.imshow("xx",img2)
    cv2.imwrite(name, img2)
    cv2.waitKey(0)
