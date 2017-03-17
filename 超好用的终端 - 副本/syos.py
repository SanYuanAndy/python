#coding=utf8
import subprocess
import time
import threading
import sys
import Queue
from syutil import print_t
from syutil import print_n

class writeThread(threading.Thread):
    def __init__(self, proc, target):
        threading.Thread.__init__(self)
        self.proc = proc
        self.target = target
        self.file = None
        if target != None and len(target)!= 0:
            self.target = target
            try:
                self.file = open(self.target, 'w')
            except Exception, e:
                print_t(str(e))
    def run(self):
        buf = ''
        while True:
            if self.proc.msg_queue.empty():
                if len(buf) != 0:
                    self.print_cache(buf)
                    buf = ''
            msg = self.proc.msg_queue.get()
            buf = "%s%s"%(buf, msg)
            if len(msg) == 0:
                self.print_cache(buf)#输出缓存数据
                buf = ''
                break
        print_n('write end')
    def print_cache(self, content):
        try:
            content = content.decode('utf8').encode('gbk')
        except Exception, e:
            pass
        print_n(content)



class readThread(threading.Thread):
    def __init__(self, proc, target):
        threading.Thread.__init__(self)
        self.proc = proc

    def run(self):
        buffer = ""
        while True:
            #buffer = self.proc.stdout.readline()#直到读到换行符才会返回
            #self.proc.stdout.read()#读到结束符才返回
            #self.proc.stdout.read(count)#读到count个字节才返回

            buffer = self.proc.proc.stdout.read(1)
            if len(buffer) == 0:
                ret = self.proc.isAlive()
                if ret:
                    print_t(ret)
                    #continue
                self.proc.msg_queue.put(buffer)
                break
            self.proc.msg_queue.put(buffer)
        print_t("exit readThread")


class SelfProcess:
    proc_cnt = 0
    
    def __init__(self, sProcName, nTimeOut):
        temp = sProcName.split('>')
        self.sProcName = sProcName
        self.nTimeOut = nTimeOut
        #stdout = subprocess.PIPE表示子进程的标准输出会被重定向到特定管道，这样父进程和子进程就可以通讯了
        #如果shell = True，表示目录执行程序，由Shell进程调起。
        #中间会产生以下流程:创建shell(cmd)进程，shell(cmd)进程创建目标进程。这样的话，目标进程是本进程的孙子进程，而不是子进程
        #可以推测，cmd窗口中命令行输出重定向到文件，应该也是这种实现方式
        self.proc = subprocess.Popen(temp[0], stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell = False)
        target =None
        if len(temp) == 2:
            target = temp[1].replace(" ", "")
        #print target
        if self.proc != None:
            self.msg_queue = Queue.Queue()
            t1 = readThread(self, target)
            t1.start()
            t2 = writeThread(self, target)
            t2.start()

    def terminate(self):
        if self.isAlive():
            self.proc.terminate()
    def wait(self):
        if self.isAlive():
            self.proc.wait()
    def write(self, strInput):
        if self.isAlive():
            self.proc.stdin.write(strInput)
    def isAlive(self):
        if self.proc != None and self.proc.poll() == None:
            return True
        else:
            return False


if __name__ == '__main__':
    proc = SelfProcess("adb logcat -v time > yzs", 10)
