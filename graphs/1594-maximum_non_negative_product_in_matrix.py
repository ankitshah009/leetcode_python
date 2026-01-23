#1594. Maximum Non Negative Product in a Matrix
#Medium
#
#You are given a m x n matrix grid. Initially, you are located at the top-left
#corner (0, 0), and in each step, you can only move right or down in the matrix.
#
#Among all possible paths starting from the top-left corner (0, 0) and ending
#in the bottom-right corner (m - 1, n - 1), find the path with the maximum
#non-negative product. The product of a path is the product of all integers
#in the grid cells visited along the path.
#
#Return the maximum non-negative product modulo 10^9 + 7. If the maximum product
#is negative, return -1.
#
#Notice that the modulo is performed after getting the maximum product.
#
#Example 1:
#Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
#Output: -1
#Explanation: It's not possible to get non-negative product starting from (0,0).
#
#Example 2:
#Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
#Output: 8
#Explanation: Maximum non-negative product is 1 * 1 * -2 * -4 * 1 = 8.
#
#Example 3:
#Input: grid = [[1,3],[0,-4]]
#Output: 0
#Explanation: Maximum non-negative product is 1 * 0 = 0.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 15
#    -4 <= grid[i][j] <= 4

from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        Track both maximum and minimum products at each cell.
        - If current value is positive: max_product = max * curr
        - If current value is negative: max_product = min * curr

        This is because multiplying by negative flips the sign.
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp_max[i][j] = max product to reach (i,j)
        # dp_min[i][j] = min product to reach (i,j)
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]

        # Initialize first cell
        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        # First row
        for j in range(1, n):
            dp_max[0][j] = dp_max[0][j-1] * grid[0][j]
            dp_min[0][j] = dp_min[0][j-1] * grid[0][j]

        # First column
        for i in range(1, m):
            dp_max[i][0] = dp_max[i-1][0] * grid[i][0]
            dp_min[i][0] = dp_min[i-1][0] * grid[i][0]

        # Fill rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]

                # From top or left
                candidates = [
                    dp_max[i-1][j] * val,
                    dp_min[i-1][j] * val,
                    dp_max[i][j-1] * val,
                    dp_min[i][j-1] * val
                ]

                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)

        result = dp_max[m-1][n-1]
        return result % MOD if result >= 0 else -1


class SolutionOptimized:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        Space-optimized version using 1D arrays.
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Arrays for current and previous rows
        max_dp = [0] * n
        min_dp = [0] * n

        # Initialize first row
        max_dp[0] = min_dp[0] = grid[0][0]
        for j in range(1, n):
            max_dp[j] = max_dp[j-1] * grid[0][j]
            min_dp[j] = min_dp[j-1] * grid[0][j]

        # Process remaining rows
        for i in range(1, m):
            new_max = [0] * n
            new_min = [0] * n

            # First column
            new_max[0] = max_dp[0] * grid[i][0]
            new_min[0] = min_dp[0] * grid[i][0]
            if new_max[0] < new_min[0]:
                new_max[0], new_min[0] = new_min[0], new_max[0]

            for j in range(1, n):
                val = grid[i][j]

                candidates = [
                    max_dp[j] * val,      # from top
                    min_dp[j] * val,
                    new_max[j-1] * val,   # from left
                    new_min[j-1] * val
                ]

                new_max[j] = max(candidates)
                new_min[j] = min(candidates)

            max_dp, min_dp = new_max, new_min

        result = max_dp[n-1]
        return result % MOD if result >= 0 else -1


class SolutionMemo:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        """
        Memoization approach with tuple tracking (max, min) products.
        """
        from functools import lru_cache

        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dp(i: int, j: int):
            """Returns (max_product, min_product) to reach (i,j)."""
            val = grid[i][j]

            if i == 0 and j == 0:
                return (val, val)

            candidates_max = []
            candidates_min = []

            if i > 0:
                top_max, top_min = dp(i-1, j)
                candidates_max.extend([top_max * val, top_min * val])
                candidates_min.extend([top_max * val, top_min * val])

            if j > 0:
                left_max, left_min = dp(i, j-1)
                candidates_max.extend([left_max * val, left_min * val])
                candidates_min.extend([left_max * val, left_min * val])

            return (max(candidates_max), min(candidates_min))

        max_val, _ = dp(m-1, n-1)
        return max_val % MOD if max_val >= 0 else -1
