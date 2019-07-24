# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-24
    description: 
    @auther: weew12
'''
import requests
import json
import os

# infoApi = "https://cuijiahua.com/wallpaper/api.php?cid=360new&start=30&count=6000"

class Getinfo(object):
    def __init__(self):
        self.infoApi = "https://cuijiahua.com/wallpaper/api.php?cid=360new&start=30&count=6000"
    
    def getApiInfo(self):
        response = requests.get(self.infoApi)
        if not response.status_code == 200:
            print("请求出错")
            return
        data = response.content
        return data
    
    @staticmethod
    def getAllDataToFile():
        allData = getApiInfo()
        path = input('请输入指定文件存储的路径:')
        try:
            with open(path+'/PicData.json', 'w') as file:
                json.dump(allData, file, ensure_ascii=False)
            print('保存成功')   
        except IOError as err:
            print(err)
    
    '''get diffrent pixel pictures'''
    def getIMG(self):
        data = json.loads(self.getApiInfo())
        options = [
            'img_1600_900',
            'img_1440_900',
            'img_1366_768',
            'img_1280_800',
            'img_1280_1024',
            'img_1024_768',
        ]
        info = '有六种格式的图片，请选择保存到文件的格式:\n'+\
            '1.'+options[0]+'\n'+\
            '2.'+options[1]+'\n'+\
            '3.'+options[2]+'\n'+\
            '4.'+options[3]+'\n'+\
            '5.'+options[4]+'\n'+\
            '6.'+options[5]+'\n'+\
            '请输入选项数字:'
        select = int(input(info))
        print("你选择了 {} 格式".format(options[select-1]))

        info = str([data['data'][i][options[select-1]] for i in range(len(data['data']))])
        # print(info)
        try:
            path = input('请输入指定文件存储的路径:')
            with open(path+'\\'+options[select-1] + '.json', 'w') as file:
                json.dump(info, file, ensure_ascii=False)
            print('保存成功')
        except IOError as err:
            print(err)

# test 
# test = Getinfo()
# test.getIMG()
