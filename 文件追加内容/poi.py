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
        pois = '%s|%s'%(pois, poi)
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
    f = open(source_file_path, 'ab+')
    f.seek(os.path.getsize(source_file_path))
    f.write("\n")
    f.write('''<navPOI>=(\n''')
    f.write('''"<navPOI_>"(\n''')
    f.write(get_poi(fileOperation.readlines('poi')))
    f.write('\n')
    f.write(''')"</navPOI_>"\n''')
    f.write(''');''')
    if f != None:
        f.close()

input_content = console_input('output')
