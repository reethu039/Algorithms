# Python program to print prime factors

def primeFactors(n):  
    primeFactorsArray = []
    print("n is : ",n)
    while(n % 2 == 0):
        #print(2)
        primeFactorsArray.append(2)
        #print(primeFactorsArray)
        n = n / 2
        
    i = 3    
    while(i*i<=n):
        while(n % i== 0):
            #print(i) 
            primeFactorsArray.append(i)
            #print(primeFactorsArray)
            n = n / i
        i += 2
        
    if(n > 2):
        #print(n)
        primeFactorsArray.append(int(n))
        #print(primeFactorsArray)
    
    return primeFactorsArray

def common_primes(primeFactorsArray1, primeFactorsArray2):
    common = []
    j = 0
    for i in range(0,len(primeFactorsArray1)-1):
        while(j<=len(primeFactorsArray2)-1):
            print("i = ", i, " j = ",j)
            while primeFactorsArray1[i] == primeFactorsArray2[j]:
                #print("HERE")
                common.append(primeFactorsArray1[i])
                print("common elements : ",common)
                del primeFactorsArray1[i]
                del primeFactorsArray2[j]
                print("array 1 : ",primeFactorsArray1)
                print("array 2 : ",primeFactorsArray2)
                print(primeFactorsArray1[i],primeFactorsArray2[j], ":", i, j)
            j += 1
        i += 1
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

print(primeFactorsArray1)
print(primeFactorsArray2)

common_list = []
common_list = common_primes(primeFactorsArray1, primeFactorsArray2)
print("final common list is : ", common_list)

result = find_gcd(common_list)
print("\nThe gcd of {} and {} is {}".format(num1, num2, result))