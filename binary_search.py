import math
import time
start = time.time()
        
def search(low, high, key, array, comp):
    comp = comp+1
    if low > high:
        result = [-1, comp] #key not found
        return result
    mid = math.floor((low + high) / 2)
    if array[mid] == key:
        result = [mid, comp]
        return result
    elif array[mid] > key:
        return search(low, mid - 1, key, array, comp)
    else:
        return search(mid + 1, high, key, array, comp)

sizeOfArray = int(input(""))
if sizeOfArray==0:
    print("-1")
else:
    array = list(map(int, input("").split()))
    key = int(input(""))
    low = comp = 0
    high = sizeOfArray-1
    result = search(low, high, key, array, comp)
    print(result[1])
    print(result[0])

print("--- %s milliseconds ---" % ((time.time() - start)*1000))