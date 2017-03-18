#coding=utf8
import os
import sys
from code import __code
from code import gbk
cwd = os.getcwd()
print cwd
listdir = os.listdir(cwd)

for dir in listdir:
    #抛异常说明dir含有gbk格式的中文
    try:
        dir = dir.decode('utf8').encode('gbk')
    except Exception, e:
        pass
    print dir

print ""
print sys.stdout.encoding
s = "你好"#s是utf8编码
print s
s = s.decode('gbk').encode('utf8')#不会抛异常
print s

s1 = u"你好"
print s1
print s1.encode('gbk')
print s1.encode('utf8')
print __code(s1, 'gbk', 'gbk')

