#64. Minimum Path Sum
#Medium
#
#Given a m x n grid filled with non-negative numbers, find a path from top left
#to bottom right, which minimizes the sum of all numbers along its path.
#
#Note: You can only move either down or right at any point in time.
#
#Example 1:
#Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
#Output: 7
#Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#Example 2:
#Input: grid = [[1,2,3],[4,5,6]]
#Output: 12
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 200
#    0 <= grid[i][j] <= 200

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        DP with 2D array.
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # First row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # First column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill rest
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


class SolutionSpaceOptimized:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Space-optimized DP - O(n) space.
        """
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[n - 1]


class SolutionInPlace:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        In-place modification - O(1) extra space.
        """
        m, n = len(grid), len(grid[0])

        # First row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # First column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Fill rest
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]


class SolutionMemoization:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Top-down DP with memoization.
        """
        from functools import lru_cache

        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            return grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))

        return dp(m - 1, n - 1)
