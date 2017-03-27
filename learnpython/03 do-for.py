# -*- coding: utf-8 -*-b

#range 可以生成整数序列，如果要生成浮点型序列，用什么方式
a=range(10)
print(a)

b=[i/10.0 for i in range(10)]
print(b)

#1-100求和
summ=0
for i in range(101):
	summ=summ+i
print(summ)

#采用do-while的方式
summ=0
i=1
while i<=100:
	summ=summ+i
	i=i+1
print(summ)

#break 退出循环
summ=0
i=1
while i<=100:
	if i>10:
		break #退出循环
	summ=summ+i
	i=i+1
print(summ)


#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
summ=0
i=1
while i<=100:
	if i>10:
		continue #退出循环
	i=i+1
	print(i)