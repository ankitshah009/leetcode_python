#1463. Cherry Pickup II
#Hard
#
#You are given a rows x cols matrix grid representing a field of cherries where
#grid[i][j] represents the number of cherries that you can collect from the
#(i, j) cell.
#
#You have two robots that can collect cherries for you:
#    Robot #1 is located at the top-left corner (0, 0), and
#    Robot #2 is located at the top-right corner (0, cols - 1).
#
#Return the maximum number of cherries collection using both robots by following
#the rules below:
#    From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or
#    (i + 1, j + 1).
#    When any robot passes through a cell, It picks up all cherries, and the cell
#    becomes an empty cell.
#    When both robots stay in the same cell, only one takes the cherries.
#    Both robots cannot move outside of the grid at any moment.
#    Both robots should reach the bottom row in grid.
#
#Example 1:
#Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
#Output: 24
#Explanation: Path of robot #1 and #2 are described in color green and blue
#respectively. Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
#Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12. Total of cherries: 12 + 12 = 24.
#
#Example 2:
#Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
#Output: 28
#Explanation: Path of robot #1 and #2 are described in color green and blue
#respectively. Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
#Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11. Total of cherries: 17 + 11 = 28.
#
#Constraints:
#    rows == grid.length
#    cols == grid[i].length
#    2 <= rows, cols <= 70
#    0 <= grid[i][j] <= 100

from typing import List
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        3D DP: dp[row][col1][col2] = max cherries when robot1 at col1, robot2 at col2
        Both robots move together row by row.
        """
        rows, cols = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dp(row: int, col1: int, col2: int) -> int:
            # Base case: reached bottom
            if row == rows:
                return 0

            # Out of bounds
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return float('-inf')

            # Cherries collected at current position
            cherries = grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]

            # Try all 9 combinations of moves (3 for each robot)
            max_future = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_future = max(max_future, dp(row + 1, col1 + dc1, col2 + dc2))

            return cherries + max_future

        return dp(0, 0, cols - 1)


class SolutionIterative:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Bottom-up DP with O(cols^2) space optimization.
        """
        rows, cols = len(grid), len(grid[0])

        # dp[c1][c2] = max cherries when robot1 at col c1, robot2 at col c2
        dp = [[float('-inf')] * cols for _ in range(cols)]
        dp[0][cols - 1] = grid[0][0] + grid[0][cols - 1]

        for row in range(1, rows):
            new_dp = [[float('-inf')] * cols for _ in range(cols)]

            for c1 in range(cols):
                for c2 in range(cols):
                    # Cherries at current positions
                    cherries = grid[row][c1]
                    if c1 != c2:
                        cherries += grid[row][c2]

                    # Try all previous positions
                    for pc1 in [c1 - 1, c1, c1 + 1]:
                        for pc2 in [c2 - 1, c2, c2 + 1]:
                            if 0 <= pc1 < cols and 0 <= pc2 < cols:
                                new_dp[c1][c2] = max(new_dp[c1][c2], dp[pc1][pc2] + cherries)

            dp = new_dp

        # Find maximum across all ending positions
        return max(dp[c1][c2] for c1 in range(cols) for c2 in range(cols))


class SolutionOptimized:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Optimized: only consider valid positions where robots haven't crossed.
        Robot 1 starts left, Robot 2 starts right.
        """
        rows, cols = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dp(row: int, c1: int, c2: int) -> int:
            if row == rows:
                return 0

            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return float('-inf')

            # Optimization: if robots swap sides, skip (by symmetry)
            if c1 > c2:
                return float('-inf')

            cherries = grid[row][c1]
            if c1 != c2:
                cherries += grid[row][c2]

            max_future = float('-inf')
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_future = max(max_future, dp(row + 1, c1 + dc1, c2 + dc2))

            return cherries + max_future

        result = dp(0, 0, cols - 1)
        dp.cache_clear()
        return result
