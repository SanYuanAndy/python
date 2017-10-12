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


proc_cmd = 'adb shell am broadcast -a com.txznet.alldemo.intent.action.cmd --es cmd %s'%('trigger_button')
cnt = 0
while True:
    os.system(proc_cmd)
    time.sleep(12)
