import os
import sys

files = os.listdir(sys.path[0])

print(files)

for i in files:
    if i.endswith('.c'):
        ori = os.path.join(sys.path[0], i)
        print(ori)

        new = ori + "pp"

        os.rename(ori, new)

# print(files)
