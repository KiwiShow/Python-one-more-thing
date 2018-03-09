#!/usr/bin/env python
# -*- coding: utf-8 -*-
# multiprocessing01.py
# Python在Mac平台上测试OS模块中fork()功能
# 20170107
import os

print('Process {} start...'.format(os.getpid()))

pid = os.fork()

# 先执行else在执行if
# 因为fork()返回2次，第一次在父进程中返回子进程的ID，pid即是子进程的ID，os.getpid()为父进程的ID；
# 第二次在子进程中返回0，即pid为0，os.getpid()为子进程的ID。
#
if pid == 0:
    print('I am a child process {} and my parent process is {}.'.format(os.getpid(), os.getppid()))  # 注意pid和ppid的区别。

else:
    print('I {} just creat a child process {}.'.format(os.getpid(), pid))
