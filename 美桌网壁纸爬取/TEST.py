import re
import requests
import time
from multiprocessing import Pool
from lxml import etree
import os
import uuid

# 第一个主页面地址
rooturl = 'http://www.win4000.com/zt/huyan_'

# http://www.win4000.com/zt/fengjing.html

# 模拟浏览器请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.110 Safari/537.36"
}

count = 0
# 图片集url
def graph_set(rooturl):
    set = []
    title = []
    results = requests.get(rooturl, headers=header)
    text = results.text
    res = re.findall('.*href="(.*)" alt="',text)
    selector = etree.HTML(text)
    tt = selector.xpath('//div[contains(@class,"tab_tj")]//li//p')
    for url in res:
        set.append(url)
    for tit in tt[:24]:
        title.append(tit.text)
    return title,set


# 图片页面解析原图集合
def parser(tup):
    response = requests.get(tup[0],headers=header)
    text = response.text
    originset = re.findall('href="(.*)" class=.*查看原图',text)
    time.sleep(1)
    oringin(originset.pop(),tup[1])

# 图集原图集合
def oringin(page,name):
    print(name+'正在爬取')
    dir = 'G:\python 资源\python project\美桌网壁纸爬取\护眼图片\\'
    oringin = []
    response = requests.get(page,headers=header)
    res = re.findall('li.*href="(.*)".*><img.*/li',response.text)
    for url in res:
        result = re.findall('(.*)" target', url)
        oringin.append(result)
    num = len(oringin)
    for url in oringin:
        count = uuid.uuid1()
        res = requests.get(url.pop(), headers=header)
        with open(dir+str(count)+'.jpg','wb') as file:
            file.write(res.content)
        # time.sleep(1)

    # print(oringin)


def main(rooturl):
    pagename,pageset = graph_set(rooturl)
    # for url,name in dict(zip(pageset,pagename)).items():
    #     orin = parser(url)
    #     oringin(orin,name)
        # print(url,name)
    p = Pool()
    p.map(parser,zip(pageset,pagename))



if __name__ == '__main__':
    for i in range(1,6):
        pageurl = rooturl + str(i) + '.html'
        print(str(i)+'页面开始爬取......')
        main(pageurl)


