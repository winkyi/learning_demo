# -*- coding: utf-8 -*-
__time__ = '2018/3/8 16:38'
__author__ = 'winkyi@163.com'

import ConfigParser
class myconf(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr
conf=ConfigParser.ConfigParser()
conf.read("db.conf")
print conf.sections()
for  i in conf.sections():
    print conf.options(i)
    for option in  conf.options(i):
        print option,conf.get(i,option)
conf=myconf()
conf.read("db.conf")
print conf.sections()
for  i in conf.sections():
    print conf.options(i)
    for option in  conf.options(i):
        print option,conf.get(i,option)
