#1140. Stone Game II
#Medium
#
#Alice and Bob continue their games with piles of stones. There are a number
#of piles arranged in a row, and each pile has a positive integer number of
#stones piles[i]. The objective of the game is to end with the most stones.
#
#Alice and Bob take turns, with Alice starting first. Initially, M = 1.
#
#On each player's turn, that player can take all the stones in the first X
#remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X).
#
#The game continues until all the stones have been taken.
#
#Assuming Alice and Bob play optimally, return the maximum number of stones
#Alice can get.
#
#Example 1:
#Input: piles = [2,7,9,4,4]
#Output: 10
#Explanation: If Alice takes one pile at the beginning, Bob takes two piles,
#then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total.
#
#Example 2:
#Input: piles = [1,2,3,4,5,100]
#Output: 104
#
#Constraints:
#    1 <= piles.length <= 100
#    1 <= piles[i] <= 10^4

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        Game theory DP: Maximize current player's score.
        Use suffix sum for efficiency.
        """
        n = len(piles)

        # Suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i, m):
            """Max stones current player can get from position i with M=m"""
            if i >= n:
                return 0

            # If can take all remaining, do so
            if i + 2 * m >= n:
                return suffix[i]

            # Try taking 1 to 2*m piles
            min_opponent = float('inf')
            for x in range(1, 2 * m + 1):
                min_opponent = min(min_opponent, dp(i + x, max(m, x)))

            # Current player gets remaining minus opponent's best
            return suffix[i] - min_opponent

        return dp(0, 1)


class SolutionIterative:
    def stoneGameII(self, piles: List[int]) -> int:
        """Bottom-up DP"""
        n = len(piles)

        # Suffix sums
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][m] = max stones for current player starting at i with M=m
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix[i]
                else:
                    min_opp = float('inf')
                    for x in range(1, 2 * m + 1):
                        min_opp = min(min_opp, dp[i + x][max(m, x)])
                    dp[i][m] = suffix[i] - min_opp

        return dp[0][1]
