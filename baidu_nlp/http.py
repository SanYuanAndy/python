#coding=utf8
import urllib2
import time
import json
import code

def request(url):
    response = urllib2.urlopen(url)
    return response.read()

def getToken():
    access_token = None
    url_host = "https://aip.baidubce.com/oauth/2.0/token"
    grant_type = 'client_credentials'
    client_id = 'yqErZfdILGqCsVMfscjywe7p'
    client_secret = 'UkZSAYlx6WSIsACqpsxl4yklMj31O4m1'
    request_url = '%s?grant_type=%s&client_id=%s&client_secret=%s'%(url_host, grant_type, client_id, client_secret)
    ret = request(request_url)
    return json.loads(ret).get('access_token')


def lexer(sText, access_token):
    url_nlp = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'
    request_url = '%s?access_token=%s'%(url_nlp, access_token)
    headers = {'Content-type':"application/json"}
    data = {"text":"导航"}
    data['text'] = code.utf8(sText)
    #json.dumps(data)不支持gbk格式，所以先将text字段转成utf8
    body = code.gbk(json.dumps(data))
    req = urllib2.Request(request_url, body, headers)
    print request(req)
    
def dnn(sText, access_token):
    url_nlp = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn'
    request_url = '%s?access_token=%s'%(url_nlp, access_token)
    headers = {'Content-type':"application/json"}
    data = {"text":"导航"}
    data['text'] = code.utf8(sText)
    #json.dumps(data)不支持gbk格式，所以先将text字段转成utf8
    body = code.gbk(json.dumps(data))
    req = urllib2.Request(request_url, body, headers)
    print request(req)

def simnet(sText, access_token):
    url_nlp = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet'
    request_url = '%s?access_token=%s'%(url_nlp, access_token)
    headers = {'Content-type':"application/json"}
    data = {"text":"导航"}
    data['text'] = code.utf8(sText)
    #json.dumps(data)不支持gbk格式，所以先将text字段转成utf8
    body = code.gbk(json.dumps(data))
    req = urllib2.Request(request_url, body, headers)
    print request(req)
    
def input_text():
    while True:
        input_content = raw_input(':')
        if input_content == 'exit':
            break
        lexer(input_content, getToken())
        dnn(input_content, getToken())
        
input_text()
