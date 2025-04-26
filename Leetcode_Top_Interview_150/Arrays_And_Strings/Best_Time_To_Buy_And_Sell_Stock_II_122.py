def prof(prices):
    maxp = 0

    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            maxp += prices[i] - prices[i-1]
    
    return maxp

print(prof([7,1,5,3,6,4]))

print(prof([1,2,3,4,5]))