z = input("enter the value of x:")
print(z)
ls = [1,2,3,10,11,12,13,100]
countlow = 0
counthigh = 0
counter = 0
x = 5

if x == 5:
    while counter < 100:
	    for i in ls:

	        if i < 10:
	           countlow +=  1
	        elif i >= 10 and i > 100:
	           counthigh += 1
	        else:
	            print("done") 
	    counter = counter + 1
	    print(countlow)
	    print(counthigh)           
	    print("counter is:",counter)       
else:
	print("skipping loop")
