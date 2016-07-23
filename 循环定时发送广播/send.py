#coding=utf-8
import os
import time
import Tkinter
from Tkinter import *

action = "com.txznet.alldemo.intent.action.cmd"
tag = "cmd"
cmd = "trigger_button"
txzProcessName = "com.txznet.txz"

def sendCmd(action, tag, cmd):
    cmdline = "adb shell am broadcast -a %s --es %s %s"%(action, tag, cmd)
    #没有返回值
    os.system(cmdline)

def sendCmdWithCheck(action, tag, cmd):
    cmdline = "adb shell am broadcast -a %s --es %s %s"%(action, tag, cmd)
    pipe = os.popen(cmdline)
    #有返回值，返回的值寸在列表中,并且包含了换行符\r\n
    #print pipe.readlines()
    
def getPidByProcessName(name):
    cmdline = "adb shell ps"
    pipe = os.popen(cmdline)
    result = pipe.readlines();
    for strLine in result:
        line = strLine.replace("\r\n", "")
        if line.endswith(name):
           fields = line.split(" ")
           while fields.count('') > 0 :
               fields.remove('')
           return fields[1]
    return 0

def alert(alert):
    top = Tkinter.Tk()
    top.title("警告!!!")
    display = Text(top)
    display.insert(INSERT, alert)
    display.pack()
    top.mainloop()
    
origin_pid = getPidByProcessName(txzProcessName)  
print "origin pid : " +  origin_pid

while True:
    if getPidByProcessName(txzProcessName) == origin_pid:
        sendCmdWithCheck(action, tag, cmd)
        time.sleep(100)
    else:
        strAlert = "%s maybe happened crash!!!"%(txzProcessName)
        print strAlert
        alert(strAlert)
        time.sleep(120)
        break
    
