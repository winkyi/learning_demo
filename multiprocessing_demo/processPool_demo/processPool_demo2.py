# -*- coding: utf-8 -*-
__time__ = '2018/2/14 10:23'
__author__ = 'winkyi@163.com'


import multiprocessing
import time

def func(msg):
    print "*msg: ", msg
    time.sleep(3)
    print "*end"
    return "{} return".format(msg)

if __name__ == "__main__":
	# 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    pool = multiprocessing.Pool(processes=3)
    result = []
    for i in range(10):
        msg = "hello [{}]".format(i)
        # pool.apply(func, (msg,))
        res = pool.apply_async(func, (msg,)) # 异步开启进程, 非阻塞型, 能够向池中添加进程而不等待其执行完毕就能再次执行循环
        result.append(res)
    print "--" * 10
    pool.close() # 关闭pool, 则不会有新的进程添加进去
    pool.join() # 必须在join之前close, 然后join等待pool中所有的线程执行完毕
    print "All process done."

    print "Return results: "
    for i in result:
        print i.get() # 获得进程的执行结果
