# -*- coding: utf-8 -*-
__time__ = '2018/3/1 14:56'
__author__ = 'winkyi@163.com'


class User(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age





if __name__ == '__main__':
    u = User('AA',19)
    print u.age
    print u.name
    u.name = "BB"
    print u.name