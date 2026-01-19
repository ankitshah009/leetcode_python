#322. Coin Change
#Medium
#
#You are given an integer array coins representing coins of different
#denominations and an integer amount representing a total amount of money.
#
#Return the fewest number of coins that you need to make up that amount. If
#that amount of money cannot be made up by any combination of the coins,
#return -1.
#
#You may assume that you have an infinite number of each kind of coin.
#
#Example 1:
#Input: coins = [1,2,5], amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1
#
#Example 2:
#Input: coins = [2], amount = 3
#Output: -1
#
#Example 3:
#Input: coins = [1], amount = 0
#Output: 0
#
#Constraints:
#    1 <= coins.length <= 12
#    1 <= coins[i] <= 2^31 - 1
#    0 <= amount <= 10^4

from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Bottom-up DP"""
        # dp[i] = minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


class SolutionMemo:
    """Top-down memoization"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def dp(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            min_coins = float('inf')
            for coin in coins:
                result = dp(remaining - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            return min_coins

        result = dp(amount)
        return result if result != float('inf') else -1


class SolutionBFS:
    """BFS approach - find shortest path"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        from collections import deque

        visited = {0}
        queue = deque([0])
        level = 0

        while queue:
            level += 1
            for _ in range(len(queue)):
                current = queue.popleft()

                for coin in coins:
                    next_amount = current + coin
                    if next_amount == amount:
                        return level
                    if next_amount < amount and next_amount not in visited:
                        visited.add(next_amount)
                        queue.append(next_amount)

        return -1


class SolutionDPOptimized:
    """DP with early termination"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
