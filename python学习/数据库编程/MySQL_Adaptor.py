# -*- coding:utf-8 -*-
'''
    Created on: 2019-08-31
    description: 
    @auther: weew12
'''

import pymysql

connect_info = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "db": "mysqlstu",
    "password": "123456"
}

connection = pymysql.connect(host=connect_info["host"],
                             user=connect_info["user"],
                             password=connect_info["password"],
                             db=connect_info["db"],
                             )

try:
    # 在数据表users插入一行数据
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('2528566339@qq.com', 'weew12'))
        connection.commit()

    # 查询插入的数据
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE `email`=%s"
        cursor.execute(sql, '2528566339@qq.com')
        res = cursor.fetchall()
        print(res)
finally:
    connection.close()
