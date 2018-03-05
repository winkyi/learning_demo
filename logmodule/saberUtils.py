# -*- coding: utf-8 -*-
__time__ = '2018/3/2 09:58'
__author__ = 'winkyi@163.com'

import platform


#判断系统是否为linux
def isLinux():
     if platform.system() == 'Linux':
          return True
     else:
          return False