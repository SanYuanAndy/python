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

strAction = "com.txznet.userconf.update"
extraTag = "json_conf"
extraContent = '''
{
"wakeup.threshhold.value":-3.5,
"wakeup.words":["你好小贱", "你好小狗"],
"wakeup.enable":true,
"device.welcome.msg":"么么哒"
}
'''
#
def sendBroadcast(strBroadcast):
    cmd = "adb shell"
    proc_cmd = strBroadcast
    #proc_cmd = code.utf8(proc_cmd)
    proc = syos.SelfProcess(cmd, None)
    proc.disable_print()
    proc.write("%s%s"%(proc_cmd, "\n"))
    proc.write("%s%s"%('exit', "\n"))
    proc.wait()
    
strBroadcast = 'am broadcast -a %s --es %s "%s"'%(strAction, extraTag, extraContent)

#print strBroadcast
sendBroadcast(strBroadcast)

    
    
