#coding=utf-8
import os

def calculate_file_size(f_path, root):
    size = 0
    cmd = "adb shell ls -l -a %s"%(f_path)
    p = os.popen(cmd)
    cmd_results = p.readlines()
    for line in cmd_results:
        temp = line.replace("\r\n", "").split(" ")
        #print temp
        result = []
        for s in temp:
            if len(s) == 0:
                continue
            result.append(s)
        #print result
        if result[0].startswith('-') and len(result) >= 7:
            file_path = "%s/%s"%(f_path, result[6])
            file_size = int (result[3])
            if f_path == root :
                print "%s:%d"%(file_path, file_size)
            size = size + file_size
        elif result[0].startswith('d'):
            #print -1
            sub_path = "%s/%s"%(f_path, result[5])
            #print sub_path
            dir_size = calculate_file_size(sub_path, root)
            if f_path == root :
                print "%s:%d"%(sub_path, dir_size)
            size = size + dir_size
    return size
            
            
f = "/sdcard/Android/data"#该路径改成需要查看的大小的路径

total_size = calculate_file_size(f, f)
print "mem total:"
print "%dbyte"%(total_size)
print "%dM"%(total_size/1024/1024)

