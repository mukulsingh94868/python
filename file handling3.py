f = open("mukki3.txt","w")
f.write("woops! i have deleted my content")
f.close()

f = open("mukki3.txt","r")
print(f.read())
