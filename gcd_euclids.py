# Python program to print the gcd of 2 given numbers using euclids algorithm
import time
start = time.time()

def euclids_algo(num1, num2) :
    while(num2 != 0) :
        rem = num1 % num2
        num1 = num2
        num2 = rem
    return num1

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
gcd = euclids_algo(num1, num2)

print("GCD of {} and {} is {}".format(num1, num2, gcd))
print("--- %s milliseconds---" % ((time.time() - start)*1000))