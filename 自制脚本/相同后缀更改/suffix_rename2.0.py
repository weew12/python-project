import os
import sys

targetDir = input('请输入文件目录绝对路径(输入#代表默认当前路径)>>>')
if targetDir == '#':
    targetDir = sys.path[0]
originalSuffix = input('请输入要修改的文件原后缀 >>>')
changeSuffix = input('请输入要修改为的后缀 >>>')

# print(os.listdir(sys.path[0]))
files = os.listdir(targetDir)

print(files)

for i in files:
    if i.endswith(originalSuffix):
        ori = os.path.join(sys.path[0], i)
        print(ori)

        new = ori.split(originalSuffix)[0] + changeSuffix
        print(new)
        os.rename(ori, new)

# # print(files)
