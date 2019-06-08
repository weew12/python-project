# -*- coding: utf-8 -*-

"""
   File Name：     read_folder_file_list
   Description :    读取文件下的文件 并获得文件名
   Author :        枫weew12
   date：          2019/4/10
   Change Activity:2019/4/10:
"""
import os
import re

dir_data = os.listdir(r'J:\银行卡\资料下载\images')

# 文件名列表
file_name = []
for i in dir_data:
    file_name.append(i)

# print(file_name)
# print(len(file_name))

pattern = re.compile(r'(^.*?)[a-z]')

res = []
for i in file_name:
    print('--->', i)
    mid = pattern.match(i).group(1)
    res.append(mid)
    print(mid)


