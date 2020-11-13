def Huge_Fib(n,m):

    if n == 0 : return 0
    elif n == 1: return 1
    else:
        a,b = 0,1
        for i in range(1,n):
            a, b = b, (a+b) % m
        print(b);

n,m = map(int, input().split());   
Huge_Fib(n,m);