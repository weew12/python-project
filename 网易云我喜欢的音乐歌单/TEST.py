#coding:utf-8
import re
from selenium import webdriver

class Yunmusic:
    def __init__(self):
        # 网易云我喜欢的音乐的歌单网页地址
        self.start_url = "https://music.163.com/#/playlist?id=2246180219"
        # 生成一个chrome 浏览器对象
        self.driver = webdriver.Chrome('G:\python 资源\Chrome浏览器驱动（webdriver）\chromedriver.exe')

    def get_info(self):
        # 歌单中的歌曲所在的标签的筛选
        url_list = self.driver.find_elements_by_xpath("//div[contains(@class,'ttc')]/span/a")
        name_list = self.driver.find_elements_by_xpath("//div[contains(@class,'ttc')]/span/a/b")
        # 包含id 的音乐链接
        urls =[]
        music_file_urls =[]
        for txt in url_list:
            urls.append(txt.get_attribute('href'))
            # 正则筛选拼接出音乐文件地址
            music_file_url = re.findall('\?id=(.*)',txt.get_attribute('href'))
            music_file_urls.append('http://music.163.com/song/media/outer/url?id='+music_file_url.pop()+'.mp3')
        # 歌单歌名
        names =[]
        for name in name_list:
            names.append(name.get_attribute('title'))
        # 把歌单歌曲对应的官方链接输出到文件
        with open('G:\python 资源\python project\外链下载网易云我喜欢的音乐歌单（成功）\歌单歌曲.txt','w',encoding='utf8') as file:
            for key,value,music_file_url in zip(urls,names,music_file_urls):
                    file.write(value+':\n')
                    file.write(key+'\n')
                    file.write(music_file_url + '\n')
        # 歌单输出成网页
        with open('G:\python 资源\python project\外链下载网易云我喜欢的音乐歌单（成功）\歌单歌曲.html','w',encoding='utf8') as fileht:
            fileht.write("<html>")
            fileht.write('<head><meta charset="utf-8"/>')
            fileht.write('<style type="text/css">table, td, th{border:1px solid red;}'
                         ' div {float:left;width:200px;height:150px;}</style>')
            fileht.write('</head>')
            fileht.write("<body>")
            for key,value,music_file_url in zip(urls,names,music_file_urls):
                fileht.write('<div>')
                fileht.write('<table>')

                fileht.write('<caption><b>'+value+'</b></caption>')

                fileht.write('<tr>')
                fileht.write('<th>')
                fileht.write('网易云页面')
                fileht.write('</th>')
                fileht.write('<th>')
                fileht.write('音乐文件页面')
                fileht.write('</th>')
                fileht.write('</tr>')

                fileht.write('<tr>')
                fileht.write('<td>')
                fileht.write('<a href="'+key+'">页面</a>')
                fileht.write('</td>')
                fileht.write('<td>')
                fileht.write('<a href="'+music_file_url+'">文件</a>')
                fileht.write('</td>')
                fileht.write('</tr>')

                fileht.write('</table>')
                fileht.write('</div>')
            fileht.write("</body>")
            fileht.write("</html>")
    def run(self):
        self.driver.get(self.start_url)
        # 内嵌的iframe 的 name -->g_iframe
        # Xpath定位到这个部分
        self.driver.switch_to.frame('g_iframe')
        #
        try:
            self.get_info()
            self.driver.quit()
        except:
            self.driver.quit()


if __name__ == "__main__":
    yun = Yunmusic()
    yun.run()



