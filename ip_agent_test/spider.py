# -*- coding: utf-8 -*-

"""
   File Name：     尝试爬取
   Description :
   Author :        枫weew12
   date：          2019/5/15
   Change Activity:2019/5/15
"""

import requests
import os
import json
import time

pro = [{'http': 'http://58.243.50.184:53281'},
       {'http': 'http://27.46.23.148:8888'},
       {'http': 'http://124.205.155.154:9090'},
       {'http': 'http://124.205.155.150:9090'},
       {'http': 'http://47.95.201.41:3128'},
       {'http': 'http://14.20.235.7:808'},
       {'http': 'http://58.249.55.222:9797'},
       {'http': 'http://111.40.84.73:9797'},
       {'http': 'http://124.205.155.151:9090'},
       {'http': 'http://119.90.126.106:7777'},
       {'http': 'http://222.74.61.98:53281'}]


class GetMusicsId(object):

    def __init__(self):
        self.musics_dic = {}
        self.song_num = 0
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/70.0.3538.110 Safari/537.36"
        }

    def open_file(self):
        with open('G:/python 资源/python project/博客站音乐爬取/musics/77629049.json', 'r', encoding='utf-8') as file_in:
            data = json.load(file_in)
            self.musics_dic = data["data"]["songs"]
            self.song_num = int(data["data"]["songListCount"])
            # print(self.musics_dic)

    def get_music(self):
        start = time.time()
        count = 1
        print('歌单包含歌曲 %d 首' % self.song_num)
        for item in self.musics_dic:

            # 使用哪个代理
            which_pro = pro[count % len(pro)]
            # 如果文件存在就跳过 否则尝试获取
            if os.path.exists('./test_musics3/' + str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3'):
                continue
            else:
                print('./test_musics3/' + str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3')

                try:
                    print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '下载中......')
                    response = requests.get(item["url"], proxies=which_pro)

                except requests.RequestException as err:
                    print(err)
                    print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '文件写入失败')
                    continue

                try:
                    with open('./test_musics3/' + str(item["name"])
                              + '(' + str(item["singer"] + ')' + '.mp3'), 'wb') as file:
                        file.write(response.content)
                    print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '文件写入成功')

                except IOError as err:
                    print(err)
                    print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '文件写入失败')
                    continue

            # 计数加一
            count += 1
        end = time.time()
        consume = end - start
        print('花费时间：%d' % consume)

    def get_download_list(self):
        num = self.song_num
        detail = os.listdir('./test_musics3')
        print('下载歌曲共 %d 首' % len(detail))
        not_download = num - len(detail)
        print('全部下载成功') if not_download == 0 else print('%d 首下载失败' % not_download)
        # print(detail)


test = GetMusicsId()
test.open_file()
test.get_music()
test.get_download_list()