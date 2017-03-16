#coding=utf8
import threading
import time
import os
import sub_process
from syutil import parse_path
from syutil import del_dir
from syutil import format_time

def pull_src(source, target):
    if target == "." or len(target) == 0:
        target = parse_path(source)
    cmd = 'adb pull %s %s'%(source, target)
    #print cmd
    if os.path.exists(target):
        del_dir(target)
    os.mkdir(target)
    #os.system(cmd)
    proc = sub_process.SelfProcess(cmd, None)

def save_sys_info(target, infoType, timeOut):
    if target == ".":
        target = 'sys_log'
    if not os.path.exists(target):
        os.makedirs(target)
    strSuffix = ".log"
    saved_path = "%s/%s%s"%(target, format_time(), strSuffix)
    if infoType == 0:
        cmd = 'adb logcat -v time > %s'%(saved_path)
    elif infoType == 1:
        cmd = 'adb shell top -m 10 -d 1 > %s'%(saved_path)
    elif infoType == 2:
        cmd = 'adb shell top -m 10 -d 1 -t > %s'%(saved_path)
    else:
        retrun
    #os.system(cmd)
    proc = sub_process.SelfProcess(cmd, timeOut)#作用与用法类似与os.system(cmd)，但是可以设置命令运行的最大时长，填None则不限时

class workThread(threading.Thread):
    def __init__(self, target, infoType, nTimeOut):
        threading.Thread.__init__(self)
        self.target = target
        self.infoType = infoType
        self.nTimeOut = nTimeOut
    def run(self):
        if self.infoType == 1000 :
            pull_src("/sdcard/txz", "")
        else:
            save_sys_info(self.target, self.infoType, self.nTimeOut)

t1 = workThread("sys_log", 0, 20)#保存系统log 20秒
t1.start()
t2 = workThread("sys_cpu", 1, 20)#保存进程CPU状态 20秒
t2.start()
t3 = workThread("sys_cpu_t", 2, 20)#保存线程CPU状态 20秒
t3.start()
t4 = workThread("", 1000, None)#拉去TXZ的目录 不限时
t4.start()
