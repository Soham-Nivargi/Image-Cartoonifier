import random
import scipy
import numpy as np

arr = []
for i in range(0, 100):
    arr.append(random.randint(1, 100))
print("The mean is : " , np.mean(arr))
print("The median is :" , np.median(arr))

print("Standard deviation : ", np.std(arr))
print("Range: " , np.max(arr)-np.min(arr))