"""
    此处为通过代码
    预测准确率大约 75%左右 有波动
    预测至少最低不会低于 65%
"""

from random import sample
import pandas as pd
import numpy as np

#*********************数据说明***********************
# 训练数据：src/step1/input/train.csv
# 测试数据：src/step1/input/test.csv
# 结果文件：src/output/test_prediction.csv
#***************************************************


def getPrediction():
    ########## Begin ##########
    train_path = "src/step1/input/train.csv"
    test_path = "src/step1/input/test.csv"

    def loadTrainData():
        '''加载训练数据'''
        all_traindata = np.loadtxt(train_path, delimiter=",", skiprows=1)
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
        x_data = all_traindata[:, 1:-1].tolist()
        y_data = all_traindata[:, -1].tolist()
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
                alpha = 4 / (1.0 + j + i) + 0.0005
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

    def loadData():
        '''
        加载预测数据

        '''
        all_traindata = np.loadtxt(test_path, delimiter=",", skiprows=1)
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
        address = pd.read_csv(test_path, usecols=[0])
        new_address = address.values.tolist()
        new_address = [str(n) for a in new_address for n in a]
        df = pd.DataFrame({'ID': new_address, 'TARGET': yres})
        df.to_csv("src/output/test_prediction.csv", index=False)

    getRes(200)

    ########## End ##########
