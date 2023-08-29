#Given an array having n number of elements write an algorithm to find the minimum element in the array.

def findMininum(arraySize, array) :
    index = 0
    minElement = array[0]
    for i in range(arraySize) :
        if array[i] < minElement :
            minElement = array[i]
            index = i
    print(index, minElement)

arraySize = int(input("Enter the size of array : "))
if arraySize != 0 :
    array = list(map(int, input("").split()))
    findMininum(arraySize, array)
else :
    print("-1")



