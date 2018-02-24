# -*- coding: utf-8 -*-
__time__ = '2018/2/24 11:12'
__author__ = 'winkyi@163.com'


import  threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s,args is %s \n' % (threading.currentThread().getName(),arg)
    time.sleep(1)

for i in range(10):
    t = threading.Thread(target=action,args=(i,))
    #serDeamon(False)(默认)前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，主线程停止
    # t.setDaemon(True)#设置线程为后台线程
    t.start()

print 'main thread end!'