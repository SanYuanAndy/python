#coding=utf8
import threading
import time
import os
import sys
import signal
import syos
from syutil import parse_path
from syutil import del_dir
from syutil import format_time
from syutil import print_t

def quit(signum, frame):
    pass

class workThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        child_proc = None
        while True:
            prompt = '>'
            if child_proc != None and child_proc.isAlive():
                prompt = ""
            try:
                pass
                strInput = raw_input(prompt)#不包含换行符Ctrl+C会抛异常
            except Exception, e:
                print_t(str(e))
                continue

            if child_proc != None and child_proc.isAlive():
                strInput = strInput.decode('gbk').encode('utf8')
                child_proc.write(strInput)
                child_proc.write('\n')
                child_proc.wait()
                continue
            if strInput == "exit":
                break
            if strInput == "":
                continue
            try:
                child_proc = syos.SelfProcess(strInput, None)
                #proc.wait()
            except Exception, e:
                pass
                print_t(str(e))
#cmd = "adb shell"
#proc = sub_process.SelfProcess(cmd, None)#作用与用法类似与os.system(cmd)，但是可以设置命令运行的最大时长，填None则不限时
def main():
    #signal.signal(signal.SIGINT, quit)
    t1 = workThread()
    t1.start()

if __name__ == "__main__":
    main()

