def maxProfitStocks(prices):
    n = len(prices)

    l = 0
    r = 1

    maxP = 0

    while r != n:
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        
        r += 1
    
    return maxP

print(maxProfitStocks([7,1,5,3,6,4]))