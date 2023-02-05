# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:05:40 2023

@author: This Pc
"""

#Different Data Types 
print(20)
print(12.5)
print(3+2j)
print("Auwal")
print(type(True))
print(['a','b','c'])
print({'Name':'Auwal',
       'Country':'Nigeria',
       'Age':'26',
       'career':'Data Science'})
print((1,2,3,4))
print({'hausa','igbo','yoruba'})

#Euclidean distance of (2,3) and (10,8)
x1=2
x2=10
y1=3
y2=8

import math
d= math.sqrt((x1-y1)**2+(x2-y2)**2)
print('the euclidean distance is:')
print(d)