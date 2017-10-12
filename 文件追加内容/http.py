#coding=utf8
import urllib2
import time
def request(url):
    response = urllib2.urlopen(url)
    return response.read()

def InternetWorm():
    f = open('tmp', 'wb')
    for i in range(1, 50):
        request_url = 'http://www.pingfandeshijie.net/di-yi-bu-%2d.html'%(i)
        request_url = request_url.replace(' ', '0')
        ret = request(request_url)
        f.write(ret)
        print request_url
    
    if f!= None:
        f.close()

InternetWorm()
    


