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
        self.proc_exited = False
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
        if not self.proc_exited:
            print_n('>')
        if self.file != None:
            try:
                self.file.close()
                self.file = None
            except Exception, e:
                pass

    def print_cache(self, content):
        if not self.proc.enable_print:
            return
        #两种可能不抛异常:1、不含中文。2、含中文、但是中文编码是utf8
        try:
            content = content.decode('utf8').encode('gbk')
        except Exception, e:
            pass
        if self.file != None:
            self.file.write(content)
        else:
            print_n(content)

    def proc_wait(self):
        pass
        self.proc_exited = True

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
                    pass
                    #print_t(ret)
                    #continue
                self.proc.msg_queue.put(buffer)
                break
            self.proc.msg_queue.put(buffer)


class SelfProcess:
    proc_cnt = 0
    
    def __init__(self, sProcName, nTimeOut):
        temp = sProcName.split('>')
        self.sProcName = sProcName
        self.nTimeOut = nTimeOut
        self.enable_print = True
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
            self.t1 = readThread(self, target)
            self.t1.start()
            self.t2 = writeThread(self, target)
            self.t2.start()
    
    def disable_print(self):
        self.enable_print = False

    def terminate(self):
        if self.isAlive():
            self.proc.terminate()
    def wait(self):
        if self.isAlive():
            self.t2.proc_wait()
            self.t1.join(5)
            self.t2.join(5)
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
