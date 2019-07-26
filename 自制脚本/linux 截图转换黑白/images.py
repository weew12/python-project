# -*- coding: utf-8 -*-

"""
   File Name：     images
   Description :
   Author :        枫weew12
   date：          2019/5/18
   Change Activity:2019/5/18
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


with open(r'./答案.txt', 'r') as file_in:
       str_ = file_in.readlines()
       print(str_)

