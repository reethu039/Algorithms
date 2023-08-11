# Python program to print the gcd of 2 given numbers using middle school method
import time
start = time.time()
def primeFactors(n):  
    primeFactorsArray = []
    #print("n is : ",n)
    while(n % 2 == 0):
        primeFactorsArray.append(2)
        n = n / 2
        
    i = 3    
    while(i*i<=n):
        while(n % i== 0):
            primeFactorsArray.append(i)
            n = n / i
        i += 2
        
    if(n > 2):
        primeFactorsArray.append(int(n))
    
    return primeFactorsArray

def common_primes(primeFactorsArray1, primeFactorsArray2):
    common = []
    remaining1 = []
    remaining2 = []
    
    for num1 in primeFactorsArray1:
        if num1 in primeFactorsArray2:
            common.append(num1)
            primeFactorsArray2.remove(num1)  
        else:
            remaining1.append(num1)
    
    remaining1.extend(primeFactorsArray2)
    remaining2.extend(primeFactorsArray2)
    
    return common


def find_gcd(common_list) :
    i = 0
    gcd = 1
    while(i <= len(common_list)-1):
        gcd *= common_list[i]
        i += 1
    return gcd
    
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

primeFactorsArray1 = []
primeFactorsArray2 = []

primeFactorsArray1 = primeFactors(num1)
primeFactorsArray2 = primeFactors(num2)


print("\nPrime factors of {} = {}".format(num1, primeFactorsArray1))
print("Prime factors of {} = {}".format(num2, primeFactorsArray2))

common_list = []
common_list = common_primes(primeFactorsArray1, primeFactorsArray2)
print("Final list of common primes = ", common_list)

result = find_gcd(common_list)
print("\nThe gcd of {} and {} is {}".format(num1, num2, result))
print("--- %s milliseconds---" % ((time.time() - start)*1000))