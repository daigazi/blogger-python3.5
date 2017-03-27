# -*- coding: utf-8 -*-
# 如果没有加开头这一行的话，注释用中文会报错。
classmates=['dai','wang','liu'] #列表，可随时添加或删除其中的元素
print(classmates)
print(classmates[0]) #第一个，即dai
print(classmates[2]) 
len(classmates) #列表长度

#列表是一个可变的有序列表，可以添加或删除其中的元素。
#不同于R语言，不可以用classmates[3]="xie"这种形式添加第四个元素
# error: classmates[3]="xie"
#添加元素，采用xxx.append
classmates.append('xie')
#删除 xxx.pop(index),插入 xxx.insert(index,"str")
#xxx.pop()默认空白是删除最后一个，即index=len(xxx)-1
#将其中的某一个更换成其他元素，可以采用classmates[0]="xie"

print(classmates)
classmates.insert(1,"liu")
print(classmates)
classmates.pop(2)
#list中可以插入另一个list，比如：
l_plus=["dai","liu",["wang","xie"]]
print(l_plus) #显示结果是['dai', 'liu', ['wang', 'xie']]
lx=["wang","xie"]
l_plus=["dai","liu",lx]  
print(l_plus) #显示结果是['dai', 'liu', ['wang', 'xie']],类似一个二维数组

#tuple

#tuple和list类似，但是一旦初始化之后就不可以修改，用小括号来包含元素

tup=("dai","liu")
#tup.append("wang") #AttributeError: 'tuple' object has no attribute 'append'

#Q1 tuple存在的意义是？
#不可修改，比较安全。

#tuple还可以包含list
tup=("dai",["x","y"])
print(tup)
#list应该也可以包含tuple
ly=["dai",("x","y")]
print(ly)
#python里所含的数据类型有 整数、浮点数、字符串、布尔型、空值None、常量、


x = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(x[0][0])
# 打印Python:
print(x[1][1])
# 打印Lisa:
print(x[2][2])