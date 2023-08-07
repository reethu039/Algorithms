# Python program to print prime factors
def primeFactors(n):  
    while(n % 2 == 0):
        print(2)
        n = n / 2
        
    i = 3    
    while(i*i<=n):
        while(n % i== 0):
            print(i) 
            n = n / i
        i += 2
        
    if(n > 2):
        print(n)
    
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

primeFactors1 = []
primeFactors2 = []

n = 315
primeFactors(n)
