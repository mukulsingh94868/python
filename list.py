Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numberlist = [1,3,4]
>>> numberlist
[1, 3, 4]
>>> one = 1
>>> two = 2
>>> three = 3
>>> numberlist = [one,two,three]
>>> numberlist
[1, 2, 3]
>>> fruits = ['apple','banana','grapes','kiwi']
>>> fruits
['apple', 'banana', 'grapes', 'kiwi']
>>> fruits.count(fruits)
0
>>> fruits.count('apple')
1
>>> fruits.reverse()
>>> fruits
['kiwi', 'grapes', 'banana', 'apple']
>>> fruits.sort()
>>> fruits
['apple', 'banana', 'grapes', 'kiwi']
>>> fruits.pop()
'kiwi'
>>> fruits.push()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    fruits.push()
AttributeError: 'list' object has no attribute 'push'
>>> fruits.count()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fruits.count()
TypeError: count() takes exactly one argument (0 given)
>>> 