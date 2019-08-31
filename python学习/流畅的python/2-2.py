# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-30
    description: 
    @auther: weew12
'''

# #常用写法
# symbols = '$%&*'
# asciiCode = []
# for symbol in symbols:
#     asciiCode.append(ord(symbol))
# print(asciiCode)

# # 推导式写法
# symbols = '$%&*'
# asciiCode = [ord(x) for x in symbols]
# print(asciiCode)

# # filter map
# '''
#     filter:提供条件进行滤
#     map: 提供方法进行映射
# '''
# symbols = '$%&*'
# asciiCode = [ord(x) for x in symbols if ord(x) < 127]
# asciiCode1 = list(filter(lambda c: c < 127, map(ord, symbols)))
# print(asciiCode)
# print(asciiCode1)

# 生成器
colors = ['black', 'blue']
sizes = ['S', 'M', 'L']
tshirt = ('{} {}'.format(color, size) for color in colors
          for size in sizes)
print(tshirt)
# 输出<generator object <genexpr> at 0x0000021A03974138>

tshirt = ['{} {}'.format(color, size) for color in colors
          for size in sizes]
print(tshirt)
# 输出['black S', 'black M', 'black L', 'blue S', 'blue M', 'blue L']
