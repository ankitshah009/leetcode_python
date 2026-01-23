#1230. Toss Strange Coins
#Medium
#
#You have some coins. The i-th coin has a probability prob[i] of facing heads
#when tossed.
#
#Return the probability that the number of coins facing heads equals target if
#you toss every coin exactly once.
#
#Example 1:
#Input: prob = [0.4], target = 1
#Output: 0.40000
#
#Example 2:
#Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
#Output: 0.03125
#
#Constraints:
#    1 <= prob.length <= 1000
#    0 <= prob[i] <= 1
#    0 <= target <= prob.length
#    Answers will be accepted as correct if they are within 10^-5 of the correct answer.

from typing import List

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        DP: dp[i][j] = probability of getting exactly j heads from first i coins.

        dp[i][j] = dp[i-1][j-1] * prob[i] + dp[i-1][j] * (1 - prob[i])
        """
        n = len(prob)

        # Use 1D DP with reverse iteration
        dp = [0.0] * (target + 1)
        dp[0] = 1.0  # 0 heads with 0 coins

        for i in range(n):
            p = prob[i]
            # Iterate in reverse to avoid using updated values
            for j in range(min(i + 1, target), 0, -1):
                dp[j] = dp[j - 1] * p + dp[j] * (1 - p)
            dp[0] *= (1 - p)

        return dp[target]


class Solution2D:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """2D DP for clarity"""
        n = len(prob)

        # dp[i][j] = probability of j heads from first i coins
        dp = [[0.0] * (target + 2) for _ in range(n + 1)]
        dp[0][0] = 1.0

        for i in range(n):
            p = prob[i]
            for j in range(min(i + 2, target + 1)):
                # Tails: stay at j heads
                dp[i + 1][j] += dp[i][j] * (1 - p)
                # Heads: move to j+1 heads
                if j + 1 <= target:
                    dp[i + 1][j + 1] += dp[i][j] * p

        return dp[n][target]


class SolutionMemo:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """Top-down DP with memoization"""
        from functools import lru_cache

        n = len(prob)

        @lru_cache(maxsize=None)
        def dp(i, heads):
            if heads > i + 1 or heads < 0:
                return 0.0
            if i < 0:
                return 1.0 if heads == 0 else 0.0

            # Either get head or tail on coin i
            return dp(i - 1, heads - 1) * prob[i] + dp(i - 1, heads) * (1 - prob[i])

        return dp(n - 1, target)
