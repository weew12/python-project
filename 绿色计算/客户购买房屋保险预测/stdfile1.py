"""
    本地用测试文件
    用于获取预测结果文件
"""
import numpy as np
import pandas as pd
from random import sample
import matplotlib.pyplot as plt
import csv


"""
    加载数据
    自定义80% 数据训练
    20%数据测试
"""


def loadTrainData():
    '''加载训练数据'''
    all_traindata = np.loadtxt(
        "G:\python 资源\python project\绿色计算\客户购买房屋保险预测\input\\a.csv", delimiter=",", skiprows=1)
    data = all_traindata[:, 5]
    maxn = max(data)
    minn = min(data)
    num = len(data)
    sumn = 0
    sumn = sum(map(lambda x: x + sumn, data))
    avrn = float(sumn / num)
    if maxn == minn and maxn == avrn:
        change = [1 for x in data]
    else:
        change = [(x-avrn)/(maxn-minn) if maxn -
                  minn != 0 else 0 for x in data]
    for pos, x in enumerate(change):
        all_traindata[pos, 5] = x/2
    x_data = all_traindata[:1401, 1:-1].tolist()
    y_data = all_traindata[:1401, -1].tolist()
    labelmat = []
    for i in y_data:
        labelmat.append(int(i))
    return x_data, labelmat


def sigmoid(num):
    """sigmoid函数"""
    if num >= 0:
        return 1.0 / (1 + np.exp(-num))
    else:
        return np.exp(num) / (1 + np.exp(num))


"""梯度上升算法"""
def stocGradAscent1(xdata, ydata, numIter=500):
    m, n = np.shape(xdata)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = [i for i in range(m)]
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.0001
            randIndex = sample(dataIndex, 1).pop()
            h = sigmoid(sum(xdata[randIndex]*weights))
            error = ydata[randIndex] - h    # 梯度
            weights = weights + alpha * error * np.array(xdata[randIndex])
            dataIndex.remove(randIndex)
    return weights


def classifyVector(inX, weights):
    """分类 1 0"""
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def testTrain(times):
    xdata, ydata = loadTrainData()
    trainWeights = stocGradAscent1(xdata, ydata, times)
    return trainWeights


def prediction(times):
    trainWeights = testTrain(times)
    errorCount = 0
    txdata, tydata = loadTestData()
    numTest = len(txdata)
    for i, j in zip(txdata, tydata):
        if int(classifyVector(i, trainWeights)) != int(j):
            errorCount += 1
    print("err:", errorCount)
    print("num:", numTest)
    errorRate = float(errorCount)/numTest
    print("{} times test the error rate is {}".format(times, errorRate))


def loadData():
    '''
    加载预测数据

    '''
    all_traindata = np.loadtxt(
        "G:\python 资源\python project\绿色计算\客户购买房屋保险预测\input\\b.csv", delimiter=",", skiprows=1)
    data = all_traindata[:, 5]
    maxn = max(data)
    minn = min(data)
    num = len(data)
    sumn = 0
    sumn = sum(map(lambda x: x + sumn, data))
    avrn = float(sumn / num)
    if maxn == minn and maxn == avrn:
        change = [1 for x in data]
    else:
        change = [(x-avrn)/(maxn-minn) if maxn -
                  minn != 0 else 0 for x in data]
    for pos, x in enumerate(change):
        all_traindata[pos, 5] = x/2
    x_data = all_traindata[:, 1:].tolist()
    return x_data


def getRes(times):
    xdata = loadData()
    yres = []
    trainWeights = testTrain(times)
    for i in xdata:
        yres.append(int(classifyVector(i, trainWeights)))
    # print(yres)
    test_path = "G:\python 资源\python project\绿色计算\客户购买房屋保险预测\input\\b.csv"
    address = pd.read_csv(test_path, usecols=[0])
    new_address = address.values.tolist()
    new_address = [str(n) for a in new_address for n in a]
    # print(len(yres))
    # np.savetxt('prediction.csv', np.array(yres),
    #            delimiter=',', newline="\n", fmt="%d", )
    df = pd.DataFrame({'ID': new_address, 'TARGET': yres})
    df.to_csv("test_prediction.csv", index=False)

getRes(200)
