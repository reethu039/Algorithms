import time
start = time.time()
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

def euclids_algo(num1, num2) :
    while(num2 != 0) :
        rem = num1 % num2
        num1 = num2
        num2 = rem
        print("num1 :",num1,"num2 :",num2)
    return num1

gcd = euclids_algo(num1, num2)

print("GCD of {} and {} is {}".format(num1, num2, gcd))
print("--- %s ---" % (time.time() - start))