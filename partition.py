def partition(array, pivotIndex, low, high):
    swap = 0
    pivot = array[pivotIndex]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
            if i!=j:
                swap+=1
    array[i+1], array[pivotIndex] = array[pivotIndex], array[i+1]
    swap+=1
    print(swap)
    for k in range(len(array)):
        if k==(len(array)-1):
            print(array[k])
        else:
            print(array[k], end=' ')
    print(i+1)
    

arraySize = int(input(""))
if arraySize == 0:
    print("-1")
else:
    array = list(map(int, input("").split()))
    pivotIndex = int(input(""))
    partition(array, pivotIndex, 0, arraySize-1)
    