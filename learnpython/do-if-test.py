# -*- coding: utf-8 -*-
height = input('说一下身高吧（m为单位）：') 
weight = input('说下体重哦，不会和别人说的么么哒（kg为单位哦）：')
h=float(height) 
 w=float(weight) 
 bim= w/(h*h) 
 if bim>=32: 
 	print('哇！你严重肥胖啦！去看一下医生吧：）') 
 elif bim>=28: 
 	print('你现在是肥胖哦') 
 elif bim>=25: 
 	print('你体重过重啦') 
 elif bim>=18.5: 
 	print('你的体重很正常，好好保持哦！')
 else : 
 	 print('你真的太轻了惹')