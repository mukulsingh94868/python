def my_function(x):
  return list(dict.fromkeys(x))

mylist =my_function(["a","b","c","c","a"])
print(mylist)
