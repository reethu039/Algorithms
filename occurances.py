# Finding the occurences of each element of an array or a list. 

def count_occurrences(inputArray):
    numOccurancesDict = {}
    
    for num in inputArray:
        if num in numOccurancesDict:
            numOccurancesDict[num] += 1
        else:
            numOccurancesDict[num] = 1
    return numOccurancesDict

sizeOfArray = int(input("Enter size of the array : "))
inputArray = []
for i in range(sizeOfArray) :
    inputArray.append(int(input("Enter number to the array : ")))

result = count_occurrences(inputArray)

print("\nOCCURANCE OF EACH ELEMENT")
for key, value in result.items():
    print(f"{key} : {value} occurrences")