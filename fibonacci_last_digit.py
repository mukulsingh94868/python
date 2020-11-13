def Fib_Last_Digit(n):

    if n == 0 : return 0
    elif n == 1: return 1
    else:

        a,b = 0,1
        for i in range(1,n):
            c = a + b;
            a = b;
            b = c;
        # Calculate the last digit of the final number 
        lastdigit = int(repr(c)[-1]);
        print(lastdigit);

n = int(input(""));
Fib_Last_Digit(n);