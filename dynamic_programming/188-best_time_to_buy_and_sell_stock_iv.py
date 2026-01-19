#188. Best Time to Buy and Sell Stock IV
#Hard
#
#You are given an integer array prices where prices[i] is the price of a given
#stock on the ith day, and an integer k.
#
#Find the maximum profit you can achieve. You may complete at most k transactions.
#
#Note: You may not engage in multiple transactions simultaneously (i.e., you must
#sell the stock before you buy again).
#
#Example 1:
#Input: k = 2, prices = [2,4,1]
#Output: 2
#Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 2.
#
#Example 2:
#Input: k = 2, prices = [3,2,6,5,0,3]
#Output: 7
#Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 4.
#Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3.
#
#Constraints:
#    1 <= k <= 100
#    1 <= prices.length <= 1000
#    0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # If k >= n//2, we can make unlimited transactions
        if k >= n // 2:
            return sum(max(0, prices[i+1] - prices[i]) for i in range(n-1))

        # dp[i][j][0] = max profit with i transactions, at day j, not holding
        # dp[i][j][1] = max profit with i transactions, at day j, holding

        # Simplified to just track buy and sell states for each transaction
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i-1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[k]

    # Alternative 2D DP approach
    def maxProfitDP(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        if k >= n // 2:
            return sum(max(0, prices[i+1] - prices[i]) for i in range(n-1))

        # dp[i][j] = max profit using at most i transactions up to day j
        dp = [[0] * n for _ in range(k + 1)]

        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])

        return dp[k][n-1]
