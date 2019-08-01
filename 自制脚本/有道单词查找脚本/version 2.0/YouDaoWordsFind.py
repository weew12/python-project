# -*- coding:utf-8 -*-
'''
    Created on: 2019-08-01
    description: 借助浏览器驱动 代替手工快速查找单词
                 由于有一堆单词 但是没有翻译 所以通过
                 爬虫方式获取单词的翻译列表 

                 本程序在上次的单词查找脚本基础上进行更改

                 使用说明：createWordsList() 的path为单词文件 （.txt） 所在目录
                           find_word()用于查找并生成含有解释的单词文件 后缀在原有文件的基础上添加.txt
                 优化： 无。。。
                 查找：可以自行添加代理防止被锁ip
    @auther: weew12
'''
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import re
import os


def createWordsList():
    # 听力音频 单词文件
    path = r"C:\Users\ASUS\Downloads\六级词汇周计划\DCZB192音频"
    allFile = os.listdir(path)

    wordsFile = allFile[::2]
    wordsFile.remove(allFile[-1])

    for i in wordsFile:
        getWordsList = []
        with open(os.path.join(path, i), 'r') as file:
            content = file.readlines()
            pattern = re.compile('\[.*\](.*)')
            for j in content:
                res = pattern.findall(j)
                getWordsList.append(res.pop())
            getWordsList.remove(getWordsList[0])
        with open(os.path.join(path, i.strip(".lrc"))+'.txt', 'w') as file:
            for i in getWordsList[:-2]:
                file.write(i+'\n')
            file.write(getWordsList[-2])
            file.write(getWordsList[-1])

# createWordsList()


def find_word():
    path = r"C:\Users\ASUS\Downloads\六级词汇周计划\DCZB192音频"
    allFile = os.listdir(path)
    wordsFile = allFile[2::3]

    for i in wordsFile:
        newpath = os.path.join(path, i)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument(
        #     "--proxy-server=http://124.205.155.153:9090")
        driver = webdriver.Chrome(
            "chromedriver.exe", chrome_options=chrome_options)
        wordlist = []
        print(newpath)
        with open(newpath, 'r') as read:
            wordlist.append(read.readlines())
        for word in wordlist.pop():
            # try:
            driver.get('http://dict.youdao.com/w/divorce/#keyfrom=dict2.top')
            driver.find_element_by_xpath(
                "//input[@type='text']").send_keys(word.strip('\n'))
            driver.find_element_by_xpath("//input[@type='submit']").click()
            result = driver.find_element_by_xpath(
                "//div[@class='trans-container']").text
            print(result)
            with open(newpath+'.txt', 'a') as file:
                file.write(word)
                file.write(result)
                file.write('\n\n')
            # except:
                # print(word)
                # print("出错")

        driver.quit()


find_word()
