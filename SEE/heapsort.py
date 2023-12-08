def heapify(arr, N, i, swap):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        swap[0] += 1  # Increment swap count

        # Heapify the root.
        heapify(arr, N, largest, swap)

def heapSort(arr):
    N = len(arr)
    swap = [0]  # Store swap count in a list to maintain reference

    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i, swap)

    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        swap[0] += 1  # Increment swap count
        heapify(arr, i, 0, swap)

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
