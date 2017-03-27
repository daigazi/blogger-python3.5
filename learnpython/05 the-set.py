# -*- coding: utf-8 -*-b


#s=set[1,2,3,2,34],这种写法会报错，需要用set(list)的形式
s=set([1,2,3,2,34])
print(s)

#发现重复元素被过滤掉了
'''
set和dict都是一组key的集合，但是不存储value，上面的1、2、3、34是key，由于
key是不能重复的，所以上述的重复元素就被过滤了。那么set的用处是什么呢？
'''

#添加新元素
s.add(5)
print(s)
s.add(34)
print(s) #重复元素过滤掉了

#remove方法删除元素

s.remove(34)
print(s)

#set可以看成是数学上的无序和无重复元素的集合，可以实现数学意义上的并集和交集
s1=set([1,2,3])
s2=set([2,3,5])
print(s1&s2)
print(s1|s2)