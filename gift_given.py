import time
start = time.time()
studentNames = ['a', 'b', 'c', 'd']
giftRecieved = ['F', 'F', 'F', 'F']

for i in range(0, len(studentNames)-1) :
    print(studentNames[i] + " has recieved gift")
    giftRecieved[i] = 'T'
    for j in range(0, len(giftRecieved)-1) :
        print(giftRecieved[j], end=' ')
    print("\n")
print("--- %s seconds ---" % (time.time() - start))