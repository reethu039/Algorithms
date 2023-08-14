import time
import math
start = time.time()

sizeOfArray = int(input("Enter size of the array : "))
key = int(input("Enter the key to search for : "))
array = []

for i in range(sizeOfArray) :
    array.append(i*2)
    i += 1
print(array)

def search1(low, high, mid, key, array) :
    if(array[mid] == key) :
        pos = mid
        return pos
    elif(array[mid] > key) :
        low = mid + 1
        mid = math.floor((low + high)/2)
        search(low, high, mid, key, array)
    elif(array[mid] < key) :
        high = mid - 1
        mid = math.floor((low + high)/2)
        search(low, high, mid, key, array)
        
def search(low, high, key, array):
    if low > high:
        return -1  # Key not found
    mid = math.floor((low + high) / 2)
    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return search(low, mid - 1, key, array)
    else:
        return search(mid + 1, high, key, array)

low = 0
high = sizeOfArray-1
pos = search(low, high, key, array)

if(pos == -1) :
    print("{} doesn't exist in array".format(key))
else :
    print("Position of {} in array is {}".format(key, pos))
    
print("--- %s seconds ---" % ((time.time() - start)))