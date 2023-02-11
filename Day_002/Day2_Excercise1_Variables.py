# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:13:02 2023

@author: This Pc
"""

#Day 2:30 days of python programming
first_name= 'Abubakar'
last_name='Auwal Khalid'
full_name='Auwal Abubakar Khalid'
country='Nigeria'
city='Kaura'
age=150
year=2023
is_married=False
is_true=True
is_light_on=False
print(first_name,last_name,full_name,country,city,age,is_married,is_light_on)

#multiple variale on one line
x,y,z=20,10,5
print(x,y,z)

#Checiking data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(year))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Arithmetic operations
num_one=5
num_two=4

total=num_one+num_two
diff=num_one-num_two
product=num_two*num_one
division=num_one/num_two
remainder=num_two%num_one
exp=num_one**num_two
floor_division=num_one//num_two
print(total,diff,product,remainder,exp,floor_division)

#Area and circumference of circle
import math
radius=float(input("Give us the radius please: "))
area_of_circle= math.pi*radius**2
circumference_of_circle=2*math.pi*radius
print('the area of the circle is: ',area_of_circle,'the circumference is: ',circumference_of_circle)

# getting personal info using input function
first_name=input("enter your first name: ")
last_name=input("enter your last name: ")
country=input("enter your country: ")
age=input("how old are you: ")
print(first_name, last_name, country, age)

#Checking python reserve words
help('keywords')