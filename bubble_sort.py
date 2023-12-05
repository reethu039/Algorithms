#Implement bubble sort sorting algorithm to sort the given array of elements.

def bubbleSort(numElements, elements) :
    countComparisions = 0
    countSwapping = 0
    for i in range(0,numElements-1):  
        for j in range(numElements-i-1): 
            countComparisions += 1
            if(elements[j]>elements[j+1]):  
                elements[j], elements[j+1] = elements[j+1], elements[j]   
                countSwapping += 1
    print(countComparisions,)
    print(countSwapping,)
    for k in elements :
        print(k, end = ' ')
    

numElements = int(input("Enter no.of elements : "))

#elements = list(map(int, input("").split()))
elements = []
for i in range(numElements) :
    ele = int(input("Enter the array elements : "))
    elements.append(ele)

if(numElements == 0) :
    print("-1\n-1\n-1")
else :
    bubbleSort(numElements, elements)