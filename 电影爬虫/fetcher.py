#coding=utf8
import urllib2
import time
from HTMLParser import HTMLParser
import code
import re
import threading
import thread

def request(url):
    response = urllib2.urlopen(url)
    return response.read()

class Parser(HTMLParser):
    is_item = False
    div_tag_cnt = 0
    items = []
    def __init__(self):
        HTMLParser.__init__(self)
        #print '__init__'
    def handle_starttag(self, tag, attr):
        #开始记录item
        if tag == 'div' and self.is_list_item(attr):
            #print '---------'
            self.is_item = True
            self.div_tag_cnt = 0
            item = {}
            self.items.append(item)
        if self.is_item:
            #print 'start_tag'
            #print tag
            #if len(attr) > 0:
                #print attr
            if tag == 'div':
                self.div_tag_cnt = self.div_tag_cnt + 1
            if tag == 'a' and len(attr) > 1:
                if attr[1][0] == 'title':
                    #print attr[1][1]
                    a = self.items[len(self.items) - 1]
                    a['title'] = attr[1][1]
                    a['href'] = attr[0][1]
                    self.items[len(self.items) - 1] = a
                
    def handle_endtag(self,tag):
        if self.is_item:
            #print 'end_tag'
            #print tag
            if tag == 'div':
                self.div_tag_cnt = self.div_tag_cnt - 1
                
                if self.div_tag_cnt == 0:
                    #print 'XXXXXXXX'
                    self.is_item = False
                    
    def handle_data(self, data):
        if self.is_item:
            #print 'handle_data_0'
            data = data.replace('\r\n', "")
            #if len(data) > 0:
                #print data
            #print 'handle_data_1'
    def is_list_item(self, attrs):
        for atts in attrs:
            #print atts
            if "list-pianyuan-box" in atts:
                return True   
        return False

    def get_list(self):
        return self.items
#条件过滤
def search(sContent):
    return re.search(r"常州|同事", sContent)
    
def parse(sPage, url):
    parser = Parser()
    parser.feed(sPage)
    parser.close()
    avis = parser.get_list()
    domain = url.replace("http://", "").split("/")[0]
    for avi in avis:
        #统一转换成utf8
        sTitle = code.utf8(avi['title'])
        if search(sTitle):
            print avi['title']
            print "http://%s/%s"%(domain, avi['href'])
            print 

def fetch(i):
    sDomain = ""
    sUrl = "http://%s/list/index%d_%d.html"%(sDomain,8,i)
    print sUrl
    try:
        sContent = request(sUrl)
        parse(sContent, sUrl)
    except Exception, e:
        print e

queue = range(1,40)
locker = threading.Lock()
    
def fetch_task():
    while True:
        index = -1
        locker.acquire()
        queue_len = len(queue)
        if queue_len > 0:
            index = queue.pop(0)
        locker.release()

        if index == -1:
            return
    
        fetch(index)
        print index

#多线程访问
for k in range(0, 10):
    try:
        thread.start_new_thread(fetch_task, ())
    except Exception,e:
        print e

    
        
