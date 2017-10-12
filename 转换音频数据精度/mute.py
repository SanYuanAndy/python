#coding=utf8
import os
import csv
from syutil import print_n
from syutil import del_dir
import ctypes
import math
import struct

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
        v_byteArray = [0,0,0,0]
        while k < byteCnt:
            #小端模式，低字节低地址
            v = v | (seq[i + k] << (8 * (k)))
            v_byteArray[byteCnt - 1 - k] = seq[i +k]
            print hex(seq[i + k])
            k = k + 1
            
        i = i + byteCnt
        tmp = ctypes.c_float(v).value
        print tmp
        print 'bbb'
        tmp = struct.unpack('!f',struct.pack('4b', *v_byteArray))[0]
        print tmp
        print 'aaa'
        a = 1
        if tmp < 0:
            a = -1
        v = a * (2**32 - 1)**(a * tmp)
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

hightWidth = 32
lowWidth = 16
samples = getSamples('f_%d.pcm'%(hightWidth), hightWidth)
outstream = getByteStream(samples, hightWidth, lowWidth)
saveVoice(outstream, 'test_%d_%d.pcm'%(hightWidth, lowWidth))


    
    
    
