#coding=utf8
import subprocess
import time
import threading
import sys
from syutil import print_t
class timeOutThread(threading.Thread):
    def __init__(self, proc, nTimeOut):
        threading.Thread.__init__(self)
        self.proc = proc
        self.nTimeOut = nTimeOut
    def run(self):
        self.time_out(self.proc, self.nTimeOut)
    def time_out(self, proc, timetout):
        time.sleep(timetout)
        proc.terminate()

class redirecThread(threading.Thread):
    def __init__(self, proc, target):
        threading.Thread.__init__(self)
        self.proc = proc
        self.target = None
        self.file = None
        if target != None and len(target)!= 0:
            self.target = target
            try:
                self.file = open(target, 'w')
            except Exception, e:
                print str(e)
                print '\n'

    def run(self):
        while True:
            buffer = self.proc.stdout.readline()
            if len(buffer) == 0:
                #print 'read end'
                print_t('read end')
                #print '\n'
                break
            if buffer.startswith('\r\n'):
                continue
            buffer = buffer.replace("\r\n", "")
            #print buffer
            if self.file == None:
                print buffer
            else:
                self.file.write(buffer)

    def time_out(self, out):
        pass


class SelfProcess:
    proc_cnt = 0
    
    def __init__(self, sProcName, nTimeOut):
        print_t(sProcName)
        #print '\n'
        temp = sProcName.split('>')
        #print temp
        #print temp[0]

        self.sProcName = sProcName
        self.nTimeOut = nTimeOut
        #stdout = subprocess.PIPE表示子进程的标准输出会被重定向到特定管道，这样父进程和子进程就可以通讯了
        #如果shell = True，表示目录执行程序，由Shell进程调起。
        #中间会产生以下流程:创建shell(cmd)进程，shell(cmd)进程创建目标进程。这样的话，目标进程是本进程的孙子进程，而不是子进程
        self.proc = subprocess.Popen(temp[0], stdout = subprocess.PIPE, shell = False)
        if self.proc != None and self.nTimeOut != None:
            t1 = timeOutThread(self, self.nTimeOut)
            t1.start()
        target =None
        if len(temp) == 2:
            target = temp[1].replace(" ", "")
        #print target
        if self.proc != None:
            t2 = redirecThread(self.proc, target)
            t2.start()

    def terminate(self):
        if self.proc != None and self.proc.poll() == None:
            print_t('terminate')
            #print '\n'
            self.proc.terminate()

if __name__ == '__main__':
    proc = SelfProcess("adb logcat -v time > yzs", 10)
