#coding=utf8
import thread
import time
import os

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

def pull_src(source, target):
    if target == ".":
        target = parse_path(source)
    cmd = 'adb pull %s %s'%(source, target)
    #print cmd
    if os.path.exists(target):
        del_dir(target)
    os.mkdir(target)
    os.system(cmd)

def format_time():
    return time.strftime('%m%d_%H%M%S', time.localtime(time.time()))

def save_sys_log(target):
    if target == ".":
        target = 'sys_log'
    if not os.path.exists(target):
        os.makedirs(target)
    strSuffix = ".log"
    log_path = "%s/%s%s"%(target, format_time(), strSuffix)
    cmd = 'adb logcat -v time > %s'%(log_path)
    print cmd
    os.system(cmd)

def save_sys_info(target, infoType):
    if target == ".":
        target = 'sys_log'
    if not os.path.exists(target):
        os.makedirs(target)
    strSuffix = ".log"
    log_path = "%s/%s%s"%(target, format_time(), strSuffix)
    if infoType == 0:
        cmd = 'adb logcat -v time > %s'%(log_path)
    elif infoType == 1:
        cmd = 'adb shell top -m 10 -d 1 > %s'%(log_path)
    elif infoType == 2:
        cmd = 'adb shell top -m 10 -d 1 -t > %s'%(log_path)
    else:
        retrun
    os.system(cmd)
def exit_proc():
    time.sleep(10)
    print 'exit'
    exit(0)

thread.start_new_thread(pull_src, ("/sdcard/txz/log/", ".",))
thread.start_new_thread(save_sys_info, ("sys_log", 0,))
thread.start_new_thread(save_sys_info, ("sys_cpu", 1,))
thread.start_new_thread(save_sys_info, ("sys_cpu_t", 2,))
thread.start_new_thread(exit_proc, ())
