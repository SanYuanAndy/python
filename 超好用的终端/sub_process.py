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
        buffer = ""
        line = ""
        while True:
            #buffer = self.proc.stdout.readline()#直到读到换行符才会返回
            #self.proc.stdout.read()#读到结束符才返回
            #self.proc.stdout.read(count)#读到count个字节才返回
            buffer = "%s%s"%(buffer, self.proc.stdout.read(1))
            if len(buffer) == 0:
                #print_t('read end')
                break
            out_encode = sys.stdout.encoding
            #中文符号单个字节解码失败，需要缓存下来
            tem_buf = ""
            errCnt = 0
            try:
                tem_buf = buffer.decode('utf8').encode(out_encode)
            except Exception, e:
                errCnt += 1
                #continue
            try:
                tem_buf = buffer.decode('gbk').encode(out_encode)
            except Exception, e:
                errCnt += 1
                #continue
            if errCnt == 2:
                continue

            #print buffer#会换行
            if self.file == None:
                sys.stdout.write(buffer)#不会换行
                sys.stdout.flush()#立即显示

            line = "%s%s"%(line, buffer)
            buffer = ""
            if line.endswith("\r\n"):
                #print_t("%s%s"%("[M]", line))
                if not line.startswith('\r\n'):
                    line = line.replace("\r\n", "")
                    if self.file != None:
                        self.file.write(line)

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
        #可以推测，cmd窗口中命令行输出重定向到文件，应该也是这种实现方式
        self.proc = subprocess.Popen(temp[0], stdout = subprocess.PIPE, shell = False)
        #self.proc = subprocess.Popen(temp[0], stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell = False)
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
            #print_t('terminate')
            #print '\n'
            self.proc.terminate()
    def wait(self):
        if self.proc != None and self.proc.poll() == None:
            self.proc.wait()

if __name__ == '__main__':
    proc = SelfProcess("adb logcat -v time > yzs", 10)
