#coding=utf8
import urllib2
import time
import json
import code

def parse(sParams):
    post_params = ""
    for key in sParams.keys():
        key_value = '%s=%s'%(key, sParams[key])
        if len(post_params) == 0:
            post_params = key_value
        else:
            post_params = '%s&%s'%(post_params, key_value)
        #print post_params
    return post_params
    
def request(url):
    response = urllib2.urlopen(url)
    return response.read()
    
def post_json():
    request_url = 'http://open.kaolafm.com/v2/app/active'
    headers = {'Content-type':"application/json"}
    data = {"appid":"wt2713","deviceid":"d9d98e65e7d03e32d8eab33e71fc3540","devicetype":0,"os":"web","osversion":"5.1","packagename":"com.sgm.carlink","sign":"39ab02fa71a2fc111948d3a2fd122842","version":"1.0"}
    data_plain = parse(data)
    #json.dumps(data)不支持gbk格式，所以先将text字段转成utf8
    body = code.gbk(json.dumps(data))
    req = urllib2.Request(request_url, body, headers)
    print request(req)

def post_plain():
    request_url = 'http://open.kaolafm.com/v2/app/active'
    headers = {}
    data = {"appid":"wt2713","deviceid":"d9d98e65e7d03e32d8eab33e71fc3540","devicetype":0,"os":"web","osversion":"5.1","packagename":"com.sgm.carlink","sign":"39ab02fa71a2fc111948d3a2fd122842","version":"1.0"}
    data_plain = parse(data)
    #json.dumps(data)不支持gbk格式，所以先将text字段转成utf8
    body = code.gbk(data_plain)
    req = urllib2.Request(request_url, body, headers)
    print request(req)

post_json()
post_plain()


