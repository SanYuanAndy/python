#coding=utf8
import urllib2
import time
def request(url):
    response = urllib2.urlopen(url)
    return response.read()

def requstBusiness(url):
    begin = time.time()
    print begin
    ret = request(url)
    now = time.time()
    print now
    print ret
    print ("cost(%f)秒")%(now - begin)

keyword = "中科大厦"
city = 'shenzhen'
appKey = 'x6zwcihxyiyvfmqvnjm2vmbfwljetmndpaucisih'

text = '深圳今天天气怎么样'
url_host = 'http://scv2.hivoice.cn/service/iss?'
url_param1 = 'platform=&screen=&text=%E5%AF%BC%E8%88%AA%E5%8E%BB%E8%A1%A1%E9%98%B3%E5%B8%82%E9%9B%81%E5%9F%8E%E5%B0%8F%E5%AD%A6&viewid=&'
url_param1 = 'platform=&screen=&text=%s&viewid=&'%(urllib2.quote(text))
url_param2 = 'appkey=%s&udid=b48d3571-d20d-449f-b1f2-51bc731d178b&ver=2.0&appsig=62D44867B5E1794EE43158E484310674ACD84FD2&appver='%(appKey)
url_param3 = 'com.txznet.txz&city=%E6%B7%B1%E5%9C%B3%E5%B8%82&history=&voiceid=&time=2017-06-12+15%3A03%3A18&scenario=incar&gps=22.537698%2C113.952003&method=iss.getTalk&dpi='

url = "%s%s%s%s"%(url_host, url_param1,url_param2, url_param3)
#url = "http://www.baidu.com"
#url = '''http://apis.juhe.cn/baidu/getData?key=nNt3GLr7InLzplGlx36LBxVhhgLAPGqv&cid=1&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&page=2'''
#url = '''http://restapi.amap.com/v3/place/text?&keywords=%s&city=%s&citylimit=true&&output=json&offset=5&page=1&key=569ddbc4a01b1b1bb617f2c22d35ba16&extensions=base'''%(keyword, city)
print url

print ''
print ''
#正常语义
print '测试语义加网络请求总耗时'
requstBusiness(url)
print ''

#appKey = 'x6zwcihxyiyvfmqvnjm2vmbfwljetmndpaucisiw'
url_host = 'http://scv2.hivoice.cn/service/iss?'
url_param1 = 'platform=&screen=&text=&viewid=&'
url_param2 = 'appkey=%s&udid=b48d3571-d20d-449f-b1f2-51bc731d178b&ver=2.0&appsig=62D44867B5E1794EE43158E484310674ACD84FD2&appver='%(appKey)
url_param3 = 'com.txznet.txz&city=%E6%B7%B1%E5%9C%B3%E5%B8%82&history=&voiceid=&time=2017-06-12+15%3A03%3A18&scenario=incar&gps=22.537698%2C113.952003&method=iss.getTalk&dpi='
url = "%s%s%s%s"%(url_host, url_param1,url_param2, url_param3)
#错误的key
print '测试网络请求耗时'.decode('utf8').encode('gbk')
requstBusiness(url)
