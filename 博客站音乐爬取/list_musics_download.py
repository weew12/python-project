# -*- coding: utf-8 -*-

"""
   File Name：     list_musics_download
   Description :    下载音乐歌单的歌曲到本地
   Author :        枫weew12
   date：          2019/5/14
   Change Activity:2019/5/14
"""
import requests
import os
import time
import json


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
        with open('./musics/77629049.json', 'r', encoding='utf-8') as file_in:
            data = json.load(file_in)
            self.musics_dic = data["data"]["songs"]
            self.song_num = int(data["data"]["songListCount"])
            # print(self.musics_dic)

    def get_music(self):
        print('歌单包含歌曲 %d 首' % self.song_num)
        for item in self.musics_dic:
            print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '下载中......')
            try:
                response = requests.get(item["url"])

            except requests.RequestException as err:
                print(err)
                print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '文件写入失败')
                continue

            try:
                with open('./test_musics/' + str(item["name"])
                          + '(' + str(item["singer"] + ')' + '.mp3'), 'wb') as file:
                    file.write(response.content)
                print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '文件写入成功')

            except IOError as err:
                print(err)
                print(str(item["name"]) + '(' + str(item["singer"]) + ')' + '.mp3' + '文件写入失败')
                continue

            # 休眠一段时间
            time.sleep(3.5)

    def get_download_list(self):
        num = self.song_num
        detail = os.listdir('./test_musics')
        print('下载歌曲共 %d 首' % len(detail))
        not_download = num - len(detail)
        print('全部下载成功') if not_download == 0 else print('%d 首下载失败' % not_download)
        print(detail)


test = GetMusicsId()
# test.open_file()
# test.get_music()
test.get_download_list()