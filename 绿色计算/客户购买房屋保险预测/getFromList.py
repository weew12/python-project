"""
    实现随机梯度下降算法时实现的一个小算法
    用于从一个列表中随机区元素 取完为止
"""

from random import sample
import time

lis = [i for i in range(1800)]
start = time.time()
while len(lis):
    item = sample(lis, 1)
    dele = item.pop()
    print(dele)
    if len(lis):
        lis.remove(dele)
end = time.time()
print("spend=", end - start)