def add(x,y):
	return x+y
def subtract(x,y):
    return x-y
def mul(x,y):
    return x*y  
def div(x,y):
    return x/y
def mod(x,y):
    return x%y

print("your choice:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. modulas") 

choice = input("enter your choice(1/2/3/4):")
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))

if choice == "1":
   print(num1,"+",num2,"=",add(num1,num2))

elif choice == "2":
   print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == "3":
   print(num1,"*",num2,"=",mul(num1,num2)) 

elif choice == "4":
   print(num1,"/",num2,"=",div(num1,num2))

elif choice == "5":
   print(num1,"%",num2,"=",mod(num1,num2)) 

else:
    print("invalid option")                           	