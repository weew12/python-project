import requests
import time
from multiprocessing import Pool
import os
import re


def get_url():  # 获取url 索引表
    # root_url = "https://mhkuaibo.com/"

    urls = list()

    pattern = re.compile('(.*).ts')

    with open("index.m3u8", 'r') as file:
        res = file.readlines()
        for i in res:
            if re.findall(pattern, i):
                urls.append(i.split('/')[-1].strip('\n'))

    return urls, len(urls)


def check_exits(file):    # 检查文件是否已经下载
    if os.path.exists('./mp2/{}'.format(file)):
        print('ok')
        return True
    return False


if __name__ == "__main__":
    # vedio, lenth = get_url()
    # print(vedio)
    # print('begin')
    # for pos, i in enumerate(vedio):
    #     # print(pos+1, i)
    #     if check_exits(i):
    #         print(i+'ok')
    # print(os.path.exists('./mp2/{}'.format('XnC0Prbi.ts')))

    for i in range(120)[::4]:
        print(i)
        print(i+1)
        print(i+2)
        print(i+3)
