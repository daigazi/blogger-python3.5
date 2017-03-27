#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，
还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，
不但能处理复杂的参数，还可以简化调用者的代码。
'''

#位置参数
import math

def power(x):  #x就是位置参数
	return x**2 
   
   
#如果要求x的3次方

def power(x,n): #x和n都是位置参数
	return x**n 


#默认参数

def power(x,n=2): #n的默认参数是2
	return x**n 

'''
从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
'''
print(power(3))

#print(power(n=3,5))  #SyntaxError: non-keyword arg after keyword arg

#默认参数必须指向不变对象！

def nonkey(l=[]):
	l.append("end")
	return l
print(nonkey(l=[1,23]))

#后面跟了一个end
print(nonkey())
#发现又叠加了一个end
print(nonkey())

#这是因为list是一个可变对象，并且l还不是局域变量，是一个全局变量的形式，每计算一次
#l就追加了end。

#可变参数

def calc(numbers):
	summ=0
	for n in numbers:
		summ=summ+n*n
	return summ
    

#组装一个list或者tuple
a_list=[1,2,3,4]
print(calc(a_list))

b_tuple=(1,2,3)
print(calc(b_tuple))


#如果把参数改成可变参数
def calc(*numbers):
	summ=0
	for n in numbers:
		summ=summ+n*n
	return summ

print(calc(1,23,4)) #不需要是list或者tuple了
print(calc(*a_list))  #list或者tuple只需要在变量前加*就可以
print(calc())  #计算0个参数


#关键字参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
请看示例：

'''
def person(name,age,**kw):
	print("name:",name,"age:",age,"others:",kw)
print(person("dai","29",wife="liu"))
print(person("dai","29",wife="liu",city="putian"))
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数

#限制关键字参数只能是city和wife两个

def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'wife' in kw:
		pass
	print("name:",name,"age:",age,"others:",kw)


person('Jack', 24, city=extra['city'], job=extra['job'])
#还是没有限制住，想要限制的话，采用如下形式 

def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city=extra['city'], job=extra['job'])



#参数组合


#小结