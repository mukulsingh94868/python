Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ding = 10
>>> ding
10
>>> if ding > 5:
	print("ding ding dang")
	print("ok done")
    if ding < 12:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if ding > 5:
	print("ding ding dang")
	print("ok done")
if ding < 12:
	
SyntaxError: invalid syntax
>>> if ding > 5:
	print("ding ding dang")
	print("ok done")
 if ding < 20:
	 
SyntaxError: unindent does not match any outer indentation level
>>> if ding > 5:
	print("ding ding dang")
	print("ok done")
        if ding < 12:
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> if ding > 5:
	print("ding ding dang")
	print("ok done")
if ding < 12:
	
SyntaxError: invalid syntax
>>> if ding > 5:
	print("ding ding dang")
	print("ok done")

	
ding ding dang
ok done
>>> 