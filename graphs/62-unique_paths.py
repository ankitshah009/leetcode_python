#62. Unique Paths
#Medium
#
#There is a robot on an m x n grid. The robot is initially located at the top-left
#corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
#(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
#point in time.
#
#Given the two integers m and n, return the number of possible unique paths that
#the robot can take to reach the bottom-right corner.
#
#Example 1:
#Input: m = 3, n = 7
#Output: 28
#
#Example 2:
#Input: m = 3, n = 2
#Output: 3
#Explanation: From the top-left corner, there are a total of 3 ways to reach the
#bottom-right corner:
#1. Right -> Down -> Down
#2. Down -> Down -> Right
#3. Down -> Right -> Down
#
#Constraints:
#    1 <= m, n <= 100

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Math - Combination formula: C(m+n-2, m-1).
        Need (m-1) down moves and (n-1) right moves.
        """
        from math import comb
        return comb(m + n - 2, m - 1)


class SolutionDP:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        DP with 2D array.
        dp[i][j] = number of paths to reach (i, j).
        """
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class SolutionDPOptimized:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Space-optimized DP - O(n) space.
        """
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]

        return dp[n - 1]


class SolutionMath:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Direct calculation without using math.comb.
        """
        # Calculate C(m+n-2, min(m-1, n-1))
        numerator = denominator = 1
        small = min(m - 1, n - 1)

        for i in range(small):
            numerator *= (m + n - 2 - i)
            denominator *= (i + 1)

        return numerator // denominator


class SolutionMemoization:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Top-down DP with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 1
            return dp(i - 1, j) + dp(i, j - 1)

        return dp(m - 1, n - 1)
