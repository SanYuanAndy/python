#coding=utf8
import subprocess
import time
import threading
import sys
import Queue
from syutil import print_t
from syutil import print_n

class SelfProcess:   
    def __init__(self, sProcName):
        self.sProcName = sProcName
        #stdout = subprocess.PIPE表示子进程的标准输出会被重定向到特定管道，这样父进程和子进程就可以通讯了
        #如果shell = True，表示目录执行程序，由Shell进程调起。
        #中间会产生以下流程:创建shell(cmd)进程，shell(cmd)进程创建目标进程。这样的话，目标进程是本进程的孙子进程，而不是子进程
        #可以推测，cmd窗口中命令行输出重定向到文件，应该也是这种实现方式
        self.proc = subprocess.Popen(self.sProcName, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell = False)

    def terminate(self):
        if self.isAlive():
            self.proc.terminate()
            
    def write(self, strInput):
        if self.isAlive():
            self.proc.stdin.write(strInput)
            
    def read(self):
        if self.isAlive():
            self.proc.stdout.read(1)
            
    def isAlive(self):
        if self.proc != None and self.proc.poll() == None:
            return True
        else:
            return False

class SqliteHelper:
    proc = None
    def __init__(self, sDBName, sTableName, itemName):
        sSubCmd = '%s %s'%('sqlite3', sDBName)
        self.proc = SelfProcss(sSubCmd)
        sCmd = 'create table %s (%s TEXT);\n'%(sTableName, itemName)
        print sCmd
        self.proc.write(sCmd)

    def addItem(self, sTableName, sItem):
        if self.proc and self.proc.isAlive():
            sCmd = 'insert into %s values(%s);\n'%(sTableName, sItem)
            print sCmd
            self.proc.write(sCmd)

if __name__ == '__main__':
    helper
