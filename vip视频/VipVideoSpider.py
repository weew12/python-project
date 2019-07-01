# -*- coding: utf-8 -*-

"""
   File Name：     t1
   Description :
   Author :        weew12
   date：          2019/7/1
"""
import requests
import time
from multiprocessing import Pool
import os

# 代理池
proxi = [
    {'http': 'http://183.247.152.98:53281'},
    {'http': 'http://58.249.55.222:9797'},
    {'http': 'http://59.44.247.194:9797'},
    {'http': 'http://119.90.126.106:7777'},
    {'http': 'http://220.180.50.14:53281'}
]

# 根地址
origin_url = 'https://sina.com-h-sina.com/20180905/18067_5102aee2/800k/hls/'


def get_url():  # 获取url 索引表
    data = []
    with open("index.m3u8", 'r', encoding='utf-8') as file:
        mid = file.readlines()
        for pos, i in enumerate(mid):
            if mid[pos][0] == '#':
                continue
            else:
                data.append(i.strip('\n'))

    split_video = []
    for j in data:
        split_video.append(origin_url+j)
    return split_video, len(split_video)


def download(url, which):   # 下载 存储
    response = requests.get(url, proxies=which)
    with open('mp/{}'.format(url[-10:]), 'wb') as file:
        try:
            file.write(response.content)
            # time.sleep(0.5)
            print('{}  ok '.format(url))
        except IOError as error:
            print(error)


def check_exits(file):    # 检查文件是否已经下载
    if os.path.exists('./mp/{}'.format(file[-10:])):
        return True
    return False


if __name__ == '__main__':
    # 获取分片视频的文件url 视频总长度
    video, lenth = get_url()
    # 创建四个进程池 分别使用不同的代理
    pool1 = Pool(10)
    pool2 = Pool(10)
    pool3 = Pool(10)
    pool4 = Pool(10)

    for i in range(lenth)[::4]:
        try:
            if check_exits(video[i]):
                print('{} exits'.format(video[i]))
            else:
                pool1.apply_async(download, (video[i], proxi[1]))
            if check_exits(video[i]):
                print('{} exits'.format(video[i+1]))
            else:
                pool2.apply_async(download, (video[i+1], proxi[2]))
            if check_exits(video[i]):
                print('{} exits'.format(video[i+2]))
            else:
                pool1.apply_async(download, (video[i+2], proxi[3]))
            if check_exits(video[i]):
                print('{} exits'.format(video[i+3]))
            else:
                pool1.apply_async(download, (video[i+3], proxi[4]))
            time.sleep(0.5)
        except Exception as err:
            print(err)
    pool1.close()
    pool1.join()
    pool2.close()
    pool2.join()
    pool3.close()
    pool3.join()
    pool4.close()
    pool4.join()
