#coding=utf8
import urllib2
import time
import json

def request(url):
    response = urllib2.urlopen(url)
    return response.read()

access_token = None
url_host = "https://aip.baidubce.com/oauth/2.0/token"
grant_type = 'client_credentials'
client_id = 'yqErZfdILGqCsVMfscjywe7p'
client_secret = 'UkZSAYlx6WSIsACqpsxl4yklMj31O4m1'

request_url = '%s?grant_type=%s&client_id=%s&client_secret=%s'%(url_host, grant_type, client_id, client_secret)

ret = request(request_url)
access_token = json.loads(ret).get('access_token')
print access_token


url_nlp = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'

request_url = '%s?access_token=%s'%(url_nlp, access_token)
headers = {'Content-type':"application/json"}
data = {"text":"导航去北京"}
body = json.dumps(data).decode('utf8').encode('gbk')

req = urllib2.Request(request_url, body, headers)

print request(req)
