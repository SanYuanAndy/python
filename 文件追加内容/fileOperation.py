#coding=utf8
import os

#按行获取文件内容,主动去掉了行末的换行符
def readlines(dataInputFile):
    newlines = []
    f = open(dataInputFile)
    while True:
        lines = f.readlines(1000)
        if len(lines) == 0:
            break
        for line in lines:
            if len(line) > 0:
                line = line[0:len(line) - 1]
            newlines.append(line)
    if f != None:
        f.close()
    return newlines

def writelines(out, data):
    f = open(out, 'wb')
    for line in data:
        if len(line) == 0:
            continue
        f.write(line)
        f.write('\n')
    if f != None:
        f.close()

#测试使用
if __name__ == '__main__':
    for line in readlines('cpu'):
        print line

    print readlines('cpu')


