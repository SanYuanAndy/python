#coding=utf-8
import multiprocessing
import time
import os

#子进程
def worker(interval):
    os.system("cmd")

flag = True

if __name__ == "__main__":
    while flag:
        p = multiprocessing.Process(target = worker, name = "worker", args = (2,))
        p.start()
        time.sleep(3)
        print p.is_alive()
        if p.is_alive():
            print "terminate : " + p.name
            p.terminate()
        print p.is_alive()
        time.sleep(5)
    print "Main Process exit"
    
