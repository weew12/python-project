# -*- coding: utf-8 -*-

"""
   File Name：     parseURL_from_musicList
   Description :    将歌单信息存储到数据库mysql
   Author :        枫weew12
   date：          2019/5/12
   Change Activity:2019/5/12
"""

import json
import os
import pymysql


db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    port=3306
)
cursor = db.cursor()

# 插入数据库
sql1 = """use music;"""
cursor.execute(sql1)

# 歌单文件
m_list = [x for x in os.listdir(r'./音乐爬取')]

# 计数器
count = 0

for name in m_list:
    count += 1
    print('歌单%s存储中' % count)

    with open(r'./音乐爬取/' + name, 'r', encoding='utf-8') as file_in:
        str_file = json.load(file_in)

        for i in str_file["data"]:
            if i["description"]:
                pass
            else:
                i["description"] = 'null'

            sql2 = "insert into two(sort_id,id,tb_title,desci,img_url,song_num) values(null,%d,'%s','%s','%s',%d)" \
                   % (
                       int(i["id"]),
                       i["title"].replace("'", ""),
                       i["description"].replace("'", ""),
                       i["coverImgUrl"],
                       i["songNum"]
                   )
            cursor.execute(sql2)

    print('歌单%s存储完成' % count)

db.commit()
db.close()

