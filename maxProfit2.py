def maxProfit2(prices):
    if not prices:
        return 0
    n = len(prices)
    dp = [[0]*2 for i in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
    return dp[n-1][0]
print(maxProfit2([7,1,5,3,6,4]))