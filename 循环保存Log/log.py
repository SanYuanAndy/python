import os
import time

def log(index):
    cmdline = "adb logcat -v threadtime > txz_%s"%(index)
    os.system(cmdline)

def curr_log_list():
    currdir_list = os.listdir(".")
    log_list = []
    for child in currdir_list:
        if child.startswith("txz_"):
            log_list.append(child)
    return log_list

def create_log(preTag,index):
    cmd_create = 'adb logcat -v timethread  > %s_%d'%(preTag, index)
    #cmd_create = 'echo "txz" > %s_%d'%(preTag, index)
    os.system(cmd_create)
    
def move_log(log_list):
    if len(log_list) < 2:
        return
    cmd_del = "del %s"%(log_list[0])
    print cmd_del
    os.system(cmd_del)
    time.sleep(1)
    for index in range(1, len(log_list)):
        cmd_mv = "move %s %s"%(log_list[index], log_list[index -1])
        print cmd_mv
        os.system(cmd_mv)
        
MAX_LOG_COUNT = 5

while True:
    time.sleep(2)
    log_list = curr_log_list()
    count = len(log_list)
    if count < MAX_LOG_COUNT:
        create_log("txz", count)
    else:
        move_log(log_list)
        create_log("txz", count - 1)





