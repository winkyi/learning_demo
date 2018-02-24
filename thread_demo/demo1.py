# -*- coding: utf-8 -*-
__time__ = '2018/2/24 14:18'
__author__ = 'winkyi@163.com'
import time,threading


"""
join的用法
设置join之后，主线程等待子线程全部执行完成后或者子线程超时后，主线程才结束
"""
def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s,args is %s \n' % (threading.currentThread().getName(),arg)
    time.sleep(1)

thread_list = []    #线程存放列表
for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print 'main thread end!'
print "----------------------------------"

"""
以下为多线程join不妥当的用法，使多线程编程顺序执行
"""

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    t.start()
    t.join()

print 'main_thread end!'