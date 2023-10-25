def insertionSort(size, arr):
    swap = 0
    comp = 0
    for i in range(1, size):
        temp = arr[i]
        j = i-1
        comp += 1
        while j>=0 and arr[j]>temp:
            if j==0:
                comp -=1
            comp += 1
            arr[j+1] = arr[j]
            swap += 1
            j-=1
        arr[j+1] = temp
        
    print(comp)
    print(swap)
    for k in arr:
        print(k, end=' ')
        

size = int(input(""))
if size==1:
    arr = list(map(int, input("").split()))
    print("0")
    print("0")
    print(arr[0])
elif size==0:
    print("-1")
else:
    arr = list(map(int, input("").split()))
    insertionSort(size, arr)