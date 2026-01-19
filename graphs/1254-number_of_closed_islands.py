#1254. Number of Closed Islands
#Medium
#
#Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal 4-directionally
#connected group of 0s and a closed island is an island totally (all left, top, right, bottom)
#surrounded by 1s.
#
#Return the number of closed islands.
#
#Example 1:
#Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],
#               [1,1,1,1,1,1,1,0]]
#Output: 2
#Explanation:
#Islands in gray are closed because they are completely surrounded by water (group of 1s).
#
#Example 2:
#Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
#Output: 1
#
#Example 3:
#Input: grid = [[1,1,1,1,1,1,1],
#               [1,0,0,0,0,0,1],
#               [1,0,1,1,1,0,1],
#               [1,0,1,0,1,0,1],
#               [1,0,1,1,1,0,1],
#               [1,0,0,0,0,0,1],
#               [1,1,1,1,1,1,1]]
#Output: 2
#
#Constraints:
#    1 <= grid.length, grid[0].length <= 100
#    0 <= grid[i][j] <=1

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False  # Touches boundary
            if grid[i][j] == 1:
                return True

            grid[i][j] = 1  # Mark as visited

            # Check all 4 directions
            top = dfs(i - 1, j)
            bottom = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return top and bottom and left and right

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count
