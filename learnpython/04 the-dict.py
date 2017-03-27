# -*- coding: utf-8 -*-b
'''
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
使用键-值（key-value）存储，具有极快的查找速度。
'''
d={"dai":98,"liu":100}
print(d)
# d[0] 利用这种方式提取第一个元素对，报错
print(d["dai"])
#print(d["wang"]) #不存在就报错

#判断某个key是否存在

"wang" in d
d.get("wamg")
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

d.get("wang",-1)

#删除某个key，采用xxx.pop的方式
d.pop("dai")
print(d)
'''
和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。

而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。
'''
#可以新增键值对吗？
#d={d,"wang":59} 报错
d={"dai":98,"liu":100}
d["wang"]=59
print(d)

#字典可以是二维的
d={
	"x":{
	"a":45,
	"b":54
	},
    "y":{
	"c":55,
	"d":64
	}
}
print(d)
print(d["x"]["a"])

'''
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、
整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''
#也就是说key的对象只能是字符串、整数、浮点型、空值None、常量