#coding=utf8
import os
import code

def scan(sDir):
    if not os.path.exists(sDir):
        print '%s is not exists'%(sDir)
    
    if not os.path.isdir(sDir):
        print '%s is not dir'%(sDir)

    
    children = os.listdir(sDir)
    if len(children) < 1:
        print '%s has not children'%(sDir)

    results = []
    for child in children:
        #print child
        if child.endswith(".wav") or child.endswith(".pcm"):
            #print child
            tmp = child.split("_")
            #print tmp
            word = tmp[1]
            score = code.utf8(tmp[2]).replace('负', '-')
            '''
            print word
            print score
            print child
            '''
            val = {}
            val['word'] = word
            val['score'] = score
            val['path'] = child
            results.append(val)
            
    return results

def printInfo(values, out):
    if len(values) == 0:
        print 'empty data'
        return None
    
    f = None
    if out != None:
        try:
            f = open(out, 'wb')
        except Exception, e:
            print e
            return
    if f != None:
        head = '%s,%s,%s'%('唤醒词', '唤醒分数', '唤醒录音')
        try:
            f.write(code.gbk(head + '\n'))
        except Exception, e:
            print e
        
    for value in values:
        s = '%s,%s,%s'%(value['word'], value['score'], value['path'])
        if f != None:
            try:
                f.write(s + '\n')
            except Exception, e:
                print e
                break
        else:
            print s

    if f != None:
        try:
            f.close()
        except Exception, e:
            print e
    
pwd = os.getcwd()
results = scan(pwd)
printInfo(results, 'results.csv')
print len(results)
    
