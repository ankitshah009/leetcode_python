#688. Knight Probability in Chessboard
#Medium
#
#On an n x n chessboard, a knight starts at the cell (row, column) and attempts
#to make exactly k moves. The rows and columns are 0-indexed, so the top-left
#cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
#
#A chess knight has eight possible moves it can make. Each move is two cells in
#a cardinal direction, then one cell in an orthogonal direction.
#
#Each time the knight is to move, it chooses one of eight possible moves
#uniformly at random and moves there.
#
#The knight continues moving until it has made exactly k moves or has moved off
#the chessboard.
#
#Return the probability that the knight remains on the board after it has
#stopped moving.
#
#Example 1:
#Input: n = 3, k = 2, row = 0, column = 0
#Output: 0.06250
#Explanation: There are two moves that keep the knight on the board.
#
#Example 2:
#Input: n = 1, k = 0, row = 0, column = 0
#Output: 1.00000
#
#Constraints:
#    1 <= n <= 25
#    0 <= k <= 100
#    0 <= row, column <= n - 1

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
        DP: dp[i][j] = probability of being at (i,j) after current moves.
        """
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        # Current probability distribution
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = [[0.0] * n for _ in range(n)]

            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                new_dp[nr][nc] += dp[r][c] / 8.0

            dp = new_dp

        return sum(sum(row) for row in dp)


class SolutionMemoization:
    """Top-down DP with memoization"""

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        from functools import lru_cache

        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        @lru_cache(maxsize=None)
        def dp(r, c, moves_left):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0.0
            if moves_left == 0:
                return 1.0

            prob = 0.0
            for dr, dc in moves:
                prob += dp(r + dr, c + dc, moves_left - 1) / 8.0

            return prob

        return dp(row, column, k)


class SolutionSpaceOptimized:
    """Space optimized using only previous state"""

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]

        prev = {(row, column): 1.0}

        for _ in range(k):
            curr = {}
            for (r, c), prob in prev.items():
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        curr[(nr, nc)] = curr.get((nr, nc), 0) + prob / 8.0
            prev = curr

        return sum(prev.values())
