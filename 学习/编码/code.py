
#coding=utf8

#中文乱码的原因是显示模块使用的编码与字符串实际的编码不一致
#解决中文乱码的方法是：1、明确显示模块的编码方式。2、将字符串转成与显示模块编码一致
#一般是先转成unicode、然后再转成目标编码

import sys

stdout_encode = sys.stdout.encoding #获取输出终端的编码方式
print "stdout.encode ： %s" % (stdout_encode)

str = u'你好世界' #unicode编码方法保存字符串
print str
str = str.encode(stdout_encode) #unicode编码直接转成输出终端使用的编码方式
print str

str = '你好世界' #utf8编码方法保存字符串
str = str.decode('utf8').encode(stdout_encode) #先将utf8编码转成unicode编码, 然后转成输出终端使用的编码方式
print str