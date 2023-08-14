import time
start = time.time()

sizeOfArray = int(input("Enter size of the array : "))
key = int(input("Enter the key to search for : "))
array = []

for i in range(sizeOfArray) :
    array.append(i*2)
    i += 1
print(array)

pos = -1
for j in range(sizeOfArray) : 
    if(key == array[j]) :
        pos = j

if(pos == -1) :
    print("{} doesn't exist in array".format(key))
else :
    print("Position of {} in array is {}".format(key, pos))
    
print("--- %s milliseconds ---" % ((time.time() - start)*1000))