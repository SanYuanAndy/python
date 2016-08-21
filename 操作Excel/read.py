#coding=utf-8
import csv
import json
from syencoder import gbk2utf

def read_csv_format_as_utf8(csvfile):
    f = file(csvfile, 'rb')
    reader = csv.reader(f)

    #角色的名称列表
    rolesName = []
    index = 0

    #主题对象
    theme = {}
    for line in reader:
        #第一行是所有角色名称列表
        if index == 0:
            rolesName = line
            index += 1
            continue
        
        #角色对象
        roles = {}
        print len(line)
        #第0列是TAG,第1列是标准文本，后面是角色和音频路径交替出现
        for i in range(2, len(line), 2):
            utf8tTextList = []
            if len(line[0]) != 0:
                for text in line[i].split('\n'):
                    if len(text) == 0:
                        continue
                    utf8tTextList.append(gbk2utf(text))
            roles[gbk2utf(rolesName[i])] = utf8tTextList
        
        theme[gbk2utf(line[0])] = roles
  
    data = json.dumps(theme, ensure_ascii=False)
    print data

    #写到json文件去
    fo = open("theme.json", "wb")
    fo.write(data)

    #关闭文件
    fo.close()
    f.close()

src = 'src.csv'    
read_csv_format_as_utf8(src)
    
