#Given two arrays, write a program to merge those two arrays such that the resultant array has sorted elements.
def bubbleSort(numElements, elements) :
    countComparisions = 0
    countSwapping = 0
    for i in range(0,numElements-1):  
        for j in range(numElements-i-1): 
            countComparisions += 1
            if(elements[j]>elements[j+1]):  
                elements[j], elements[j+1] = elements[j+1], elements[j]   
                countSwapping += 1
    print(countComparisions)
    print(countSwapping)
    for k in elements :
        print(k, end = ' ')        

size1 = int(input("Enter size of array 1 : "))
array1 = []
for i in range(size1) :
    ele = int(input("Enter the array elements : "))
    array1.append(ele)
size2 = int(input("Enter size of array 2 : "))
array2 = []
for i in range(size2) :
    ele = int(input("Enter the array elements : "))
    array2.append(ele)
    
array = array1 + array2
size = size1 + size2

if(size == 0) :
    print("-1\n-1\n-1")
else :
    bubbleSort(size, array)