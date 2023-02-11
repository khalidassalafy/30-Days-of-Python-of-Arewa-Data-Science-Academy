Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Checking data types
>>> type(10)
<class 'int'>
>>> type(2.5)
<class 'float'>
>>> type("Hello")
<class 'str'>
>>> type(1+j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(1+j)
NameError: name 'j' is not defined
>>> type(1+2j)
<class 'complex'>
>>> type ([0,1,2,3,4])
<class 'list'>
>>> type({"Name": "Auwal"})
<class 'dict'>
>>> type(1,0,8,'Auwal')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(1,0,8,'Auwal')
TypeError: type() takes 1 or 3 arguments
>>> type((1,0.8,"Auwal"))
<class 'tuple'>
>>> type({"Hausa","Igbo","Yoruba"})
<class 'set'>
