# -*- coding: utf-8 -*-
__time__ = '2018/2/24 11:12'
__author__ = 'winkyi@163.com'


import  threading
import time

def action(arg):
    time.sleep(2)
    print 'the arg is:%s' %arg

for i in range(10):
    t = threading.Thread(target=action,args=(i,))
    t.start()

print 'main thread end!'