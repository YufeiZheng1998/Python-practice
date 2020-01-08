def maxProfit(prices):
    mins = prices[0]
    maxs = 0
    for i in range(len(prices)):
        mins = min(mins,prices[i])
        maxs = max(maxs,prices[i] - mins)
    return maxs
print(maxProfit([7,1,5,3,6,4]))
