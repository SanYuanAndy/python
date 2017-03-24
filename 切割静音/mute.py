#coding=utf8
import os
import csv
from syutil import print_n
import ctypes
import math

f = open(r"test.pcm", "rb")
buf = f.read()
f.close()
seq = bytearray(buf)
print len(seq)

value = []
for i in range(0, len(seq) - 2, 2):
    v = 0
    #小端模式，低字节低地址
    v = seq[i + 1] << 8
    v = v | seq[i]
    '''
    if v & 0x8000 == 0x8000:
        v = v - 0xffff #-1 * (v & 0x7fff)
    '''
    v = ctypes.c_int16(v).value
    value.append(v)

index = []
win_size = 16000/1000*20
i = 0
v_len = 0
v_len = len(value)
mute_db = 20*math.log10(2000)
while i < v_len:
    #print i
    j = 0
    while j < win_size:
        if i + j > len(value) - 1:
            break
        logVal = abs(value[i + j])
        if logVal > 0 and  20*math.log10(logVal) > mute_db:
            break
        j = j + 1
        
    if j == win_size:
        index.append(i)
        i = i + j - 1
    else:
        i = i + j
    i = i + 1
    
for i in range(0, len(index)):
    if not (i - 2 >= 0 and index[i] - index[i - 2] <= 2*win_size):
        continue
    if not (i + 2 < len(index) and index[i + 2] - index[i] <= 2*win_size):
        continue
    for j in range(index[i], index[i] + win_size):
        value[j] = 'a'
        
outstream = bytearray()
for val in value:
    if val != 'a':
        sample = ctypes.c_uint16(val).value
        outstream.append(sample & 0x00ff)
        outstream.append((sample >> 8) & 0xff)

fw = open('result.pcm', 'wb')
fw.write(outstream)
fw.close()
print len(outstream)


    
    
    
