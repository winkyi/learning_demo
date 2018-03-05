# -*- coding: utf-8 -*-
__time__ = '2018/2/27 16:33'
__author__ = 'winkyi@163.com'

from optparse import OptionParser

parser = OptionParser()


parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")


parser.add_option("-f", "--file",
                  action="store", type="string", dest="filename")


parser.add_option("-s","--GET",action="store",dest="show_status",help=u"获取node、server等相关参数")



"""
判断参数是否正确
"""
"""
if parser.has_option('-f'):
    print('content -f')
    parser.set_default('-f', 'myFile')
    # parser.remove_option('-f')

if not parser.has_option('-f'):
    print('do not content -f')

"""
(options, args) = parser.parse_args()

if options.filename:
    print('file in args : %s' % options.filename)

if parser.has_option("-s"):
    pass

print type(options.show_status)
print args
