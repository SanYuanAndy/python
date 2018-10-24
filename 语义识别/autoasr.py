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
    item = 1
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
texts = []
jok0 = '''
双腿瘫痪后我的脾气变得暴怒无常望着望,
着天上北归的雁阵我会突然把面前的玻璃,
砸碎听着听着李谷一甜美的歌声我会猛地,
把手边的东西摔向四周的墙壁母亲就悄悄,
地躲出去在我看不见的地方偷偷地听着我,
'''
jok1 = '''
的动静当一切恢复沉寂她又悄悄地进来眼,
边红红的看着我听说北海的花儿都开了我,
推着你去走走她总是这么说母亲喜欢花可,
自从我的腿瘫痪以后她侍弄的那些花都死,
'''
jok2 = '''
了不我不去我狠命地捶打这两条可恨的腿,
喊着我可活什么劲儿母亲扑过来抓住我的,
手忍住哭声说咱娘儿俩在一块儿好好儿活,
好好儿活可我却一直都不知道她的病已经。
'''
jok3 = '''
十岁那年我在一次作文比赛中得了第一母亲那时候还年轻急着跟，
说她自己说她小时候的作文作得还要好老师甚至不相信那么好的文章
会是她写的老师找到家来问是不是家里的大人帮了忙我那时，
可能还不到十岁呢我听得扫兴故意笑可能什么叫可能还不。
'''
jok4 = '''
根本不再注意她的话对着墙打乒乓球把她气得够呛不过，
我承认她聪明承认她是世界上长得最好看的女的她正给，
自己做一条蓝底白花的裙，
子二十岁我的两条腿残废了除去给人家画彩蛋我想我还，
应该再干点别的事先后改变了几次主意最后想学写作母亲，
'''
jok5 = '''
再试一回不试你怎么知道会没用她说每一回都虔诚地，
抱着希望然而对我的腿有多少回希望就有多少回失望，
最后一回我的胯上被熏成烫伤医院的，
'''
jok6 = '''
心烦我摇着车躲出去坐在小公园安静的树林里想上帝为什么，
早早地召母亲回去呢迷迷糊糊的我听见回答她心里太苦了，
上帝看她受不住了就召她回去我的心得，
'''
jok7 = '''
西但当时心思全在别处第二年合欢树没有发芽母亲叹息了一回还不舍得扔掉依然让，
它长在瓦盆里第三年合欢树却又长出叶子而且茂盛了母亲高兴了，
很多天以为那是个好兆头常去侍弄它不敢再大意又过一年她，
'''
jok8 = '''
真是不能了家家门前的小厨房都扩大过道窄到一个人推自行车，
进出也要侧身我问起那棵合欢树大伙说年年都开花长到房高了，
这么说我再看不见它了我要是求人，
'''

caipu = '''
五花肉清洗切块,锅里放入少量的油，肉块倒进去翻炒,放入少量料酒，翻炒出香味，大概5.6分钟左右，时间长一点，肥油出的多，不会腻，然后把肉盛出来放进碗里,炒肉留下的油不够可以再放点，然后放入白糖，小火不停搅拌，以免糊锅。待糖完全炒化把肉倒进去,翻炒过后放入葱姜蒜，桂皮，荤香，少量花椒，少量料酒，少量酱油，喜欢吃辣的可以放入几个干辣椒。翻炒3分钟左右，加入水,加水量是肉的四分之三，个人觉得砂锅炖出来的肉更烂,加入水后把煮好的鹌鹑蛋，香菇切条放入锅里，大火煮开，小火慢炖半个小时左右，放入盐，鸡精，然后转大火收汁,肥而不腻的红烧肉出锅啦
'''
'''
texts.append(jok0)
texts.append(jok1)
texts.append(jok2)
texts.append(jok3)
texts.append(jok4)
texts.append(jok5)
texts.append(jok6)
texts.append(jok7)
texts.append(jok8)
'''
texts.append(caipu)

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
    time.sleep(15*3)
    if total%5 == 0:
        print total
        printMemInfo(f)
    time.sleep(2)

if f!= None:
    f.close()
    
