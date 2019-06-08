# -*- coding: utf-8 -*-

'''
新闻网新闻提取
'''


from selenium import webdriver
import json
import time

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument(
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36")

# chrome_info = "chrome_options=chrome_options,executable_path=r'G:\python 资源\Chrome浏览器驱动（webdriver）\chromedriver.exe'"

wd = webdriver.Chrome(executable_path='/xiaodengz/chrome/chromedriver', chrome_options=options)

try:
    wd.get("http://www.chinanews.com/")
except Exception as error:
    print(error)
    wd.quit()

# 新闻文章【大标题】
part_one_info = {}

try:
    part_one_title = wd.find_elements_by_xpath(
        "//div[contains(@class,'new_con_border_b')]"
        "//div[contains(@class,'xwzxdd-dbt')]//h1//a")
except Exception as error:
    print(error)
    pass

for item in part_one_title:
    # 首页获取标题与文章url
    title = item.text
    page_url = item.get_attribute('href')
    part_one_info[title] = {page_url: ''}

for key, url in part_one_info.items():
    url = list(url.keys())[0]

    # 获取页面内容
    try:
        wd.get(url)
        cont = wd.find_element_by_xpath("//div[contains(@class,'left_zw')]").text
    except Exception as error:
        print(error)
        pass

    print(cont)
    # 添加页面内容
    part_one_info[key][url] = cont

    # 返回上一页
    wd.back()

# =======================
# =======================

# 新闻文章【小标题】
part_two_info = {}

try:
    part_two_title = wd.find_elements_by_xpath(
        "//div[contains(@class,'new_con_border_b')]"
        "//div[contains(@class,'xwzxdd-xbt')]//div//a")
except Exception as error:
    print(error)
    pass

for item in part_two_title:
    # 首页获取标题与文章url
    title = item.text
    page_url = item.get_attribute('href')
    part_two_info[title] = {page_url: ''}

for key, url in part_two_info.items():
    url = list(url.keys())[0]

    # 获取页面内容
    try:
        wd.get(url)
        cont = wd.find_element_by_xpath("//div[contains(@class,'left_zw')]").text
    except Exception as error:
        print(error)
        pass

    # 添加页面内容
    part_two_info[key][url] = cont

    # 返回上一页
    wd.back()

# 合并大小标题的数据
part_all_info = part_one_info.copy()
part_all_info.update(part_two_info)

# 关闭
wd.quit()

try:
    with open(r'/xiaodengz/news/' + time.asctime(time.localtime(time.time())).replace(':', '_') + '.json',
              'w') as file_in:
        json.dump(part_all_info, file_in, ensure_ascii=False)
        print('生成json文件保存数据成功！')
except IOError as error:
    print(error)
    print("转存文件错误")

