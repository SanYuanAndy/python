#coding=utf8
import os
import syos
import code
import time

targetDir = "/sdcard/txz/voice/wk"
#targetDir = "/sdcard/alldemo/voice_wk"
def list_dir(path):
    cmd = 'adb shell ls %s'%(path)
    p = os.popen(cmd)
    return p.readlines()

def pullFile(path, newName):
    cmd = "adb pull %s wk/%s"%(path, newName)
    os.system(cmd)
    
def pull(all_file, targetDir):
    if not os.path.exists("wk"):
        os.mkdir("wk")
        
    shell_cmd = "adb shell"
    cd_cmd = "cd %s"%(targetDir)
    exit_cmd = "exit"
    child_proc = syos.SelfProcess(shell_cmd, None)
    child_proc.write(cd_cmd)
    child_proc.write('\n')
    time.sleep(0.05)
    count = 0
    for f in all_file:
        if not f.startswith("txz_"):
            continue
        oldName = f.replace("\r\n", "")
        print oldName
        #continue
    
        count += 1
        newName = "new_%d.pcm"%(count)
        cp_cmd = "cp %s %s"%(oldName, newName)
        child_proc.write(cp_cmd)
        child_proc.write('\n')
        time.sleep(0.05)
        pullFile("%s/%s"%(targetDir, newName), code.gbk(oldName))
    time.sleep(0.1)
    rm_tmp_cmd = "rm new*"
    child_proc.write(rm_tmp_cmd)
    child_proc.write('\n')
    time.sleep(0.1)
     
    child_proc.write(exit_cmd)
    child_proc.write('\n')
    child_proc.wait()

all_file = list_dir(targetDir)
pull(all_file, targetDir)
