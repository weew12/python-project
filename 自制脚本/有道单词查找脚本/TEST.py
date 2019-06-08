# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_word():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
    wordlist = []
    with open('C:\\Users\\ASUS\\Desktop\\11.txt', 'r') as read:
        wordlist.append(read.readlines())
    for word in wordlist.pop():
        # try:
        driver.get('http://dict.youdao.com/w/divorce/#keyfrom=dict2.top')
        driver.find_element_by_xpath("//input[@type='text']").send_keys(word)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        result = driver.find_element_by_xpath("//div[@class='trans-container']").text
        print(result)
        with open('C:\\Users\\ASUS\\Desktop\\22.txt', 'a') as file:
            file.write(word)
            file.write(result)
            file.write('\n\n')
        # except:
        # print(word)
        print("出错")

    driver.quit()


if __name__ == '__main__':
    find_word()
