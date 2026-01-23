#1269. Number of Ways to Stay in the Same Place After Some Steps
#Hard
#
#You have a pointer at index 0 in an array of size arrLen. At each step, you
#can move 1 position to the left, 1 position to the right in the array, or
#stay in the same place (The pointer should not be placed outside the array
#at any time).
#
#Given two integers steps and arrLen, return the number of ways such that your
#pointer is still at index 0 after exactly steps steps. Since the answer may
#be too large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: steps = 3, arrLen = 2
#Output: 4
#Explanation: There are 4 different ways to stay at index 0 after 3 steps.
#Right, Left, Stay
#Stay, Right, Left
#Right, Stay, Left
#Stay, Stay, Stay
#
#Example 2:
#Input: steps = 2, arrLen = 4
#Output: 2
#Explanation: There are 2 different ways to stay at index 0 after 2 steps
#Right, Left
#Stay, Stay
#
#Example 3:
#Input: steps = 4, arrLen = 2
#Output: 8
#
#Constraints:
#    1 <= steps <= 500
#    1 <= arrLen <= 10^6

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        DP: dp[step][pos] = number of ways to be at position pos after step steps.

        Key optimization: We can never go further than steps positions from 0.
        """
        MOD = 10**9 + 7

        # Maximum position we can reach
        max_pos = min(arrLen, steps // 2 + 1)

        # dp[pos] = ways to be at position pos
        dp = [0] * max_pos
        dp[0] = 1

        for _ in range(steps):
            new_dp = [0] * max_pos

            for pos in range(max_pos):
                # Stay
                new_dp[pos] = dp[pos]

                # Move from left
                if pos > 0:
                    new_dp[pos] = (new_dp[pos] + dp[pos - 1]) % MOD

                # Move from right
                if pos < max_pos - 1:
                    new_dp[pos] = (new_dp[pos] + dp[pos + 1]) % MOD

            dp = new_dp

        return dp[0]


class SolutionMemo:
    def numWays(self, steps: int, arrLen: int) -> int:
        """Top-down DP with memoization"""
        MOD = 10**9 + 7
        max_pos = min(arrLen, steps // 2 + 1)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(remaining, pos):
            if remaining == 0:
                return 1 if pos == 0 else 0

            if pos < 0 or pos >= arrLen:
                return 0

            ways = dp(remaining - 1, pos)  # Stay
            ways += dp(remaining - 1, pos - 1)  # Move left
            ways += dp(remaining - 1, pos + 1)  # Move right

            return ways % MOD

        return dp(steps, 0)
