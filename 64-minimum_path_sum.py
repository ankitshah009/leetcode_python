#64. Minimum Path Sum
#Medium
#
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
#right, which minimizes the sum of all numbers along its path.
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

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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
