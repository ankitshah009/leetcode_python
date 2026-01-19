#1020. Number of Enclaves
#Medium
#
#You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents
#a land cell.
#
#A move consists of walking from one land cell to another adjacent (4-directionally) land
#cell or walking off the boundary of the grid.
#
#Return the number of land cells in grid for which we cannot walk off the boundary of the
#grid in any number of moves.
#
#Example 1:
#Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
#Output: 3
#Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed
#because its on the boundary.
#
#Example 2:
#Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
#Output: 0
#Explanation: All 1s are either on the boundary or can reach the boundary.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 500
#    grid[i][j] is either 0 or 1.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            grid[i][j] = 0  # Mark as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Remove all land connected to boundary
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # Count remaining land cells
        return sum(grid[i][j] for i in range(m) for j in range(n))
