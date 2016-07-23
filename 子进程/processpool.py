#coding=utf-8
import multiprocessing
import time
import os

#子进程
def worker(interval):
    os.system("ping www.baidu.com")

flag = True

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 1)
    pool.apply_async(worker, (1,))
    time.sleep(3)
    pool.terminate()
    print "Main Process exit"
    
