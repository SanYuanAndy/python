#coding=utf8
import os
import csv
from syutil import print_n
from syutil import del_dir
import ctypes
import math

#将PCM字节流转为short数组
def getSamples(source):
    f = open(source, "rb")
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
    return value

#标注pcm流中的静音段，并返回所有索引
def getMuteIndex(value, muteTime, muteThreshold, win_size):
    index = []
    i = 0
    v_len = 0
    v_len = len(value)
    mute_db = 20*math.log10(muteThreshold)
    while i < v_len:
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
        
    return index

def clearMute(value, index, source, win_size):
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

    fw = open('cut_%s'%(source), 'wb')
    fw.write(outstream)
    fw.close()
    print len(outstream)

def saveCutVoice(value,source):
    outstream = bytearray()
    for val in value:
        if val != 'a':
            sample = ctypes.c_uint16(val).value
            outstream.append(sample & 0x00ff)
            outstream.append((sample >> 8) & 0xff)
    out_file = source
    fw = open(out_file, 'wb')
    fw.write(outstream)
    fw.close()
    print len(outstream)
    
def getVoices(value, index, source, win_size):
    voices = []
    sampleLen = len(value)
    indexLen = len(index)
    i = 0
    while i < indexLen:
        k_begin = 0
        k_end = 0
        if i == 0:
            k = 0
            k_end = index[i]
        elif i == indexLen - 1 and index[i] + win_size < indexLen:
            k = index[i] + win_size
            k_end = indexLen - 1
        elif (i < indexLen - 1) and (index[i + 1] - index[i] > win_size):
            k = index[i] + win_size
            k_end = index[i + 1]
            
        if k_end != 0:
            voice = []
            while k < k_end:
                voice.append(value[k])
                k = k + 1
            voices.append(voice)
        i = i + 1
    return voices
    
        
    
def cutMutes(source, muteTime, muteThreshold):
    sample = getSamples(source)
    win_size = 16000/1000*muteTime
    index = getMuteIndex(sample, muteTime, muteThreshold, win_size)
    clearMute(sample, index, source, win_size)
    
def cutVoices(source, muteTime, muteThreshold):
    sample = getSamples(source)
    win_size = 16000/1000*muteTime
    index = getMuteIndex(sample, muteTime, muteThreshold, win_size)
    voices = getVoices(sample, index, source, win_size)
    cnt = 0
    #####
    out_dir = 'out_%s'%(source)
    out_dir = out_dir.replace('.pcm', "")
    if os.path.exists(out_dir):
        del_dir(out_dir)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    #####
    for voice in voices:
        saveCutVoice(voice, r'%s\%d_%s'%(out_dir,cnt,source))
        cnt = cnt + 1
cutMutes(r'test.pcm', 10, 2000)
cutVoices(r'test.pcm', 100, 2000)
exit(0)


    
    
    
