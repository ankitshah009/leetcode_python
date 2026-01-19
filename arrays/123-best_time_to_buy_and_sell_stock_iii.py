#123. Best Time to Buy and Sell Stock III
#Hard
#
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
#Find the maximum profit you can achieve. You may complete at most two transactions.
#
#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the
#stock before you buy again).
#
#Example 1:
#Input: prices = [3,3,5,0,0,3,1,4]
#Output: 6
#Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
#
#Example 2:
#Input: prices = [1,2,3,4,5]
#Output: 4
#
#Example 3:
#Input: prices = [7,6,4,3,1]
#Output: 0
#
#Constraints:
#    1 <= prices.length <= 10^5
#    0 <= prices[i] <= 10^5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2
