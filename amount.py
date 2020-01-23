x = int(input("enter the amount:"))
x1 = 0
x2 = 0
x3 = 0
x4 = 0
if x > 10000:
    print("please enter the amount which is less than 10000")
    exit()

if x % 100 == 0:
    print("notes is here",x)
        

    
    
if x / 2000:
    x1 = int(x / 2000)
    x = x % 2000
    print("2000 note",x1)

if x / 500:
    x2 = int(x / 500)
    x = x % 500
    print("500 note",x2)

if x / 200:
    x3 = int(x / 200)
    x = x % 200
    print("200 note",x3)

if x / 100:
    x4 = int(x / 100)
    x = x % 200
    print("100 note",x4)

