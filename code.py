#coding=utf8
#中文乱码的原因是显示模块使用的编码与字符串实际的编码不一致
#解决中文乱码的方法是：1、明确显示模块的编码方式。2、将字符串转成与显示模块编码一致
#一般是先转成unicode、然后再转成目标编码

#以下方法可以将任意单一编码格式(仅支持utf8, gbk, unicode)的字符串转为目标编码格式(仅支持gbk、utf8)
#该方法的优点是:不用知道输入字符串的编码格式
#可以使用不同编码的‘你好’和‘你好中国’，测试以下方法，表现不同

import sys

def __code(s, src, target):
    u = ''
    while True:
        try:
            u = s.decode(src)#1可能抛异常，也可能不抛异常
        except UnicodeDecodeError, e:#如果s是target编码，转成unicode失败，抛此异常
            #print repr(e)
            break
        except UnicodeEncodeError, e:#如果s是unicode编码，转成unicode失败，抛此异常
            #print repr(e)
            u = s
        try:
            s = u.encode(target)
        except Exception, e:
            break
        break
    return s
def utf8(s):
    return __code(s, 'gbk', 'utf8')

def gbk(s):
    return __code(s, 'utf8', 'gbk')

######下面为该模块的测试代码##########
if __name__ == '__main__':
    stdout_encode = sys.stdout.encoding #获取输出终端的编码方式
    ss = ['', '', '', '']
    ss[0] = '你好'#s0为utf8编码
    ss[1] = '你好'.decode('utf8').encode('gbk')#s1为gbk编码
    ss[2] = u'你好'#s2为unicode编码
    ss[3] = 'hello, china'
    print stdout_encode
    for str in ss:
        print str

    count = 0
    for str in ss:
        print count 
        print utf8(str)
        print gbk(str)
        count += 1
    #####以下注释原始的实现方式########
    '''
    def utf8(s):
    u = ''
    while True:
        try:
            u = s.decode('gbk')#1可能抛异常，也可能不抛异常
        except UnicodeDecodeError, e:#如果s是utf8编码，转成unicode失败，抛此异常
            print repr(e)
            break
        except UnicodeEncodeError, e:#如果s是unicode编码，转成unicode失败，抛此异常
            print repr(e)
            u = s
        try:
            s = u.encode('utf8')
        except Exception, e:
            break
        break
    return s

    def gbk(s):
    u = ''
    while True:
        try:
            u = s.decode('utf8')
        except UnicodeDecodeError, e:
            #print repr(e)
            break
        except UnicodeEncodeError, e:
            #print repr(e)
            u = s
        try:
            s = u.encode('gbk')
        except Exception, e:
            break
        pass
        break
    return s
    '''



