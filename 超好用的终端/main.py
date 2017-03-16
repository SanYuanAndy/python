#coding=utf8
import threading
import time
import os
import sub_process
import sys
from syutil import parse_path
from syutil import del_dir
from syutil import format_time
from syutil import print_t

class workThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            strInput = raw_input(">")
            if strInput == "exit":
                break
            try:
                proc = sub_process.SelfProcess(strInput, None)
                proc.wait()
            except Exception, e:
                print_t(str(e))
#cmd = "adb shell"
#proc = sub_process.SelfProcess(cmd, None)#作用与用法类似与os.system(cmd)，但是可以设置命令运行的最大时长，填None则不限时
t1 = workThread()
t1.start()
