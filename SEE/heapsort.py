def heapify(arr, size, i, swap):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < size and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < size and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        swap[0] += 1  # Increment swap count

        # Heapify the root.
        heapify(arr, size, largest, swap)

def heapSort(array):
    size = len(array)
    swap = [0]  # Store swap count in a list to maintain reference

    # Build a maxheap.
    for i in range(size//2 - 1, -1, -1):
        heapify(array, size, i, swap)

    # One by one extract elements
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
        swap[0] += 1  # Increment swap count
        heapify(array, i, 0, swap)

    return swap[0]  # Return the total swap count

size = int(input(""))
if size != 0:
    array = list(map(int, input("").split()))
    swap = heapSort(array)
    print(swap)
    for i in array:
        print(i, end=' ')
else:
    print("-1")
