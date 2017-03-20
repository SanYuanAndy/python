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
#parse_text_cmd = '''adb shell am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd "parse_text" --es text_args fuck you'''
#os.system(parse_text_cmd)
print code.gbk('输入exit退出')
while True:
    try:
        strInput = raw_input(code.gbk("请输入要识别的文本:"))
    except Exception, e:
        print repr(e)

    if strInput == 'exit':
        break
    cmd = "adb shell"
    proc_cmd = "am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd parse_text --es text_args %s"%(strInput)
    proc_cmd = code.utf8(proc_cmd)
    proc = syos.SelfProcess(cmd, None)
    proc.disable_print()
    proc.write("%s%s"%(proc_cmd, "\n"))
    proc.write("%s%s"%('exit', "\n"))
    #time.sleep(1)
    #proc.terminate()
    proc.wait()
    
