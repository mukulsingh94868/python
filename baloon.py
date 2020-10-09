n = int(input("first input:"))
n1 = int(input("second number:"))
n2 = int(input("third number:"))

sum = (n*n1*n2)
print(sum)

for i in range(5):
	print(n)

if n == n1:
   print("soki")
elif n == n2:
   print("loki")
else:
    print("iski bhn ka")

print("the fault values is",n,n1,n2)       

print("after values:")
n = n + 1
n1 = n1 + 2
n2 = n2  + 3

print((n1,n2,n2))

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))

print("the value of a and b is:",(a,b))

temp = a
a = b
b = temp
print("after swapping the values of a and b is:",(a,b))


num = input("what is the string input you want to reverse:")

def reverse_string(num):
	return num[::-1]
my_text = reverse_string(num)
print("the text is:")
print(my_text)	
