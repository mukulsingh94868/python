Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number1 = 5
>>> number1
5
>>> int number1 = 1.1
SyntaxError: invalid syntax
>>> 
>>> int number1 = 1
SyntaxError: invalid syntax
>>> number1
5
>>> number1 = 6
>>> number1
6
>>> x = 20
>>> y = 10
>>> x
20
>>> y
10
>>> x-y
10
>>> x+y
30
>>> x*y
200
>>> x/y
2.0
>>> number1 = 2*8
>>> number1
16
>>> number1 = 12*8/7-9+5
>>> number1
9.714285714285714
>>> word = "string"
>>> word
'string'
>>> word = "23"
>>> word
'23'
>>> word = "45+4"
>>> word
'45+4'
>>> word = 45+4
>>> word
49
>>> testlist = [1,2,3]
>>> testlist
[1, 2, 3]
>>> testlist = ["1","2","3"]
>>> testlist
['1', '2', '3']
>>> testlist = [1+2,2+3,3+4]
>>> testlist
[3, 5, 7]
>>> testlist = ["1+2","2+3","3+4"]
>>> testlist
['1+2', '2+3', '3+4']
>>> testlist = [stay,love,fuck]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    testlist = [stay,love,fuck]
NameError: name 'stay' is not defined
>>> testlist
['1+2', '2+3', '3+4']
>>> tstlist = ["stay","fuch","you"]
>>> testlist
['1+2', '2+3', '3+4']
>>> tstlist
['stay', 'fuch', 'you']
>>> testlist = ["you",2,"yes",3]
>>> testlist
['you', 2, 'yes', 3]
>>> testlist = ["yes",2+3,"ok",3+4]
>>> testlist
['yes', 5, 'ok', 7]
>>> testlist = ["yes","2+3","ok","6+9"]
>>> testlist
['yes', '2+3', 'ok', '6+9']
>>> testlist = [fuck,.23]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    testlist = [fuck,.23]
NameError: name 'fuck' is not defined
>>> testlist = ["fuck u",.23]
>>> testlist
['fuck u', 0.23]
>>> {pencil,.34}
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    {pencil,.34}
NameError: name 'pencil' is not defined
>>> {"pencil,.34}
 
SyntaxError: EOL while scanning string literal
>>> testlist = {"pencil",.34}
>>> testlist
{0.34, 'pencil'}
>>> testlist = {"stay","away","yes"}
>>> testlist
{'yes', 'stay', 'away'}
>>> testlist = {"star","make:","ok","done"}
>>> testlist
{'ok', 'star', 'make:', 'done'}
>>> testlist = ("ok","done","yes")
>>> testlist
('ok', 'done', 'yes')
>>> word = 5
>>> print(word)
5
>>> number = 4
>>> number
4
>>> print(number)
4
>>> print("number")
number
>>> list = [word,number]
>>> list
[5, 4]
>>> 4 = word
SyntaxError: can't assign to literal
>>> 8**2
64
>>> 8||3
SyntaxError: invalid syntax
>>> 8|3
11
>>> 56|3
59
>>> var = 3
>>> var
3
>>> var1 = 4
>>> var1
4
>>> word = var+var1
>>> word
7
>>> print(var)
3
>>> print(var1)
4
>>> print(word)
7
>>> string1 = "cat"
>>> string2 = "dog"
>>> string3 = string1+string2
>>> string3
'catdog'
>>> string3 = {string1+string2}
>>> string3
{'catdog'}
>>> print(string3)
{'catdog'}
>>> "patrick"
'patrick'
>>> 'patrick'
'patrick'
>>> string1
'cat'
>>> string2
'dog'
>>> string3 = string1-string2
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    string3 = string1-string2
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> string3
{'catdog'}
>>> 
