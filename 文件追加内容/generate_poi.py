#coding=utf8
import os
import sys
import fileOperation

stdin_encoding =  sys.stdin.encoding
stdout_encoding = sys.stdout.encoding

    
def get_poi(origin_data):
    pois = '中国'
    for poi in origin_data:
        if len(poi) == 0:
            continue
        pois = 's%|%s'%(pois, poi)
    return pois

def console_input(output):
    source_file_path = None
    secret = None
    prompt1 = "需要追加内容的文件(输入'exit'退出):"
    
    while True:
        input_content = raw_input(prompt1.decode('utf8').encode(stdin_encoding))
        if input_content == 'exit':
            return
        if len(input_content) == 0:
            print 'file path can not be empty'
            continue
        if not os.path.exists(input_content):
            print 'file do not exists'
            continue
        source_file_path = input_content
        break
    temp_data = fileOperation.readlines(source_file_path)
    pois = []
    line_num = 0
    for line in temp_data:
        i = 0
        line_num = line_num + 1
        #print line
        try:
            line = line.decode('utf8')
        except:
            print line
            print line_num
            break
            
        while True:
            lenght = len(line)
            #print lenght
            if lenght < 4:
                pois.append(line.encode('utf8'))
                break
            pois.append(line[0:4].encode('utf8'))
            line = line[4:]

    fileOperation.writelines('poi', pois)
            
input_content = console_input('output')
