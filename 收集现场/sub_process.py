#coding=utf8
import subprocess
import time
import thread

def time_out(proc, timetout):
    time.sleep(timetout)
    proc.terminate()

class SelfProcess:
    proc_cnt = 0
    
    def __init__(self, sProcName, nTimeOut):
        self.sProcName = sProcName
        self.nTimeOut = nTimeOut
        self.proc = subprocess.Popen(sProcName, stdin = subprocess.PIPE, stdout=subprocess.PIPE, shell = False)
        if self.proc != None:
            thread.start_new_thread(time_out, (self, nTimeOut,))

    def terminate(self):
        if self.proc != None and self.proc.poll() == None:
            print 'terminate'
            #self.proc.terminate()
            self.proc.kill()

if __name__ == '__main__':
    proc = SelfProcess("adb shell top", 5)
