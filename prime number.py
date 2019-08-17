num = int(input("enter number:"))
if num > 1:
    for i in range(2,num//2):
        if (num%i)==0:
            print("not aprime number")
            break
    else :
        print(num,"is a prime number")
