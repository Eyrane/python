#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
内置模块、自定义模块、第三方模块
'''
#本文件自定义一个模块test6，该模块必须以.py为文件名，调用模块时要import test6


'module test' #任何模块代码的第一个字符串都被视为模块的文档注释
_author_ = 'Eyrane'  #_author_声明作者

#以下为模块的代码
import sys
def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

def add(a, b):
	return a+b


#在命令行运行本模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该模块时，if判断将失败
#即直接运行本文件时，if成立；把本文件当中模块使用时，if不成立
if __name__=='__main__':  
	test()
	print add(2,3)
	
def printadd( a ):
	a+=[1,2,3]
	return a