#coding=utf-8
import os
import time
import Tkinter
from Tkinter import *

tag = "cmd"
cmd = "trigger_button"
txzProcessName = "com.txznet.txz" 
def getPidByProcessName(name):
    cmdline = "adb shell ps"
    pipe = os.popen(cmdline)
    result = pipe.readlines();
    if len(result) == 0 or not result[0].find("PID"):
        return "-1"
    for strLine in result:
        line = strLine.replace("\r\n", "")
        if line.endswith(name):
           fields = line.split(" ")
           while fields.count('') > 0 :
               fields.remove('')
           return fields[1]
    return "0"

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
    now_pid = getPidByProcessName(txzProcessName)
    if now_pid == "-1":
        strAlert = "adb maybe offline, please try make adb sure again !!!"
        print strAlert
        alert(strAlert)
        time.sleep(30)
    elif now_pid == origin_pid:
        time.sleep(0.5)
    else:
        strAlert = "%s maybe happened crash!!!"%(txzProcessName)
        print strAlert
        alert(strAlert)
        time.sleep(30)   
