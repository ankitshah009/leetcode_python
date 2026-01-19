#309. Best Time to Buy and Sell Stock with Cooldown
#Medium
#
#You are given an array prices where prices[i] is the price of a given stock
#on the ith day.
#
#Find the maximum profit you can achieve. You may complete as many transactions
#as you like (i.e., buy one and sell one share of the stock multiple times)
#with the following restrictions:
#    After you sell your stock, you cannot buy stock on the next day (i.e.,
#    cooldown one day).
#
#Note: You may not engage in multiple transactions simultaneously (i.e., you
#must sell the stock before you buy again).
#
#Example 1:
#Input: prices = [1,2,3,0,2]
#Output: 3
#Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#Example 2:
#Input: prices = [1]
#Output: 0
#
#Constraints:
#    1 <= prices.length <= 5000
#    0 <= prices[i] <= 1000

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        State machine DP:
        - hold: max profit if holding stock
        - sold: max profit if just sold stock (in cooldown)
        - rest: max profit if in rest state (can buy)
        """
        if not prices:
            return 0

        hold = float('-inf')  # Cannot hold without buying
        sold = 0
        rest = 0

        for price in prices:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)  # Keep holding or buy
            sold = prev_hold + price  # Sell stock
            rest = max(prev_rest, prev_sold)  # Keep resting or finish cooldown

        return max(sold, rest)


class SolutionDP:
    """Explicit DP array"""

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        n = len(prices)

        # buy[i] = max profit if we buy on or before day i
        # sell[i] = max profit if we sell on or before day i
        buy = [0] * n
        sell = [0] * n

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[0] = 0
        sell[1] = max(0, prices[1] - prices[0])

        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        return sell[-1]


class SolutionMemo:
    """Memoization approach"""

    def maxProfit(self, prices: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, holding):
            if i >= len(prices):
                return 0

            # Option 1: Do nothing
            result = dp(i + 1, holding)

            if holding:
                # Option 2: Sell
                result = max(result, prices[i] + dp(i + 2, False))
            else:
                # Option 2: Buy
                result = max(result, -prices[i] + dp(i + 1, True))

            return result

        return dp(0, False)
