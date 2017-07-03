#coding=utf8
import urllib2
import time

def request(url):
    response = urllib2.urlopen(url)
    return response.read()

text = '你好'
url_svr = "http://scv2.hivoice.cn/service/iss"
param1 = "platform=&screen="
param2 = "text=%s"%(urllib2.quote(text))
param3 = "viewid=&appkey=x6zwcihxyiyvfmqvnjm2vmbfwljetmndpaucisih&udid=b48d3571-d20d-449f-b1f2-51bc731d178b"
param4 = "ver=2.0&appsig=62D44867B5E1794EE43158E484310674ACD84FD2&appver=com.txznet.txz&city=%E6%B7%B1%E5%9C%B3%E5%B8%82"
param5 = "history=&voiceid=&time=2017-06-12+15%3A03%3A18&scenario=incar&gps=22.537698%2C113.952003&method=iss.getTalk&dpi="

request_url = '%s?%s&%s&%s&%s&%s'%(url_svr, param1, param2, param3, param4, param5)
begin = time.time()
print begin
ret = request(request_url)
now = time.time()
print now
print now - begin
print ret
