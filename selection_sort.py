def selectionSort(num, arr):
    swap = 0
    comp = 0
    for i in range(num):
        min=i
        for j in range(i+1, num):
            if arr[j]<arr[min]:
                min=j
            comp = comp + 1
        if i!=min:
            arr[i],arr[min]=arr[min],arr[i]
            swap = swap + 1
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
    selectionSort(num, arr)