#coding=utf-8
import csv
import sys
from syencoder import gbk2utf,utf2gbk


def write_csv(csvfile):
    f = file(csvfile, 'wb')
    writer = csv.writer(f)
    writer.writerow(['1', '2', '3'])
    data = [(utf2gbk('小河'), '25', '1234567'), (utf2gbk('小芳'), '18', '789456')]
    writer.writerows(data)
    f.close()

    
