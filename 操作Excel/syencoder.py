#coding=utf-8
import codecs

#unicode是标准编码
#uft-8和gbk之间的转换，必须通过unicode中转
#每个软件都有默认的编码工作模式，即处于gbk编码模式下的shell等软件，
#只能显示gbk编码格式的文本。否则出现中文乱码等问题。

def utf2gbk(src):
    return src.decode('utf-8').encode('gb2312')

def gbk2utf(src):
    return src.decode('gb2312').encode('utf-8')
