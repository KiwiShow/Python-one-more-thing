#!/usr/bin/env python
# -*- coding: utf-8 -*-
# poolinprocess.py
# Python在Mac平台上测试进程池功能
# 20170108
# 测试有问题，打开Pool时失败（解决）
# 终于知道为什么失败，因为pythoncode文件夹中有一个multiprocessing.py文件，
# 这个路径是优先搜索的，但是匹配到之后发现没有Pool.py所以会报错
# 之后改完名之后发现还不行，再排查，发现还有一个multiprocessing.pyc文件残留删除之，搞定
# ------------注意.pyc文件-------------
# ------------注意不要命名与标准库重名的文件名-------------
# 

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    # 注意apply_async函数是异步执行，相当于for...in...中4个函数依次执行，但是执行下一个不需要等待上一个执行完
    # 又因为sleep的时间比较长，所以先输出了'waiting...'
    #
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
