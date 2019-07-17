"""
    题目见Mardown
    测试数据 testdata.txt
    代码: 此处代码
"""

xlist = input('please input:')
xlist = [int(i) for i in xlist]
ori = xlist[:]

# 检查是否有序(升序)
def ordered():
    now = xlist[0]
    for i in xlist[1:]:
        if i < now:
            return False
        now = i
        # print(now)
    return True
# print(ordered())

res = []
if ordered():
    res.append(xlist)
else:
    while(not ordered()):
        # 正向交换
        for pos, i in enumerate(xlist):
            if pos != len(xlist)-1:
                if xlist[pos] > xlist[pos+1]:
                    temp = xlist[pos]
                    xlist[pos] = xlist[pos+1]
                    xlist[pos+1] = temp
                if xlist not in res and not xlist == ori:
                    info = xlist[:]
                    res.append(info)
            # print(xlist)

        # 反向交换
        pos2 = len(xlist)-1
        for i in xlist[::-1]:
            if pos2 == 0:
                continue
            if xlist[pos2] < xlist[pos2-1]:
                temp = xlist[pos2]
                xlist[pos2] = xlist[pos2-1]
                xlist[pos2-1] = temp
            if xlist not in res and not xlist == ori:
                info = xlist[:]
                res.append(info)
            # print(xlist)
            pos2 -=1

# 格式化输出
for i in res:
    for j in i:
        if j != i[-1]:
            print(j, end=" ")
        else:
            print(j)

