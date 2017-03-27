#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	if not isinstance (a,(int,float)) |  isinstance (b,(int,float)) | isinstance (c,(int,float)):
		raise TypeError("bad operated type")
	tmp1=b**2-4*a*c
        if tmp1>0:
             return '%.04f'%float((-b+sqrt(tmp1))/(2*a)),'%.04f'%((-b-sqrt(tmp1))/(2*a))
        elif tmp1==0:
            return -b/(2*a)
        else:
            return 'No rational answer!'

print(quadratic(1,2,1))

print(help(isinstance))