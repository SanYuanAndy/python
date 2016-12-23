#coding=utf-8
import os

def getOOM_ADJ(pid):
    cmd_line = "adb shell cat /proc/%s/oom_adj"%(pid)
    p = os.popen(cmd_line)
    cmd_results = p.readlines()
    if len(cmd_results) > 0:
        return cmd_results[0].replace("\r\n", "")
    return

def getAllProcess(processName):
    cmd_ps = "adb shell ps"
    p = os.popen(cmd_ps)
    cmd_results = p.readlines()
    p.close()
    allProcess = []
    if len(cmd_results) < 2:
        return allProcess
        
    for i in range(1,len(cmd_results)):
        result_line = cmd_results[i].replace("\r\n", "")
        if result_line.find(processName) != -1:
            temp = result_line.split(" ")
            process = []
            for s in temp:
                if len(s) == 0:
                    continue
                process.append(s)

            processInfo = {}
            processInfo['name'] = process[len(process) - 1]
            processInfo['pid'] = process[1]
            processInfo['oom_adj'] = getOOM_ADJ(process[1])
            allProcess.append(processInfo)
    return allProcess

def printAllProcess(allProcess):
    print_format = '%-*s%-*s%-*s'
    info = print_format%(8, 'pid', 30, 'proc_name', 4, 'oom_adj')
    print info
    for proc in allProcess:
        #info = "%s %s %s"%(proc['pid'], proc['name'], proc['oom_adj'])
        info = print_format%(8, proc['pid'], 30, proc['name'], 4, proc['oom_adj'])
        print info
    
allProcess = getAllProcess("com.txznet.")
printAllProcess(allProcess)

