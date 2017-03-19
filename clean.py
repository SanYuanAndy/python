#coding=utf8
import os
import sys
import re
from code import __code
from code import gbk

def del_special_file(dir, pattern):
    if os.path.isdir(dir):
        listdir = os.listdir(dir)
        for subdir in listdir:
            subdir = os.path.join(dir, subdir)
            del_special_file(subdir, pattern)
    else:
        if pattern.match(dir) != None:
            print 'del dir %s'%(dir)
            os.remove(dir)

cwd = os.getcwd()
print cwd
strPattern = r'^.*\.pyc'#加上‘r’,不会被转义，输出的和写入的一样
pattern = re.compile(strPattern,re.I);
del_special_file(cwd, pattern)
    

