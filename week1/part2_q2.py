import numpy as np
import random

array_2d = [[0 for j in range(4)] for i in range(4)]

array_2d[0][0] = 1
array_2d[0][1] = 5
array_2d[0][2] = 3
array_2d[0][3] = 2

array_2d[1][0] = 1
array_2d[1][1] = 4
array_2d[1][2] = 3
array_2d[1][3] = 2

array_2d[2][0] = 1
array_2d[2][1] = 6
array_2d[2][2] = 3
array_2d[2][3] = 2

array_2d[3][0] = 0
array_2d[3][1] = 0
array_2d[3][2] = 0
array_2d[3][3] = 1

arr=[]
maxi = []
mini = []

for row in array_2d:
    maxi.append(max(row))
    mini.append(min(row))

for i in range(4):
    arr.append(array_2d[i][i])

print("Digonal array: " , arr)
print("Trace: ", sum(arr))
print(maxi)
print(mini)

array_45 = np.random.uniform(low=0.0, high=1.0, size=(4, 5))

print(array_45)

array_f = [[0 for j in range(5)] for i in range(4)]

for i in range(4):
    for j in range(5):
        for m in range(4):
            array_f[i][j] += (array_2d[i][m] * array_45[m][j])

print(array_f)
    

