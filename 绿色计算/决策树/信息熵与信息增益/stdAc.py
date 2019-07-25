# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-25
    description: 标准答案 代码
    @auther: weew12
'''

#计算熵
def calcInfoEntropy(self, label):
    label_set = set(label)
    result = 0
    for l in label_set:
        count = 0
        for j in range(len(label)):
            if label[j] == l:
                count += 1
        p = count/len(label)
        result -= p*np.log2(p)
    return result

#计算条件熵
def calcHDA(self, feature, label, index, value):
    count = 0
    sub_feature = []
    sub_label = []
    for i in range(len(feature)):
        if feature[i][index] == value:
            count += 1
            sub_feature.append(feature[i])
            sub_label.append(label[i])
    pHA = count/len(feature)
    e = self.calcInfoEntropy(sub_label)
    return pHA*e

#计算信息增益

def calcInfoGain(self, feature, label, index):
    base_e = self.calcInfoEntropy(label)
    f = np.array(feature)
    f_set = set(f[:, index])
    sum_HDA = 0
    for l in f_set:
        sum_HDA += self.calcHDA(feature, label, index, l)
    return base_e - sum_HDA
