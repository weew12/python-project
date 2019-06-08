# -*- coding:UTF-8 -*-
import requests
from selenium import webdriver
import re
from urllib import parse
import time
from selenium.webdriver.chrome.options import Options

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/70.0.3538.110 Safari/537.36"
}

rooturl = 'https://www.biqukan.com/1_1094/'


def all_page_url(rooturl):
    response = requests.get(rooturl, headers=header)
    urls = re.findall('<dd><a href ="(.*)".*/dd>', response.text)
    reurls = []
    for url in urls:
        reurls.append(parse.urljoin(rooturl, url))
    return reurls


def page_download_parser(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome("G:\python 资源\Chrome浏览器驱动（webdriver）\chromedriver.exe", chrome_options=chrome_options)
    try:
        driver.get(url)
        result_t = driver.find_element_by_tag_name('h1')
        result = driver.find_element_by_xpath("//div[contains(@id,'content')]")
        with open('G:\python 资源\python project\笔趣阁在线小说爬取\\'+result_t.text+'.txt','w') as file:
            file.write(result_t.text+'\n')
            file.write(result.text)
        # print(result.text)
    except:
        print("页面下载解析出错")
    finally:
        driver.quit()


def main():
    urls = []
    urls = all_page_url(rooturl)
    count = 1
    for url in urls[15:-3]:
        count += 1
        try:
            page_download_parser(url)
            time.sleep(0.5)
            print("第%d下载成功" % count)

        except:
            print("第%d下载出错" % count)


if __name__ == "__main__":
    main()
