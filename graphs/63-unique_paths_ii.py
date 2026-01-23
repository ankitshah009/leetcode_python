#63. Unique Paths II
#Medium
#
#You are given an m x n integer array grid. There is a robot initially located at
#the top-left corner (i.e., grid[0][0]). The robot tries to move to the
#bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
#down or right at any point in time.
#
#An obstacle and space are marked as 1 and 0 respectively in grid.
#
#Return the number of possible unique paths that the robot can take to reach the
#bottom-right corner.
#
#Example 1:
#Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
#Output: 2
#Explanation: There is one obstacle in the middle of the 3x3 grid above.
#There are two ways to reach the bottom-right corner:
#1. Right -> Right -> Down -> Down
#2. Down -> Down -> Right -> Right
#
#Example 2:
#Input: obstacleGrid = [[0,1],[0,0]]
#Output: 1
#
#Constraints:
#    m == obstacleGrid.length
#    n == obstacleGrid[i].length
#    1 <= m, n <= 100
#    obstacleGrid[i][j] is 0 or 1.

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        DP with 2D array.
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # First row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # First column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # Fill rest
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class SolutionSpaceOptimized:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Space-optimized DP - O(n) space.
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]

        return dp[n - 1]


class SolutionInPlace:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        In-place modification of input grid.
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        # First row
        for j in range(1, n):
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] == 1 else obstacleGrid[0][j - 1]

        # First column
        for i in range(1, m):
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i - 1][0]

        # Fill rest
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[m - 1][n - 1]
