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
while True:
    try:
        strInput = raw_input(code.gbk(prompt))
    except Exception, e:
        print repr(e)

    if strInput == 'exit':
        break
    item = -1
    try:
        item = int(strInput)
    except Exception,e:
        continue
    if not (item >= 0 and item < len(func)):
        continue
    while True:
        try:
            strInput = raw_input(code.gbk(func[item]["prompt"]))
        except Exception, e:
            print repr(e)

        if strInput == 'exit':
            break
        cmd = "adb shell"
        proc_cmd = "am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd %s --es text_args %s"%(func[item]["cmd"],strInput)
        proc_cmd = code.utf8(proc_cmd)
        proc = syos.SelfProcess(cmd, None)
        proc.disable_print()
        proc.write("%s%s"%(proc_cmd, "\n"))
        proc.write("%s%s"%('exit', "\n"))
        #time.sleep(1)
        #proc.terminate()
        proc.wait()
    
