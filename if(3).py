Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if x < 0:
	x = 0
	print("negative changed to zero")

	
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    if x < 0:
NameError: name 'x' is not defined
>>> if x < 0:
	x = 0
	print("negative changed to zero")
    elif x == 0:
	    
SyntaxError: unindent does not match any outer indentation level
>>>  if x < 0:
	x = 0
	print("negative changed to zero")
	
SyntaxError: unexpected indent
>>> number = 12
>>> number
12
>>> if number > 10:
	print("hey")
elif number < 13 and number > 9:
	print("jolly")
elif number < 15 or number > 12:
	print("mam")
else:
	print("hello jolly mam")

	
hey
>>> number = 16
>>> number
16
>>> 
>>> 
>>> 
>>> 
>>> 