#coding=utf8
import os
import sys

cmd = 'dir'

#直接执行cmd命令，不返回输出结果
os.system(cmd)

#执行cmd命令，返回输出结果
dirs = os.popen(cmd).readlines()

for dir in dirs:
    print dir.decode('gbk').encode('utf8')
