'''
    @author: weew12
    @date: 2024/03/14
    @description:
        比较两个目录的不同文件。。。
'''
import os
import sys
import logging
from queue import Queue
from collections import OrderedDict
from enum import Enum

baseDir = os.path.dirname(__name__)

# source directory
SOURCE_DIR_PATH = r"F:\技术\资料\【BOOK-C++c】Linux高级程序设计PPT"
# to compare directory
COMPARE_DIR_PATH = r"F:\技术\拓展阅读"
# result save path
RES_2_SAVE = "result.txt"
RES_2_SAVE = os.path.join(baseDir, RES_2_SAVE)
# 存储对比结果
ORDERED_RES_DICT = OrderedDict()


def addSuffix2FileOrDir(
        filePath,
        dirPrefix = "[",
        dirSuffix = "]",
        filePrefix = "<",
        fileSuffix = ">"
    ):
    '''
        给路径字符串添加指定的前后缀
        @param: filePath 文件路径
        @param: dirPrefix 指定目录添加的前缀字符串
        @param: dirSuffix 指定目录添加的后缀字符串
        @param: filePrefix 指定文件添加的前缀字符串
        @param: fileSuffix 指定文件添加的后缀字符串
        @return str
    '''
    if os.path.isfile(filePath):
        return filePrefix + os.path.basename(filePath) + fileSuffix
    elif os.path.isdir(filePath):
        return dirPrefix + filePath + dirSuffix

def appendRes2Dict(level, fileNode, resDict):
    '''
        把对比的结果写入resDict
        @param: level 遍历层级
        @param: fileNode 文件对象
        @param: resDict 存储结果的dict
        @return: None
    '''
    # print("run ", level, " ", fileNode)
    if not resDict.keys().__contains__(level):
        resDict[level] = []
    resDict[level].append(fileNode)

def appendRes2DictAndRemoveDuplicates(level, fileNode, resDict):
    '''
        把对比的结果写入resDict 并对同层次的文件做去重
        @param: level 遍历层级
        @param: fileNode 文件对象
        @param: resDict 存储结果的dict
        @return: None
    '''
    if not resDict.keys().__contains__(level):
        resDict[level] = []
    # 去除同level的重名文件
    for index, file in enumerate(resDict[level]):
        if os.path.basename(file) == os.path.basename(fileNode):
            del resDict[level][index]
            return
    
    # 没有重复的文件的话 就把当前的文件进去
    resDict[level].append(fileNode)

def pathGetPublicPrefix(path1, path2):
    '''
        获取两个路径的公共前缀
        @param: path1 PathLike 文件路径
        @param: path2 PathLike 文件路径
        @return 公共路径 str
    '''
    return os.path.commonprefix([path1, path2]) or ""

class MODE(Enum):
    '''
        区分当前遍历的是source 还是target
        @param: SOURCE  遍历source
        @param: TARGET  遍历target
    '''
    SOURCE = 1
    TARGET = 2

def directoryBFS(fileNode, level = 1, maxLevel = None, mode = None):
    '''
        BFS遍历目录文件
        @param: PathLike fileNode 需要遍历的文件节点绝对路径
        @param: int level 当前层级
        @param: int maxLevel 最大遍历层次 超过不再遍历/None 则表示不限制层次
        @param: function 调用的函数
        @param: mode 遍历的目标 SOURCE | TARGET
        @return: None
    '''
    if mode != MODE.SOURCE and mode != MODE.TARGET:
        return
    # 超过maxLevel不再遍历
    if maxLevel:
        if level > maxLevel:
            return
    # 实际的操作
    # print("|" + "-" * level if os.path.isdir(fileNode) else " " + "-" * level, os.path.basename(fileNode))
    if mode == MODE.SOURCE:
        appendRes2Dict(level=level, fileNode=fileNode, resDict=ORDERED_RES_DICT)
    else:
        appendRes2DictAndRemoveDuplicates(level=level, fileNode=fileNode, resDict=ORDERED_RES_DICT)

    if os.path.isfile(fileNode):
        return
    
    fileNodeQueue = Queue()
    for fileNodeItem in os.listdir(fileNode):
        fileNodePath = os.path.join(fileNode, fileNodeItem) 
        fileNodeQueue.put(fileNodePath)
    
    while not fileNodeQueue.empty():
        nextLevelFileNode = fileNodeQueue.get()
        directoryBFS(nextLevelFileNode, level + 1, maxLevel, mode)

def processAndSaveDictData(dictData, soucePath, comparePath, savePath):
    '''
        处理并保存得到的dict结果
        @param: dictData 遍历对比后获得的dict结果
        @param: soucePath 源目录路径
        @param: comparePath 要对比目录的路径
        @param: savePath 要保存结果文件的路径
    '''
    # 按level排序
    sorted(dictData)
    # 获取公共的目录前缀  后面去除掉 保存路径到文件时好查看一点
    publicPrefix = pathGetPublicPrefix(soucePath, comparePath)
    # print(publicPrefix)
    file = open(savePath, 'wb')
    for items in zip(dictData.keys(), dictData.values()):
        level = items[0]
        files = items[1]
        for fileItem in files:
            fileName = "{} {} {}".format("|" if os.path.isdir(fileItem) else "",
                                         "--" * level + str(fileItem).replace(publicPrefix, ""),
                                         "\n")
            file.write(
                bytes(
                    fileName,
                    encoding='utf-8'
                )
            )
    file.close()
    
        

if __name__ == "__main__":
    directoryBFS(SOURCE_DIR_PATH, 1, 50, mode=MODE.SOURCE)
    directoryBFS(COMPARE_DIR_PATH, 1, 50, mode=MODE.TARGET)
    processAndSaveDictData(ORDERED_RES_DICT, SOURCE_DIR_PATH, COMPARE_DIR_PATH, RES_2_SAVE)
