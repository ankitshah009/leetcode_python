#877. Stone Game
#Medium
#
#Alice and Bob play a game with piles of stones. There are an even number of
#piles arranged in a row, and each pile has a positive integer number of stones
#piles[i].
#
#The objective of the game is to end with the most stones. The total number of
#stones across all the piles is odd, so there are no ties.
#
#Alice and Bob take turns, with Alice starting first. Each turn, a player takes
#the entire pile of stones either from the beginning or from the end of the row.
#This continues until there are no more piles left, at which point the person
#with the most stones wins.
#
#Assuming Alice and Bob play optimally, return true if Alice wins the game, or
#false if Bob wins.
#
#Example 1:
#Input: piles = [5,3,4,5]
#Output: true
#Explanation: Alice starts first, and can take either 5. She takes 5 from left.
#Now piles = [3,4,5]. Bob takes 5. piles = [3,4]. Alice takes 4. piles = [3].
#Bob takes 3. Alice has 5+4=9, Bob has 5+3=8. Alice wins.
#
#Example 2:
#Input: piles = [3,7,2,3]
#Output: true
#
#Constraints:
#    2 <= piles.length <= 500
#    piles.length is even.
#    1 <= piles[i] <= 500
#    sum(piles[i]) is odd.

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        """
        Mathematical insight: Alice can always win because she can choose
        to always take odd or even indexed piles.
        """
        return True


class SolutionDP:
    """DP solution for general understanding"""

    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        # dp[i][j] = max score difference (current player - opponent) for piles[i:j+1]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])

        return dp[0][n-1] > 0


class SolutionMemo:
    """Memoized recursion"""

    def stoneGame(self, piles: list[int]) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            """Max score difference for current player in piles[i:j+1]"""
            if i > j:
                return 0
            # Current player chooses left or right
            return max(piles[i] - dp(i+1, j), piles[j] - dp(i, j-1))

        return dp(0, len(piles) - 1) > 0


class SolutionOptimized:
    """O(n) space DP"""

    def stoneGame(self, piles: list[int]) -> bool:
        n = len(piles)
        dp = piles[:]  # dp[i] represents dp[i][i] initially

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(piles[i] - dp[i+1], piles[j] - dp[i])

        return dp[0] > 0
