#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_abs(x):
	if x>0:
		return x
	else:
		return -x

print(my_abs(-9))

#空函数
def  none(x):
	pass

print(none(1))

#参数检查
#看一下原先我们编写的函数，如果输入两个参数的时候，会报错
print(my_abs(1,2)) #my_abs() takes exactly 1 argument (2 given)
my-abs("a")
#查看下python自带的abs函数报错结果

#abs(1,2) #abs() takes exactly one argument (2 given)
abs("a") #bad operand type for abs(): 'str'

#说明自带的abs函数有参数类型检查，仿造，可以更改我们的函数

def my_abs(x):
	if not isinstance (x,(int,float)):
		raise TypeError ('bad operand type')
	if x>0:
		return x
	else:
		return -x

my_abs("a")