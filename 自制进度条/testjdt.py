# coding=utf-8
import time
for i in range(101):
    print('\r进度：['+'='*i+'] '+"%d"%i+'%',end=' ')
    time.sleep(0.01)
