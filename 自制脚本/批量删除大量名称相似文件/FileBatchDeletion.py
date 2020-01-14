'''

    大量文件的批量删除(不会放入回收站中)
    -----------------------------------------
    文件名具有相似性
    eg:
        SQLDmpr3740.mdmp 
        SQLDmpr3741.mdmp 
        SQLDmpr3742.mdmp 

    -----------------------------------------
    拓展:
    存在0001 0002 0003 ... 1000 等补0的名称存在
    此处使用str.zfill(arg) 函数
    arg 为设置的位数

    -----------------------------------------
    变长名称待补充:
    0001 0002 ... 1000 ... 9999 10000

'''

import os


file_name = ''
count = 0

for i in range(0, 9998):
    print(i + 1, end='  ')
    file_name = 'SQLDump' + str(i).zfill(4) + '.txt'
    try:
        if os.path.exists('./' + file_name):
            # print('./' + file_name)
            os.remove('./' + file_name)
            print('./' + file_name + '删除成功' + '------->总计删除文件数:' + str(count))
            count += 1
    except Exception as err:
        print(file_name+'删除出错！！！！！！！！！！！！')

