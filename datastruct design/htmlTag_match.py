# -*- coding: utf-8 -*-
from __future__ import print_function
import re
import os


# 网页文档
htmltext = ''

# 需要剔除的特殊单标签
special = ['<meta>','<link>','<hr>','<input>','<br>','<img>','<pre>']

# 筛选结果
res = []
# 未处理标签
temp = []

# 栈的实现
class Stack(object):

    # 初始化
    def __init__(self):
        self.stack = []

    # 空栈
    def isEmpty(self):
        return self.stack == []

    # 入栈
    def push(self, item):
        self.stack.append(item)

    # # 出栈
    # def pop(self):
    #     if self.isEmpty():
    #         raise IndexError, 'empty'
    #     return self.stack.pop()

    # 栈的长度
    def size(self):
        return len(self.stack)


# 前标签栈
s1 = Stack()
# 后标签栈
s2 = Stack()


# 主界面
def main_menu():
    # 菜单界面
    print('*******************************************************')
    print('|---------------------------------------------------- |')
    print('|--------------简易HTML文档标记匹配工具-------------- |')
    print('|--------------------1.读取文本内容------------------ |')
    print('|--------------------2.验证文档标记------------------ |')
    print('|--------------------0.退出系统---------------------- |')
    print('|---------------------------------------------------- |')
    print('*******************************************************')

# 读取文本
def input_menu():
    doc_in()
    #   界面
    print('*---------------------------------------------------- *')
    print('*读取成功！                                       *')
    print('*---------------------------------------------------- *')
    print('*内容：--------------------------------------------- *')
    print(s1.stack + s2.stack)
    print('*---------------------------------------------------- *')

    # 选项
    n = input('请输入选项:(1.退出 2.返回主界面)')
    try:
        while(True):
            if n == 1:
                print('退出系统\n')
                os.exit(0)
            elif n == 2:
                main_menu()
                break
            else:
                n = input('输入有误，重新输入:')
    except:
        pass
    print('\n' * 10)

# 文档读入
def doc_in():
    global htmltext

    #   网页文档的存储文件 :C:\\Users\\ASUS\\Desktop\\111.txt
    with open('C:\\Users\\ASUS\\Desktop\\111.txt', 'r') as fileopen:
        htmltext += fileopen.read()
        print('读取成功')
    read()

# 验证_界面
def match_menu():

    opt()
    print("*---------------------------------------------------- *")

    if len(htmltext) == 0:
        print('未输入文档')
    else:
        print('验证结果:')
    if len(res) == 0:
        print('文档规范')
    else:
        print('文档出现问题,问题标签如下:')
        print(res)
    print('*---------------------------------------------------- *')

    # 选项
    n = input('请输入选项:(1.退出 2.返回主界面)')
    try:
        while (True):
            if n == 1:
                print('退出系统\n')
                os.exit(0)
            elif n == 2:
                main_menu()
                break
            else:
                n = input('输入有误，重新输入:')
    except:
        pass
    print('\n' * 10)

# 读取入栈 前标签栈s1 后标签栈s2
def read():

    # 使用全局声明的栈存取便签对
    global s1, s2

    # 正则筛选所有便签
    result = re.findall('</?[^><]+>', htmltext)

    # 存储剔除空格的结果
    ress = []
    for i in result:
        # 剔除所有空格
        ress.append(i.replace('\x00',''))

    with open('C:\\Users\\ASUS\\Desktop\\777.txt', 'a') as ee:
        for i in ress:
            # 剔除便签的内嵌样式
            st = i.replace('\x00', '').split()
            mid = ''
            if '>' in st[0]:
                str = st.pop()
                if '!' not in str:
                    ee.write(str)
                    mid = str
            else:
                str = st[0] + '>'
                if '!' not in str:
                    ee.write(str)
                    mid = str
            if '/' in mid:
                s2.push(mid)
            else:
                s1.push(mid)



# 标签分堆结果写入文件
def write():
    read()
    # 此处使用全局变量
    global s1, s2

    # 前标签
    with open('C:\\Users\\ASUS\\Desktop\\s1.txt', 'w') as s11:
        for i in s1.stack:
            s11.write(i+'\n')

    # 后标签
    with open('C:\\Users\\ASUS\\Desktop\\s2.txt', 'w') as s22:
        for i in s2.stack:
            s22.write(i+'\n')


# 验证操作
def opt():

    global res
    write()
    t1 = s1.stack
    t2 = s2.stack

    for i in range(0,len(t1)):
        if t1[i] in special:
            t1[i] = ''

    for i in range(0,len(t2)):
        if t2[i] in special:
            t2[i] = ''

    while '' in t1:
        t1.remove('')
    while '' in t2:
        t2.remove('')

    for i in range(0,len(t1)):
        for j in range(0,len(t2)):
            if t2[j].replace('/','') == t1[i]:
                t1[i] = ''
                t2[j] = ''

    while '' in t1:
        t1.remove('')
    while '' in t2:
        t2.remove('')

    # 最终结果
    result = []
    for i in t1:
        result.append(i)
    for i in t2:
        result.append(i)

    print('结果-----》(问题标签对:)')
    print(result)

    # 结果赋值给去全局结果
    res = result
    return t1,t2


# 验证界面
def match_menu():


    r1,r2 = opt()
    print('*---------------------------------------------------- *')
    print('前标签筛选结果:')

    if len(r1) == 0:
        print('全部筛出')
    else:
        print(r1)

    print('*---------------------------------------------------- *')
    print('后标签筛选结果:')

    if len(r2) == 0:
        print('全部筛出')
    else:
        print(r2)

    print('*---------------------------------------------------- *')
    print('\n' * 10)

if __name__ == '__main__':
    main_menu()
    while True:
        key = input("请输入你要选择的操作：")
        if key == 1:
            input_menu()
        elif key == 2:
            match_menu()
        elif str(key) == 'g':
            os._exit(0)
