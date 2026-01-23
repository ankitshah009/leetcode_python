#518. Coin Change II
#Medium
#
#You are given an integer array coins representing coins of different denominations
#and an integer amount representing a total amount of money.
#
#Return the number of combinations that make up that amount. If that amount of
#money cannot be made up by any combination of the coins, return 0.
#
#You may assume that you have an infinite number of each kind of coin.
#
#Example 1:
#Input: amount = 5, coins = [1,2,5]
#Output: 4
#Explanation: there are four ways to make up the amount:
#5=5
#5=2+2+1
#5=2+1+1+1
#5=1+1+1+1+1
#
#Example 2:
#Input: amount = 3, coins = [2]
#Output: 0
#
#Example 3:
#Input: amount = 10, coins = [10]
#Output: 1
#
#Constraints:
#    1 <= coins.length <= 300
#    1 <= coins[i] <= 5000
#    All the values of coins are unique.
#    0 <= amount <= 5000

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Unbounded knapsack DP.
        dp[i] = number of ways to make amount i
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make 0: use no coins

        # Process each coin (this avoids counting permutations)
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


class Solution2D:
    """2D DP for clarity"""

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[i][j] = ways to make amount j using coins[0:i]
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base case: one way to make 0
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(amount + 1):
                dp[i][j] = dp[i-1][j]  # Don't use this coin
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]  # Use this coin

        return dp[n][amount]


class SolutionMemo:
    """Top-down with memoization"""

    def change(self, amount: int, coins: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(idx, remaining):
            if remaining == 0:
                return 1
            if remaining < 0 or idx >= len(coins):
                return 0

            # Skip this coin or use it
            return dp(idx + 1, remaining) + dp(idx, remaining - coins[idx])

        return dp(0, amount)
