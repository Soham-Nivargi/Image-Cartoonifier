import numpy as np

def solution(num):
    out = []
    for i in range(0, len(num)):
        if((num[i])%2 != 0):
            out.append(num[i])
    return out
    
nums = [1, 2, 3, 4, 5, 6]
sol = solution(nums)
print(sol)
