import numpy as np
import pandas as pd


# 获取训练数据
def xdataDeal():
    traindata = np.loadtxt("./input/train.csv",
                           delimiter=',', skiprows=1, dtype=str)
    h, l = np.shape(traindata)
    for i in range(1, l-3):
        tag = {}
        midtag = set(traindata[:, i])
        for j in midtag:
            if j not in tag.keys():
                tag[j] = 0

        for pos, j in enumerate(tag):
            tag[j] = int(pos)+1

        for pos, j in enumerate(traindata[:, i]):
            value = tag[j]
            traindata[pos, i] = float(value)

    a = traindata.tolist()
    newdata = []
    for i in a:
        mid = []
        for j in i:
            mid.append(float(j))
        newdata.append(mid)
    data = np.array(newdata)
    return data


# 获取测试数据
def ydataDeal():
    traindata = np.loadtxt(
        "./input/test.csv", delimiter=',', skiprows=1, dtype=str)
    h, l = np.shape(traindata)
    for i in range(1, l-2):
        tag = {}
        midtag = set(traindata[:, i])
        for j in midtag:
            if j not in tag.keys():
                tag[j] = 0

        for pos, j in enumerate(tag):
            tag[j] = int(pos)+1

        for pos, j in enumerate(traindata[:, i]):
            value = tag[j]
            traindata[pos, i] = float(value)

    a = traindata.tolist()
    newdata = []
    for i in a:
        mid = []
        for j in i:
            mid.append(float(j))
        newdata.append(mid)
    data = np.array(newdata)
    return data


# 线性回归
def liner_Regression(data_x, data_y, learningRate, Loopnum):
    data_y = data_y.reshape(np.shape(data_y)[0], 1)  # !!!!!
    Weight = np.ones(shape=(1, data_x.shape[1]))
    baise = np.array([[1]])

    # 梯度下降
    """
        公式：
            预测值 = datax * w + bias
            损失 = 【(实际值 - 预测值)*(实际值 - 预测值)】/(测试用例数)
            w梯度 = (-2/(测试用例数)) * (实际值 - 预测值)(转置) * datax
            b梯度 = (-2) * (实际值 - 预测值) / (测试用例数)
            更新：
            w = w - 学习率*旧的w
            b = b - 学习率*旧的b
    """
    for num in range(Loopnum):
        predict = np.dot(data_x, Weight.T) + baise
        loss = np.dot((data_y-predict).T, data_y-predict)/data_y.shape[0]
        w_gradient = -(2/data_x.shape[0])*np.dot((data_y-predict).T, data_x)
        baise_gradient = -2 * \
            np.dot((data_y-predict).T,
                   np.ones(shape=[data_x.shape[0], 1]))/data_x.shape[0]
        Weight = Weight-learningRate*w_gradient
        baise = baise-learningRate*baise_gradient
    return (Weight, baise)


def pre():
    data = xdataDeal()
    datax = data[:, 1:-1]
    datay = data[:, -1]
    Weight, bias = liner_Regression(datax, datay, 0.0001, 500000)
    testIndex = np.loadtxt("./input/test.csv", delimiter=",",
                           dtype=str, usecols=(0,), skiprows=1).tolist()
    xdata = ydataDeal()[:, 1:]
    ydata = []
    for i in xdata:
        mid = np.array(i).reshape(7, 1)
        res = np.dot(Weight, mid) + bias
        mid = int(res)
        ydata.append(mid)
    df = pd.DataFrame({'id': testIndex, 'math score': ydata})
    df.to_csv("./output/test_prediction.csv", index=False)


pre()
