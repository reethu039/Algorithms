def partition(array, low, high):
    comp = swap = 0
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        comp += 1
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
            if i!=j:
                swap+=1
    array[i+1], array[high] = array[high], array[i+1]
    if i+1!=high:
        swap+=1
    return i+1, comp, swap
    
def quicksort(array, low, high):
    comp = swap = 0
    if low < high:
        pivot, comp_p, swap_p = partition(array, low, high)
        comp += comp_p
        swap += swap_p
        comp_l, swap_l = quicksort(array, low, pivot - 1)
        comp_r, swap_r = quicksort(array, pivot + 1, high)
        comp += comp_l + comp_r
        swap += swap_l + swap_r
    return comp, swap

arraySize = int(input(""))
if arraySize == 0:
    print("-1")
else:
    array = list(map(int, input("").split()))
    comp, swap = quicksort(array, 0, arraySize - 1)
    print(comp)
    print(swap)
    for i in array:
        print(i, end=' ')
    