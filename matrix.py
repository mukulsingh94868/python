X = [[12,3,4],
     [4,5,6],
     [5,3,6]]
Y = [[5,6,4],
     [4,2,1],
     [5,6,4]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
            
