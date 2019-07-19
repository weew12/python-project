from random import sample
import time
"""
    从列表中随机取出一个元素
    知道所有元素都取完
"""
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