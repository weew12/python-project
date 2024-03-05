import sys
import os
from queue import Queue
import logging

'''
    @description:   获取目录的目录树(windows下，Linux下有问题)
    @use:           脚本放置到需要遍历的文件目录下
    @input:         需要遍历的文件夹绝对路径
    @output:        结果文件 res.txt
    
'''
# 日志配置
baseDir = os.path.dirname(__file__)
logFile = os.path.join(baseDir, 'treeRes.txt')
logging.basicConfig(filename=logFile, level=logging.INFO)

rootPath = input('Please input the directory that you want to generate its file tree:\n')

if not os.path.exists(rootPath):
    print('{} is not exists!'.format(rootPath))

#####################  分隔字符串  #####################
DELIMETER_PRE = '│   '
DELIMETER_END_MID = '│──'
DELIMETER_END_END = '└──'
# 限制查找的层数
BASE_LEVEL = 5
#######################################################

def levelOrderTravelsal(rootPath, level, isEndFile):
    '''
        dfs 遍历目录
        @param: rootPath 需要遍历的根目录
        @return: 遍历结果
    '''
    # 限制查找层次
    if level >= BASE_LEVEL:
        print(level)
        return
    if os.path.isdir(rootPath):
        if level < 1:
            # print(DELIMETER_PRE*level+DELIMETER_END_MID, rootPath)
            message =DELIMETER_PRE*level+DELIMETER_END_MID+rootPath
            logging.info(message)
        else:
            fileName = os.path.basename(rootPath)
            # print(DELIMETER_PRE*level+DELIMETER_END_MID, fileName)
            message = DELIMETER_PRE*level+DELIMETER_END_MID+fileName
            logging.info(message)
            
    elif os.path.isfile(rootPath):
        fileName = os.path.basename(rootPath)
        if not isEndFile:
                # print(DELIMETER_PRE*level+DELIMETER_END_MID, fileName)
                message = DELIMETER_PRE*level+DELIMETER_END_MID+fileName
                logging.info(message)
        else:
            # print(DELIMETER_PRE*level+DELIMETER_END_END, fileName)
            message = DELIMETER_PRE*level+DELIMETER_END_END+fileName
            logging.info(message)
        return
    queue = Queue()
    
    for i in os.listdir(rootPath):
        queue.put(os.path.join(rootPath, i) )
    while not queue.empty():
        filePath = queue.get()
        isEndFile = False
        if queue.qsize() == 0:
            isEndFile = True
        levelOrderTravelsal(filePath, level + 1, isEndFile)

levelOrderTravelsal(rootPath=rootPath, level=0, isEndFile=False)        
