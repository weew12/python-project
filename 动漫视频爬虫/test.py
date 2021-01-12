# -*- coding: utf-8 -*-

import requests
import time
from multiprocessing import Pool
import os
import re
# 代理池
proxi = [
    {'http': 'http://221.6.201.18:9999'},
    {'http': 'http://122.136.212.132:53281'},
    {'http': 'http://221.229.252.98:9797'},
    {'http': 'http://58.249.55.222:9797'},
    {'http': 'http://58.243.50.184:53281'}
]

# 根地址
origin_url = 'https://sina.com-h-sina.com/20180905/18067_5102aee2/800k/hls/'


def get_url():  # 获取url 索引表
    root_url = "https://mhkuaibo.com/20191228/B2hahatr/1200kb/hls/"

    urls = list()

    pattern = re.compile('(.*).ts')

    with open("index.m3u8", 'r') as file:
        res = file.readlines()
        for i in res:
            if re.findall(pattern, i):
                urls.append(root_url + i.split('/')[-1].strip('\n'))

    return urls, len(urls)


def download(url, which, name):   # 下载 存储
    response = requests.get(url, proxies=which)
    with open('mp/{}'.format(name+'.ts'), 'wb') as file:
        try:
            file.write(response.content)
            # time.sleep(0.5)
            print('{} {}  ok '.format(url, name))
        except IOError as error:
            print('出错')
            print(error)


def check_exits(file):    # 检查文件是否已经下载
    if os.path.exists('./mp/{}'.format(file)):
        return True
    return False


if __name__ == '__main__':
    # 获取分片视频的文件url 视频总长度
    video, lenth = get_url()
    print(lenth)
    # 创建四个进程池 分别使用不同的代理
    pool1 = Pool(10)
    pool2 = Pool(10)
    pool3 = Pool(10)
    pool4 = Pool(10)

    for i in range(lenth)[::4]:
        try:
            if check_exits(str(i)+'.ts'):
                print('{} exits'.format(video[i]))
            else:
                pool1.apply_async(download, (video[i], proxi[1], str(i)))
            if check_exits(str(i+1)+'.ts'):
                print('{} exits'.format(video[i+1]))
            else:
                pool2.apply_async(download, (video[i+1], proxi[2], str(i+1)))
            if check_exits(str(i+2)+'.ts'):
                print('{} exits'.format(video[i+2]))
            else:
                pool1.apply_async(download, (video[i+2], proxi[3], str(i+2)))
            if check_exits(str(i+3)+'.ts'):
                print('{} exits'.format(video[i+3]))
            else:
                pool1.apply_async(download, (video[i+3], proxi[4], str(i+3)))
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
