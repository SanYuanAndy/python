#coding=utf-8
import os

def filter_empty_str_in_list(temp):
    result = []
    for s in temp:
        if len(s) == 0:
            continue
        result.append(s)
    return result

def get_solib_path(pid):
    cmd_shell = "cat /proc/%s/maps | grep %s"%(pid, "/data/data/com.txznet.txz/solibs/") 
    cmd_line = 'adb shell ' + '"' + cmd_shell + '"'
    p = os.popen(cmd_line)
    cmd_results = p.readlines()
    if len(cmd_results) > 0:
        temp = cmd_results[0].replace("\r\n", "").split(" ")
        result = filter_empty_str_in_list(temp)
        return result[len(result) - 1]
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
            processInfo['solib_path'] = get_solib_path(process[1])
            allProcess.append(processInfo)
    return allProcess

def printAllProcess(allProcess):
    print_format = '%-*s%-*s%-*s'
    info = print_format%(8, 'pid', 30, 'proc_name', 4, 'solibs_path')
    print info
    for proc in allProcess:
        info = print_format%(8, proc['pid'], 30, proc['name'], 4, proc['solib_path'])
        print info
    
allProcess = getAllProcess("com.txznet.txz")
printAllProcess(allProcess)

