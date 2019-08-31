# -*- coding:utf-8 -*-
'''
    Created on: 2019-07-25
    description: 测试下划线定义的内部方法
    @auther: weew12
'''

"""
    使用*通配符导入会忽略_func()
"""
# from module1 import *

# external()
# # 输出
# # external

# # internal()
# # 报错
# # Traceback(most recent call last):
# #   File "g:/python 资源/python project/python语法/下划线方法、属性/module2.py", line 5, in < module >
# #   internal()
# # NameError: name 'internal' is not defined

"""
    使用常规导入可以使用_func()
"""
import module1

module1._internal()
# 输出
# internal