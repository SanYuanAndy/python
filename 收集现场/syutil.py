#coding=utf8
import time
import os
import threading

def parse_path(path):
        temp = path.split("/")
        target = temp[len(temp) - 1]
        #print temp
        i = len(temp) - 1
        while i >= 0:
            if temp[i] != "":
                return temp[i]
            i -= 1 
        return ""

def del_dir(target):
    del_cmd = 'rd /s /q %s'%(target)
    os.system(del_cmd)

def format_time():
    return time.strftime('%m%d_%H%M%S', time.localtime(time.time()))

mutex = threading.Lock()
#同步打印接口，解决多线程调用print，出现换行符紊乱的问题
def print_t(content):
    mutex.acquire()
    print content
    mutex.release()
