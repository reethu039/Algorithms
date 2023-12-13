def heapify(array, size, i, swap):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < size and array[largest] < array[left]:
        largest = left

    if right < size and array[largest] < array[right]:
        largest = right
    
    if largest!=i:
        array[i], array[largest] = array[largest], array[i]
        swap[0]+=1
        heapify(array, size, largest, swap)

def heapsort(array):
    size = len(array)
    swap = [0]
    
    for i in range(size//2 -1, -1, -1):
        heapify(array, size, i, swap)
    
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        swap[0] += 1
        heapify(array, i, 0, swap)
    
    return swap[0]

size = int(input(""))
if size!=0:
    array = list(map(int, input("").split()))
    swap = heapsort(array)
    print(swap)
    for i in array:
        print(i, end=' ')
else:
    print("-1")