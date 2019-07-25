# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-25
    description:  解题、测试代码
    @auther: weew12
'''

from math import log
import numpy as np

info = {
    'feature': [[0, 1], [1, 0], [1, 2], [0, 0], [1, 1]],
    'label': [0, 1, 0, 0, 1], 'index': 0
    }
    
# info = {
#     'feature': [[0, 0], [1, 0], [1, 2], [0, 0],[1, 1]],
#      'label': [0, 1, 0, 0, 0], 'index': 1
# }

feature = np.array(info['feature'])
label = np.array(info['label'])
# print(feature)
# print(np.shape(feature))
# print(label)
# print(np.shape(label))


# 计算信息熵
def calcInfoEntropy(feature, label):
    '''
    计算信息熵
    :param feature:数据集中的特征，类型为ndarray
    :param label:数据集中的标签，类型为ndarray
    :return:信息熵，类型float
    '''
    #*********** Begin ***********#
    numEntries = np.shape(feature)[0]
    numFeatures = np.shape(label)[0]
    labelCounts = {}
    for i in range(numFeatures):
        if label[i] not in labelCounts.keys():
            labelCounts[label[i]] = 0
        labelCounts[label[i]] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        # shannonEnt -= prob * log(prob, 2)
        shannonEnt -= prob * np.log2(prob)
    return shannonEnt
    #*********** End *************#


# 计算条件熵
def calcHDA(feature, label, index, value):
    '''
    计算信息熵
    :param feature:数据集中的特征，类型为ndarray
    :param label:数据集中的标签，类型为ndarray
    :param index:需要使用的特征列索引，类型为int
    :param value:index所表示的特征列中需要考察的特征值，类型为int
    :return:信息熵，类型float
    '''
    #*********** Begin ***********#
    numEntries = np.shape(feature)[0]
    numFeatures = 0
    labelCounts = {}
    for i in range(numEntries):
        if feature[i][index] == value:
            if label[i] not in labelCounts.keys():
                labelCounts[label[i]] = 0
            labelCounts[label[i]] += 1
            numFeatures += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numFeatures
        shannonEnt -= prob * np.log2(prob)
    # print("条件", shannonEnt)
    return shannonEnt
    #*********** End *************#


def calcInfoGain(feature, label, index):
    '''
    计算信息增益
    :param feature:测试用例中字典里的feature
    :param label:测试用例中字典里的label
    :param index:测试用例中字典里的index，即feature部分特征列的索引
    :return:信息增益，类型float
    '''
    #*********** Begin ***********#
    numEntries = np.shape(feature)[0]
    infoEnt = calcInfoEntropy(feature, label)
    # print("infoEnt", infoEnt)
    clsfy = {}
    for i in range(numEntries):
        if feature[i][index] not in clsfy:
            clsfy[feature[i][index]] = 0
        clsfy[feature[i][index]] += 1
    newshannonEnt = 0.0
    for key in clsfy:
        prob = float(clsfy[key])/numEntries
        midshannonEnt = calcHDA(feature, label, index, key)
        newshannonEnt += prob * midshannonEnt
    # print("clsfy", clsfy)
    # print("newshannonEnt", newshannonEnt)
    infoGain = infoEnt - newshannonEnt
    # print(infoGain)
    return infoGain
    #*********** End *************#
# calcInfoGain(feature, label, 0)
