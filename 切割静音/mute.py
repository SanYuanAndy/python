#coding=utf8
import os
import csv
from syutil import print_n

f = open(r"test.pcm", "rb")
buf = f.read()
seq = bytearray(buf)
'''
for i in range(0, 16*16):
    #sHex = "%4d"%(seq[i])
    sHex = "%x"%(seq[i])
    if len(sHex) == 1:
        sHex = "0%s"%(sHex)
    print_n(sHex)
    print_n(' ')
    if (i + 1)%16 == 0:
        print_n('\n')
'''
print

def write_csv(csvfile, data):
    f = file(csvfile, 'wb')
    writer = csv.writer(f)
    #data = [['1','1234567'], ['2','789456']]
    writer.writerow(['num', 'value'])
    writer.writerows(data)
    f.close()
  
value = []
sValue = []
for i in range(0, 32000 - 2, 2):
    v = 0
    v = seq[i] << 8
    v = v | seq[i+1]
    if v & 0x8000 == 0x8000:
        v = -1 * (v & 0x7fff)
    value.append(v)
    sHex = "%d"%(v)
    row = []
    row.append('%d'%(len(sValue)))
    row.append(sHex)
    sValue.append(row)
    '''
    sHex = "%x"%(v)
    if len(sHex) == 3:
        sHex = "0%s"%(sHex)
    if len(sHex) == 1:
        sHex = "000%s"%(sHex)
    '''
    '''
    print_n(sHex)
    print_n(' ')
    if (i + 2)%16 == 0:
        print_n('\n')
    '''

write_csv("test.csv", sValue)
    
