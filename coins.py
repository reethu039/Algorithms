# Given k coins having different denominations and total amount T (these two inputs can be read),
# Write a program to find the minimum number of coins needed to make the total amount using brute force approach. 

def minimumCoins(coins, amt) :
    if amt == 0 :
        return 0
    
    minCount = 0
    for coin in coins :
        if coin <= amt :
            count = 1 + minimumCoins(coins, amt - coin)
            if (minCount == 0) or (count < minCount) :
                minCount = count
    
    return minCount

k = int(input("Enter the number of coin denominations : "))
#coins = []
coins = list(map(int, input("").split()))
#for i in range(k) :
#    coins.append(int(input("Enter the coin denominations : ")))
T = int(input("Enter the total amount: "))

result = minimumCoins(coins, T)
print("The minimum number of coins needed is : {}".format(result))