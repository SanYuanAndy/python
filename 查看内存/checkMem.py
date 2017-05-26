import os
import time
from syutil import print_t
from syutil import print_n

def format_time():
    return time.strftime('%m:%d %H:%M:%S', time.localtime(time.time()))

def checkMem(exp, fos):
    cmd = 'adb shell "dumpsys meminfo|grep %s"'%(exp)
    results = os.popen(cmd).readlines()
    time_tag = "%s\n"%(format_time())
    print_n(time_tag)
    fos.write(time_tag)
    for i in range(0, 3):
        print_n(results[i])
        fos.write(results[i])

f_name = "%s"%(time.strftime('%m%d%H%M%S', time.localtime(time.time())))
f = open(f_name, "w")
while True:
    checkMem('txznet.txz', f)
    #time.sleep(1.0)

f.close()
