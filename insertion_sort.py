def insertionSort(num, arr):
    swap = 0
    comp = 0
    for i in range(num):
        key=i
        j = i-1
        while j >= 0 and key < arr[j] :
            comp = comp + 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(swap)
    print(comp)
    for i in arr:
        print(i, end=' ')
    
num = int(input(""))
arr = list(map(int, input("").split()))
if num==1:
    print(arr[0])
elif num==0:
    print("-1")
else:
    insertionSort(num, arr)