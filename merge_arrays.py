#Given two arrays, write a program to merge those two arrays such that the resultant array has sorted elements.
def merge(left, right, arr):
    i = j = k = 0
    comp = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            comp += 1
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1 
        
    print(comp)
    for i in arr:
        print(i, end=' ')

size1 = int(input(""))
if size1!=0:
    array1 = list(map(int, input("").split()))
else:
    array1 = []
size2 = int(input(""))
if size2!=0:
    array2 = list(map(int, input("").split()))
else:
    array2 = []

array = array1 + array2
size = size1 + size2

if(size == 0) :
    print("-1")
else :
    merge(array1, array2, array)