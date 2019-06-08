# 爬取笔趣阁的小说 《伏天氏》
# -*- utf-8 -*-
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 目录主页面 地址
root_url = 'https://www.qu.la/book/2125/'


# 获取章节目录 以及章节页面链接
def get_catalogue():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(root_url)

    # 目录列表
    catalogue = {}

    # Xpath筛选
    results = driver.find_elements_by_xpath("//div[contains(@id,'list')]//dl//dd//a")
    for result in results:
        res_url = result.get_attribute('href')  # url
        res_tit = result.text   # 章节标题

        # 检测'月票' '通知' 关键字
        flag = False
        if not re.search('月票', res_tit) and not re.search('通知', res_tit):
            flag = True

        # 存入字典
        if res_url not in catalogue and flag:
            catalogue[res_tit] = res_url

    driver.close()
    # 输出章节总数
    # print(catalogue.__len__())
    return catalogue


# 下载并存储章节数据
def download(catalogue):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    count = 0   # 计数器

    for key, value in catalogue.items():
        count = count + 1
        title = key    # 章节标题
        url = value      # 章节页面
        print('title =' + title + 'url = ' + url)
        try:
            driver.get(url)
            content = driver.find_element_by_xpath("//div[contains(@id,'content')]").text
            with open('G:\python 资源\python project\小说爬取(伏天氏)\\'+str(title)+'.txt','wt', encoding='utf-8') as file:
                file.write(content)
            print('章节'+str(count)+'写入成功')
        except IOError:
            print('章节'+str(count)+'写入出错')

        # 休眠 1s
        time.sleep(1)
        driver.back()
    driver.close()


if __name__ == '__main__':
    catalogues = get_catalogue()
    download(catalogues)

