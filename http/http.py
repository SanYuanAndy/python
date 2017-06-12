#coding=utf8
import urllib2
import time
def request(url):
    response = urllib2.urlopen(url)
    return response.read()

url = "http://scv2.hivoice.cn/service/iss?platform=&screen=&text=%E5%AF%BC%E8%88%AA%E5%8E%BB%E8%A1%A1%E9%98%B3%E5%B8%82%E9%9B%81%E5%9F%8E%E5%B0%8F%E5%AD%A6&viewid=&appkey=x6zwcihxyiyvfmqvnjm2vmbfwljetmndpaucisih&udid=b48d3571-d20d-449f-b1f2-51bc731d178b&ver=2.0&appsig=62D44867B5E1794EE43158E484310674ACD84FD2&appver=com.txznet.txz&city=%E6%B7%B1%E5%9C%B3%E5%B8%82&history=&voiceid=&time=2017-06-12+15%3A03%3A18&scenario=incar&gps=22.537698%2C113.952003&method=iss.getTalk&dpi="

begin = time.time()
print begin
ret = request(url)
now = time.time()
print now
print now - begin
print ret
