#coding=utf8
import os
import csv
from syutil import print_n
from syutil import del_dir
import ctypes
import math

#将PCM字节流转为short数组
def getSamples(source, bitWidth):
    f = open(source, "rb")
    buf = f.read()
    f.close()
    seq = bytearray(buf)
    print len(seq)

    byteCnt = bitWidth/8
    
    value = []
    seq_len = len(seq)
    i = 0
    while i + byteCnt < seq_len:
        v = 0
        k = 0
        while k < byteCnt:
            #小端模式，低字节低地址
            v = v | (seq[i + k] << (8 * k))
            k = k + 1
        i = i + byteCnt
        
        value.append(v)
        
    return value

def getByteStream(value, hightWidth, lowWidth):
    outstream = bytearray()
    for val in value:
        #sample = ctypes.c_uint16(val).value
        sample = val
        sample = sample >> (hightWidth - lowWidth)#等同于sample 除以[(2^hightWidth）除以(2^lowWidth)]
        byteCnt = lowWidth/8#字节个数

        #转成字节流
        outstream.append(sample & 0x00ff)
        byteCnt = byteCnt -1
        while byteCnt > 0:
            sample = sample >> 8
            outstream.append(sample & 0x00ff)
            byteCnt = byteCnt -1
    return outstream

    
def saveVoice(outstream,target):
    out_file = target
    fw = open(out_file, 'wb')
    fw.write(outstream)
    fw.close()


samples = getSamples('test32.pcm', 32)
outstream = getByteStream(samples, 32, 16)
saveVoice(outstream, 'test_1.pcm')


    
    
    
