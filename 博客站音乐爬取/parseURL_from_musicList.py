# -*- coding: utf-8 -*-

"""
   File Name：     parseURL_from_musicList
   Description :
   Author :        枫weew12
   date：          2019/5/12
   Change Activity:2019/5/12
"""

import requests
import time
import json


class ParseMusicList(object):
    """
    通过给出的歌单id song_num 请求歌单数据
    返回json 格式的歌单数据
    """
    def __init__(self, id_, song_num):
        """
        :param id_: 歌单地址
        :param song_num: 歌曲总数
        """
        self.id = id_
        self.num = song_num
        self.link = 'https://zeus-ui.com/api/musics/songList?limit=%d&id=%d'

    def request_url(self):
        """
        :return: 请求歌单数据的地址
        """
        music_list_url = self.link % (self.num, self.id)
        print(music_list_url)
        return music_list_url

    def get_data(self):
        """
        :return: 得到歌单数据
        """
        requests_url = self.request_url()
        response = requests.get(requests_url)
        print(str(self.id) + '请求数据中')
        if response.status_code == 200:
            print('请求成功')
        else:
            print('请求出错%s' % response.status_code)
        return response.text


class SaveMusicListData(object):
    """
    获取歌单数据 保存为id 命名的json文件
    """
    def __init__(self, id_, song_num):
        self.Save_Path = './musics/'
        self.id_ = id_
        self.num = song_num

    def save_data(self):
        parse_data = ParseMusicList(self.id_, self.num)
        with open(self.Save_Path + str(parse_data.id) + '.json', 'w', encoding='utf-8') as file_out:
            file_out.write(parse_data.get_data())
            print('保存成功')


def test_save_one_list():
    with open('./音乐爬取/轻音乐歌单.json', 'r', encoding='utf-8') as file_in:
        data = json.load(file_in)
        musics = data["data"]

        for item in musics:
            id_ = item["id"]
            song_num = item["songNum"]
            save = SaveMusicListData(id_, song_num)
            save.save_data()
            time.sleep(2)
    print('此歌单提取子歌单完成')


if __name__ == "__main__":
    test_save_one_list()
