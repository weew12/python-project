'''
    基于difflib+BFS对两个目录以及文件做对比
'''
import os
from queue import Queue
import difflib
import time

baseDir = os.path.dirname(__file__)

# source directory
# COMPARE_DIR_PATH = os.path.join("", "ElasticSchedulerCopy")
COMPARE_DIR_PATH = os.path.join("", "sp-ant")
# to compare directory
SOURCE_DIR_PATH = os.path.join("", "storm-2.1.0")

def strAnsiControl(sCtrl, content, eCtrl="\033[0m"):
    '''
        ansi控制字符输出的样式
        @param: sCtrl 设置ansi样式
        @param: content 输出字符的内容
        @param: eCtrl 重置 默认重置所有\033[0m
        @return: 拼接过后的字符串
    '''
    result = sCtrl + content + eCtrl
    # print(result)
    return result

def directoryBFS(fileNode, level = 1, maxLevel = None, resStr = [], format = False):
    '''
        BFS遍历目录文件
        @param: PathLike fileNode 需要遍历的文件节点绝对路径
        @param: int level 当前层级
        @param: int maxLevel 最大遍历层次 超过不再遍历/None 则表示不限制层次
        @param: List 遍历的结果
        @param: format 是否格式化
        @return: None
    '''
    # 超过maxLevel不再遍历
    if maxLevel:
        if level > maxLevel:
            return
    # 实际的操作
    # TODO
    # 从路径中去除根目录名字
    fileNodePath = "\\".join(str(fileNode).split("\\")[1:])
    if os.path.isfile(fileNode):
        if format:
            resStr.append("|" + " " * level + fileNodePath)
        else:
            resStr.append(fileNodePath)
        # print(strAnsiControl(sCtrl="\033[30m", content=resStr))
        # append2file(resStr, os.path.join(baseDir, OUT_TXT))
        return
    
    if format:
        resStr.append("|" + "-" * level + fileNodePath)
    else:
        resStr.append(fileNodePath)
        
    # print(strAnsiControl("\033[33m", content=resStr))
    # append2file(resStr, os.path.join(baseDir, OUT_TXT))
    
    fileNodeQueue = Queue()
    for fileNodeItem in os.listdir(fileNode):
        fileNodePath = os.path.join(fileNode, fileNodeItem)
        fileNodeQueue.put(fileNodePath)

    while not fileNodeQueue.empty():
        nextLevelFileNode = fileNodeQueue.get()
        directoryBFS(nextLevelFileNode, level + 1, maxLevel, resStr=resStr)
import chardet

def fileContentDiff(file1, file2, saveFile):
    '''
        对比文件内容，不同的话将difflib的对比结果输出到html
        @param: file1 对比文件1 全路径
        @param: file2 对比文件2 全路径
        @param: saveFile 保存到的html文件 全路径
    '''
    T1 = time.time()
    
    with open(file1, 'rb') as f:
        raw_data = f.read()
        
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
    # print(encoding, " ", confidence)
    
    file1 = open(file1, 'r', encoding='{}'.format('utf-8' if confidence < 0.7 else encoding))
    content1 = file1.readlines()
    file1.close()

    file2 = open(file2, 'r', encoding='{}'.format('utf-8' if confidence < 0.7 else encoding))
    content2 = file2.readlines()
    file2.close()

    if content1 != content2:
        htmlDifferObj = difflib.HtmlDiff() 
        diffRes = htmlDifferObj.make_file(content1, content2)
        with open(saveFile, 'w') as htmlFile:
            # print('diffRes', diffRes)
            htmlFile.writelines(diffRes)

    T2 = time.time()
    fileName = file1.name.ljust(100)
    runTime = "对比程序运行时间:{:.5} 毫秒".format((T2 - T1)*1000).rjust(20)
    print('\x1b[2J\x1b[H\x1b[K\n\033[32m{} {} \033[0m'.format(runTime, fileName))

def genDiffTreeFile():
    '''
        生成目录树差异文件
        输出 treeFiff.html
    '''
    res1 = []
    res2 = []
    directoryBFS(SOURCE_DIR_PATH, 1, 50, res1, format=True)
    directoryBFS(COMPARE_DIR_PATH, 1, 50, res2, format=True)
    htmlDifferObj = difflib.HtmlDiff() 
    diffRes = htmlDifferObj.make_file(res1, res2)
    with open(os.path.join(baseDir, '{}_treeDiff.html'.format(COMPARE_DIR_PATH)), 'w', encoding='utf-8') as htmlFile:
        # print('diffRes', diffRes)
        htmlFile.writelines(diffRes)

def isIgnoreFiles(file):
    '''
        是否是忽略相关后缀的文件
        @param: file 文件路径
        @return bool 存在则
    '''
    ignoreTypes = ['.jpg', '.png', '.gif', '.class', 'jar', '.gz', '.test', '.tgz', '.zip', '.ico']
    for ignoreType in ignoreTypes:
        if str(file).lower().__contains__(ignoreType):
            return True
    return False

def genDiffFile():
    '''
        对比目录树中所有的文件内容
        并输出到storm目录对应的文件夹下 结果为文件差异的html
    '''
    res1 = []
    res2 = []
    directoryBFS(SOURCE_DIR_PATH, 1, 50, res1, format=False)
    directoryBFS(COMPARE_DIR_PATH, 1, 50, res2, format=False)
    from progress.bar import Bar
    bar = Bar()
    for item in bar.iter(res1):
        if item in res2:
            souceFilePath = os.path.join(baseDir, SOURCE_DIR_PATH, item)
            targetFilePath = os.path.join(baseDir, COMPARE_DIR_PATH, item)
            # 跳过多媒体文件/字节码文/jar包/gz/.test/tgz/zip
            if isIgnoreFiles(souceFilePath):
                    continue
            if os.path.exists(souceFilePath) and os.path.exists(targetFilePath)\
                and os.path.isfile(souceFilePath) and os.path.isfile(targetFilePath):
                # fileExt = os.path.splitext(item)[1]
                htmlFileName = str(os.path.basename(item)) + ".{}.diff.html".format(COMPARE_DIR_PATH)
                saveHtmlPath = os.path.join(COMPARE_DIR_PATH, htmlFileName)
                try:
                    fileContentDiff(souceFilePath, targetFilePath, saveHtmlPath)
                except Exception as err:
                    # pass
                    error = '\n\033[35merror ' + souceFilePath + '\033[0m'
                    print(error)
                    with open(os.path.join(baseDir, '{}_errors.log'.format(COMPARE_DIR_PATH)), '+a', encoding='utf-8') as file:
                        file.write(error + '\n')
                    
                # print("\033[33mgenerate result in :" + saveHtmlPath, '\033[0m')
    bar.finish()
    

if __name__ == "__main__":
    genDiffTreeFile()
    genDiffFile()

