num = int(input("enter the number:"))
sum = 0
temp = 0
temp = num
while(temp > 0):
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp//10
if(sum==num):
    print("number is armstrong")

else:
    print("number is not armstrong")
    