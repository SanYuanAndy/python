#coding=utf8
import threading
import time
import os
import sys
import signal
import syos
import re
import code
from syutil import parse_path
from syutil import del_dir
from syutil import format_time
from syutil import print_t
from syutil import print_n

#cmd = "adb shell am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd parse_text --es text_args 播放刘德华的暗里着迷"
######直接使用os.system(cmd)方式有些中文编码转换的时候还是有问题，比如“暗里着迷”、“你好的”
#parse_text_cmd = 'adb shell am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd "parse_text" --es text_args 播放暗里着迷'
#os.system(parse_text_cmd)
#####test######
func = []
func.append({"index":0, "cmd":"parse_text", "prompt":"请输入要识别的文本:"})
func.append({"index":1, "cmd":"speak_text", "prompt":"请输入要播放的文本:"})

prompt ='''********************
[0]文本识别    
[1]文本播报
********************
请选择功能(输入exit退出):'''
def play(strInput):
    item = 0
    cmd = "adb shell"
    proc_cmd = 'am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd %s --es text_args "%s"'%(func[item]["cmd"],strInput)
    #print code.gbk(proc_cmd)
    #proc_cmd = code.utf8(proc_cmd)
    proc = syos.SelfProcess(cmd, None)
    proc.disable_print()
    proc.write("%s%s"%(proc_cmd, "\n"))
    proc.write("%s%s"%('exit', "\n"))
    #time.sleep(1)
    #proc.terminate()
    proc.wait()

def now_time():
    return time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
    
def printMemInfo(f):
    proc_cmd = '''adb shell "dumpsys meminfo|grep com.txznet.txz"'''
    p = os.popen(proc_cmd)
    lines = p.readlines()
    if len(lines)>0:
        print_n(lines[0])

    if f != None:
        try:
            f.write("%s\n"%(now_time()))
            f.write(lines[0])
        except Exception,e:
            print e
    
    
texts = ['关闭音乐', '播放刘德华的十年','播放周杰伦的枫','导航去北京天安门','取消','讲个笑话','关闭蓝牙','打电话给习近平','打电话给10086','取消','再见']
#texts = ['取消']
cnt = 0
total = 0
print total
f = open('mem_%d'%(time.time()), 'wb')
printMemInfo(f)
while True:
    cnt = cnt + 1
    cnt = cnt%len(texts)
    total = total + 1
    play(texts[cnt])
    time.sleep(8)
    if total%5 == 0:
        print total
        printMemInfo(f)
    time.sleep(2)

if f!= None:
    f.close()
    
