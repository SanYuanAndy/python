#coding=utf-8
import multiprocessing
import time
import os

#子进程
def worker(interval):
    #os.system("cmd")
    time.sleep(5)
    
flag = True

if __name__ == "__main__":
    count = 0
    while flag:
        count = count + 1
        if count > 5:
            break
        p = multiprocessing.Process(target = worker, name = "worker", args = (2,))
        p.start()
        time.sleep(3)
        print p.is_alive()
        if p.is_alive():
            print "terminate : " + p.name
            p.terminate()
            p.join()
        #time.sleep(2)
        print p.is_alive()
    print "Main Process exit"
    
