# -*- coding: utf-8 -*-
__time__ = '2018/2/14 10:05'
__author__ = 'winkyi@163.com'

import multiprocessing

def do(n) :
    #获取当前线程的名字
    name = multiprocessing.current_process().name
    print name,'starting'
    print "worker ", n
    return

if __name__ == '__main__' :
    numList = []
    for i in xrange(5) :
        p = multiprocessing.Process(target=do, args=(i,))
        numList.append(p)
        p.start()
        p.join()
        print "Process end."
