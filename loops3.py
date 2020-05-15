def mukki(n):
	for i in range(0,n):
		for j in range(0,i+1):
			print("*", end="")

		print("\r")
		
n = 20
mukki(n)


		

x = ["bif","hif","gif"]
y = ["gold","ave","ace"]

a = 0
b = 0

for i in x:
    for j in y:
    	print(x[a],y[b])
        b += 1
    a += 1  
    b  = 0    
