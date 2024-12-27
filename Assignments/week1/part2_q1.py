import numpy as np

class arr:
    
    array = []
    
    def __init__(self) -> None:
        pass
    def get_array(self):
        len = int(input("Number of elements in array"))
        elem = []
        for i in range(0, len):
            elems = int(input())
            elem.append(elems)
        elem = quicksort(elem)
        return elem
    
    
def quicksort(ar):
    if len(ar) < 1:
        return ar
    else:
        pivot=ar[0]
        left = []
        right = []
        for i in range(1, len(ar)):
            if(ar[i] < pivot):
                left.append(ar[i])
            else:
                right.append(ar[i])
        return quicksort(left) + [pivot] + quicksort(right)
    
    
        

my_arr = arr()
sol = my_arr.get_array()
print(sol)
            