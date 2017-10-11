#coding=utf8
import os
import json
import urllib2
import time
import re

def request(url):
    response = urllib2.urlopen(url)
    return response.read()

#param2 = "text=%s"%(urllib2.quote(text))

def load(data):
    with open(data, 'r') as f:
        sJson = f.read()
        #print sJson
        jsonObj = json.loads(sJson)
        return jsonObj
    
def loadFromUrl(url):
    sJson = ''
    trycnt = 0
    while trycnt < 3:
        try:
            trycnt = trycnt + 1
            sJson = request(url)
            break
        except Exception,e:
            print e
            print 'happen error try again '
            time.sleep(1)
            continue
    
    jsonObj = json.loads(sJson)
    return jsonObj

def sort(data, target):
    new_data = {}
    for key in data.keys():
        #print '%-10d : %s'%(data[key], key)
        #if re.match('^.*all\.asr\.*.I\.all', key):
            #print 111
        if re.match(r'^.*all.asr..*.I.all', key) and key.find(target) != -1:
            new_data["%s"%(data[key])] = key
    return new_data

#显示最多maxCnt家客户数据，返回所有客户的数据的总和
def display(data, maxCnt):
    keys = data.keys()
    new_keys = []
    for key in keys:
        new_keys.append(int(key))
    new_keys.sort()
    new_keys.reverse()
    cnt = 0
    for new_key in new_keys:
        key = "%d"%(new_key)
        cnt = cnt + 1
        if cnt > maxCnt:
            break
        print '%-10s:%s'%(key, data[key])

    count = 0
    for new_key in new_keys:
        count = count + new_key

    return count

#jsonObj = load('data.json')
def printData(sDate):
    url_svr = 'http://monitor.txzing.com/tmp_task/get_all_client_asr_data?date=%s'%(sDate)
    jsonObj = loadFromUrl(url_svr)
    print sDate
    print '-----ifly----'
    ifly = sort(jsonObj, 'ifly')
    ifly_total = display(ifly, 10)
    print
    print '-----yzs----'
    yzs = sort(jsonObj, 'yzs')
    yzs_total = display(yzs, 10)
    total = ifly_total + yzs_total
    print
    print '两家引擎访问量详细数据'
    print 'total : %d'%(total)
    print 'ifly : %d'%(ifly_total)
    print 'yzs : %d'%(yzs_total)
    print '两家引擎访问量占用百分比'
    print "ifly : %d%s"%((ifly_total*1.0/(total)*100), "%")
    print "yzs : %d%s"%((yzs_total*1.0/(total)*100), "%")
    print
    print

def dateFromTime(sTime):
    date = time.strftime('%Y%m%d',time.localtime(sTime))
    return date

now = time.time();
#最近三天的数据
printData(dateFromTime(now))
printData(dateFromTime(now - 1*24*60*60))
printData(dateFromTime(now - 2*24*60*60))

#过去几天的数据
for i in range(3, 20, 5):
    printData(dateFromTime(now - i * 24*60*60))
    
'''
printData("20170928")
printData("20170927")
printData("20170920")
printData("20170915")
printData("20170910")
'''

