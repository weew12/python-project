"""
    第二届绿色计算的决赛最后一题 机器学习(天气预测)
"""
import numpy as np
import pandas as pd


def MinMaxscale(train_x):  # Min-Max 缩放
    '''
        计算公式:
        xi = (xi - min)/(max - min)
    '''
    minn = train_x.min(axis=0)
    maxx = train_x.max(axis=0)
    new_train = (train_x - minn) / (maxx - minn)
    return new_train


def xdataDeal():  # 训练数据集
    dataset = pd.read_csv('input/train.csv', header=0)
    # 使用属性的均值作为填充值 对于缺失的值进行插值
    dataset = dataset.fillna(dataset.mean())

    # 使用独热编码方式对于风向属性列进行数值化编码
    index = ['WindGustDir', 'WindDir9am', 'WindDir3pm']
    string = dataset[index]
    string = string.fillna(dict(zip(string.columns, string.mode().values[0])))
    dataset[index] = string

    all_data = pd.get_dummies(dataset.iloc[:, 2:-1]).values

    y = (dataset.iloc[:, -1] == "Yes").values
    return MinMaxscale(all_data), y


def ydataDeal():  # 测试数据集

    dataset = pd.read_csv('input/test.csv', header=0)
    # 使用属性的均值作为填充值 对于缺失的值进行插值
    dataset = dataset.fillna(dataset.mean())

    # 使用独热编码方式对于风向属性列进行数值化编码
    index = ['WindGustDir', 'WindDir9am', 'WindDir3pm']
    string = dataset[index]
    string = string.fillna(dict(zip(string.columns, string.mode().values[0])))
    dataset[index] = string

    all_data = pd.get_dummies(dataset.iloc[:, 2:]).values
    return MinMaxscale(all_data)


def liner_Regression(data_x, data_y, learningRate, Loopnum):
    data_y = data_y.reshape(-1, 1)  # !!!!!
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
        #********#
        # if num % 1 == 0:
        #     print("loss {}".format(loss))
    # print(Weight, baise)
    return (Weight, baise)


def pre():
    datax, datay = xdataDeal()
    Weight, bias = liner_Regression(
        datax, datay, 0.1, 500)  # args: 输入 输出 学习率 迭代次数
    testIndex1 = np.loadtxt("input/test.csv", delimiter=",",
                            dtype=str, usecols=(0,), skiprows=1).tolist()
    testIndex2 = np.loadtxt("input/test.csv", delimiter=",",
                            dtype=str, usecols=(1,), skiprows=1).tolist()
    xdata = ydataDeal()
    ydata = []
    for i in xdata:
        mid = np.array(i).reshape(66, 1)
        res = np.dot(Weight, mid) + bias
        mid = float(res)
        mid = float(mid)
        if mid < 0:
            ydata.append(0.0)
        elif mid > 1:
            ydata.append(1.0)
        else:
            ydata.append(mid)
    # print(ydata)
    df = pd.DataFrame(
        {'Date': testIndex1, 'Location': testIndex2, 'RainTomorrow': ydata})
    df.to_csv("test_prediction.csv", index=False)


pre()
