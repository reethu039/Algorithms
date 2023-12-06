def merge(left, right, arr):
    i = j = k = 0
    comp = 0
    while (i < len(left)) and (j < len(right)):
        comp += 1
        if left[i] <= right[j]:
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
        
    return comp

def mergeSort(arr):
    comp = 0
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        comp_l = mergeSort(left)
        comp_r= mergeSort(right)
        comp += comp_l + comp_r
        c = merge(left, right, arr)
        comp += c
        
    return comp

size = int(input(""))
if size != 0:
    array = list(map(int, input("").split()))
    comp = mergeSort(array)
    print(comp)
    for i in array:
        print(i, end=' ')
else:
    print("-1")
