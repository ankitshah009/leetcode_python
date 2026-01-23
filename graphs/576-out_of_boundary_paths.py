#576. Out of Boundary Paths
#Medium
#
#There is an m x n grid with a ball. The ball is initially at the position
#[startRow, startColumn]. You are allowed to move the ball to one of the four
#adjacent cells in the grid (possibly out of the grid crossing the grid boundary).
#You can apply at most maxMove moves to the ball.
#
#Given the five integers m, n, maxMove, startRow, startColumn, return the number
#of paths to move the ball out of the grid boundary. Since the answer can be very
#large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
#Output: 6
#
#Example 2:
#Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
#Output: 12
#
#Constraints:
#    1 <= m, n <= 50
#    0 <= maxMove <= 50
#    0 <= startRow < m
#    0 <= startColumn < n

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """DP with memoization"""
        MOD = 10**9 + 7

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(row, col, moves):
            # Out of bounds = found a path
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1

            # No moves left
            if moves == 0:
                return 0

            # Try all four directions
            return (
                dp(row - 1, col, moves - 1) +
                dp(row + 1, col, moves - 1) +
                dp(row, col - 1, moves - 1) +
                dp(row, col + 1, moves - 1)
            ) % MOD

        return dp(startRow, startColumn, maxMove)


class SolutionBottomUp:
    """Bottom-up DP"""

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to reach (i, j) with remaining moves
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        result = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue

                    for di, dj in directions:
                        ni, nj = i + di, j + dj

                        if 0 <= ni < m and 0 <= nj < n:
                            new_dp[ni][nj] = (new_dp[ni][nj] + dp[i][j]) % MOD
                        else:
                            result = (result + dp[i][j]) % MOD

            dp = new_dp

        return result
