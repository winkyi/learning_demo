# -*- coding: utf-8 -*-
__time__ = '2018/2/14 14:47'
__author__ = 'winkyi@163.com'

"""
使用闭包的过程中，一旦外函数被调用一次返回了内函数的引用，虽然每次调用内函数，
是开启一个函数执行过后消亡，但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量
"""
#coding:utf8
# def outer(x):
#     def inner(y):
#         # nonlocal x
#         # x+=y
#         # return x
#     return inner
#
#
# a = outer(10)
# print(a(1)) //11
# print(a(3)) //14