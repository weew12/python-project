# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-25
    description: module1
    @auther: weew12
'''



"""
    单下划线
"""
class Test:
    def __init__(self):
        self.foo = 12
        self._bar = 13

# t = Test()
# print(t.foo)
# print(t._bar)
# 输出
# 12
# 13

"""
    单下划线方法
"""
def external():
    print('external')

def _internal():
    print('internal')

