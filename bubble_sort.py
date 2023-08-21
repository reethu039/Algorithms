#Implement bubble sort sorting algorithm to sort the given array of elements.

def bubbleSort(numElements, elements) :
    for i in range(numElements) :
        j = i
        for j in range(numElements-1) :
            if elements[j] > elements[j+1] :
                elements[j], elements[j+1] = elements[j+1], elements[j]   
    print(elements)             

numElements = int(input("Enter no.of elements : "))
#elements = list(map(int, input("").split()))

elements = []
for i in range(numElements) :
    ele = int(input("Enter the array elements : "))
    elements.append(ele)

print(elements)
bubbleSort(numElements, elements)