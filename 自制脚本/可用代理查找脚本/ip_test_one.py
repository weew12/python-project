# -*- coding: utf-8 -*-

"""
   File Name：     ip_test_one
   Description :
   Author :        枫weew12
   date：          2019/5/15
   Change Activity:2019/5/15
"""
import requests
import down_ip

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

# proxies = {"http": "http://27.46.23.148:8888"}

ip_pool = down_ip.get_ip_pool()
success = []

for i in ip_pool:
    mid = {}
    mid["http"] = 'http://' + i
    # temp = proxies.copy()
    # temp.update(mid)
    # proxies = temp
    try:
        res = requests.get('http://httpbin.org/ip', headers=headers, proxies=mid)
        print(res.status_code)
        print(res.text)
        print(mid)
        success.append(mid)
    except Exception as err:
        print(err)
        continue

print('可用ip ', success)

compile()