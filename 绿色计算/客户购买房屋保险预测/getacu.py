
"""
    测试文件 用于对比预测文件与标准文件的出错率
"""
import numpy as np
dataAcu = np.loadtxt(
    "G:\python 资源\python project\绿色计算\客户购买房屋保险预测\input\\acu.csv", delimiter=",")

dataPre = np.loadtxt(
    "G:\python 资源\python project\绿色计算\客户购买房屋保险预测\input\\prediction.csv", delimiter=",")
dataLen = len(dataAcu)
error = 0
for i, j in zip(dataAcu, dataPre):
    if not i == j:
        error += 1

errorRate = float(error / dataLen)
print("errorRate:", errorRate)
