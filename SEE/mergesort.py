def merge(left, right, array):
    i = j = k = 0
    comp = 0
    while (i < len(left)) and (j < len(right)):
        comp+=1
        if left[i] < right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1
    
    while (i < len(left)):
        array[k] = left[i]
        i+=1
        k+=1
        
    while (j < len(right)):
        array[k] = right[j]
        j+=1
        k+=1
    
    return comp           

def mergeSort(array):
    comp = 0
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        c_left = mergeSort(left)
        c_right = mergeSort(right)
        c = merge(left, right, array)
        comp += c + c_left + c_right
    
    return comp

size = int(input(""))
if size!=0:
    array = list(map(int, input("").split()))
    comp = mergeSort(array)
    print(comp)
    for i in array:
        print(i, end=' ')
else:
    print("-1")