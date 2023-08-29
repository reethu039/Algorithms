#Given an array having n number of elements write an algorithm to find the minimum element in the array

def findMininum(arraySize, array, index, minElement, i) :
    if i < arraySize :
        if array[i] < minElement :
            minElement = array[i]
            index = i
        findMininum(arraySize, array, index, minElement, i+1)
    print(index, minElement)

arraySize = int(input("Enter the size of array : "))
if arraySize != 0 :
    array = list(map(int, input("").split()))
    minElement = array[0]
    findMininum(arraySize, array, 0, minElement, 0)
else :
    print("-1")

