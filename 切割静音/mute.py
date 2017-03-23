#coding=utf8
import os
from syutil import print_n

f = open(r"test.pcm", "rb")
buf = f.read()
seq = bytearray(buf)
for i in range(0, 16*16 - 1):
    sHex = "%x"%(seq[i])
    if len(sHex) == 1:
        sHex = "0%s"%(sHex)
    print_n(sHex)
    print_n(' ')
    if (i + 1)%16 == 0:
        print_n('\n')
