#coding=utf8
import os

def getProcessIdByName(sName):
    pid = '0'
    cmd = 'adb shell "ps|grep %s"'%(sName)
    #print cmd
    results = os.popen(cmd).readlines()
    for result in results:
        result = result.replace('\r\n', '')
        if result.endswith(sName):
            pid = result.split(' ')[4]
            
    return pid

def killProcssById(procId):
    cmd = 'adb shell kill %s'%(procId)
    os.system(cmd)
    
#pid = getProcessIdByName('com.ls.bluetooth.service')
pid = getProcessIdByName('com.txznet.txz')
print pid

killProcssById(pid)
