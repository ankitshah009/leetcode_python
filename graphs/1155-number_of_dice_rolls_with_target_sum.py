#1155. Number of Dice Rolls With Target Sum
#Medium
#
#You have n dice, and each die has k faces numbered from 1 to k.
#
#Given three integers n, k, and target, return the number of possible ways
#(out of the k^n total ways) to roll the dice, so the sum of the face-up
#numbers equals target. Since the answer may be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 1, k = 6, target = 3
#Output: 1
#Explanation: You throw one die with 6 faces.
#There is only one way to get a sum of 3.
#
#Example 2:
#Input: n = 2, k = 6, target = 7
#Output: 6
#Explanation: You throw two dice, each with 6 faces.
#There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#
#Example 3:
#Input: n = 30, k = 30, target = 500
#Output: 222616187
#
#Constraints:
#    1 <= n, k <= 30
#    1 <= target <= 1000

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        DP: dp[i][j] = ways to get sum j with i dice
        """
        MOD = 10**9 + 7

        # dp[j] = ways to get sum j with current number of dice
        dp = [0] * (target + 1)
        dp[0] = 1

        for dice in range(n):
            new_dp = [0] * (target + 1)
            for j in range(1, target + 1):
                for face in range(1, min(k, j) + 1):
                    new_dp[j] = (new_dp[j] + dp[j - face]) % MOD
            dp = new_dp

        return dp[target]


class SolutionMemo:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Top-down DP with memoization"""
        MOD = 10**9 + 7

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(dice, total):
            if dice == 0:
                return 1 if total == 0 else 0
            if total <= 0:
                return 0

            ways = 0
            for face in range(1, k + 1):
                if total >= face:
                    ways = (ways + dp(dice - 1, total - face)) % MOD
            return ways

        return dp(n, target)


class Solution2D:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Explicit 2D DP"""
        MOD = 10**9 + 7

        # dp[i][j] = ways to get sum j using i dice
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(i, min(i * k, target) + 1):  # Min sum = i, max sum = i*k
                for face in range(1, k + 1):
                    if j >= face:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MOD

        return dp[n][target]
