def solver(s, p, ops):
    # ********** Begin ********** #
    def I(s, p, str):#插入
        newS = s[:p] +  str + s[p:]
        s = newS
        p = p + len(str)
        return s,p

    def B(s, p, n):#退格
        if p == 0:
            return s,p
        elif p <= n:
            return s[p:], 0
        else:
            newS = s[:p-n] + s[p:]
            newP = p-n
            return newS, newP

    def D(s, p, n):#删除
        allS = len(s)
        if n >= allS - p:
            newS = s[:p]
            newP = len(newS)
            return newS, newP
        else:
            newS = s[:p] + s[p+n:]
            newP = p
            return newS, newP

    def L(s, p, n):#左移
        if n >= p:
            newP = 0
            newS = s
            return newS, newP
        else:
            newP = p-n
            newS = s
            return newS, newP

    def R(s, p, n):#右移
        allS = len(s)
        if p+n >= allS:
            newP = allS
            newS = s
            return newS, newP
        else:
            newP = p+n
            newS = s
            return newS, newP

    # for i in range(p):
    # q1,q2 = I(s, p, ops)
    # q1, q2 = B(s, p, 0)
    # q1, q2 = D(s, p, 110)
    # q1, q2 = L(s, p, 55)
    # q1, q2 = R(s, p, 20)
    # s= q1
    # p = q2
    nowS = s
    nowP = p
    for i in ops:
        choose, n = i
        if choose == 'L':
            nowS,nowP = L(nowS, nowP, n)
        elif choose == 'R':
            nowS, nowP = R(nowS, nowP, n)
        elif choose == 'D':
            nowS, nowP = D(nowS, nowP, n)
        elif choose == 'I':
            nowS, nowP = I(nowS, nowP, n)
        elif choose == 'B':
            nowS, nowP = B(nowS, nowP, n)

    return nowS

    # ********** End ********** #
s = "whatsyourproblem"
p = 5
ops = [
    ['L', 2],
    ['D', 1],
    ['R', 4],
    ['I', 'abcdef'],
    ['L', 3],
    ['B', 2]]
res = solver(s, p, ops)
print(res)