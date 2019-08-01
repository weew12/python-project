# -*- coding: utf-8 -*-

"""
   File Name：     down_ip
   Description :
   Author :        枫weew12
   date：          2019/5/15
   Change Activity:2019/5/15
"""

import requests
import re

patter_1 = re.compile('<td data-title="IP">(.*)</td>')
patter_2 = re.compile('<td data-title="PORT">(.*)</td>')


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}


def get_ip_pool():
    res = requests.get('https://www.kuaidaili.com/free/intr/6/', headers=headers)

    # print(res.text)

    ress = patter_1.findall(res.text)
    ress2 = patter_2.findall(res.text)
    ip_pool = [item[0] + ':' + item[1] for item in zip(ress, ress2)]
    ip_pool = set(ip_pool)

    return ip_pool

