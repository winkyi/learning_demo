# -*- coding: utf-8 -*-
__time__ = '2018/2/14 14:52'
__author__ = 'winkyi@163.com'


"""
装饰器类的网址：
http://python.jobbole.com/85056/
"""

a_string = "This is a global variable"

def foo():
    a = 5
    print locals()

print globals()
foo()


print "----------------------"
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def apply(func,x,y):
    return func(x,y)

print apply(add,2,1)
print apply(sub,2,1)

print "-----------------------"
#装饰器实例1
def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func()
        print ret + 1
    return inner

def foo():
    return 1
decorated = outer(foo)
decorated()


print "-----------------------"
#装饰器实例2

class Coordinate(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


def add(a,b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a,b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)

print sub(one,two)
print add(one,three)

print "----------------------------------------"

def wrapper(func):
    def checker(a, b): # 1
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
            return ret
    return checker

add = wrapper(add)
sub = wrapper(sub)
print sub(one, two)
print add(one, three)