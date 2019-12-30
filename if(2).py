Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x == 4 and y == 5
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x == 4 and y == 5
NameError: name 'x' is not defined
>>> x = 4
>>> y = 5
>>> x == 4 and y == 5
True
>>> x = 5
>>> if x < 10 and x > 5:
	print("hey")

	
>>> if x < 10 and x >=5:
	print("hey")

	
hey
>>> if x < 10 and x > 5:
	print("hey")

	
>>> if x < 10 or x > 9:
	print("hey")

	
hey
>>> x =-100
>>> x
-100
>>> if x < 13 or x < 1:
	print("hey")

	
hey
>>> 