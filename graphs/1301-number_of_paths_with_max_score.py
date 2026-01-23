#1301. Number of Paths with Max Score
#Hard
#
#You are given a square board of characters. You can move on the board starting
#at the bottom right square marked with 'S'.
#
#You need to reach the top left square marked with 'E'. The rest of the squares
#are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'.
#
#In one move you can go up, left or diagonally up-left only if there is no
#obstacle there.
#
#Return a list of two integers: the first integer is the maximum sum of numeric
#characters you can collect, and the second integer is the number of such paths
#that you can take to get that maximum sum, taken modulo 10^9 + 7.
#
#In case there is no path, return [0, 0].
#
#Example 1:
#Input: board = ["E23","2X2","12S"]
#Output: [7,1]
#
#Example 2:
#Input: board = ["E12","1X1","21S"]
#Output: [4,2]
#
#Example 3:
#Input: board = ["E11","XXX","11S"]
#Output: [0,0]
#
#Constraints:
#    2 <= board.length == board[i].length <= 100

from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """
        DP from bottom-right to top-left.
        Track (max_score, count) for each cell.
        """
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = (max_score, count)
        dp = [[(-1, 0)] * n for _ in range(n)]

        # Start position
        dp[n-1][n-1] = (0, 1)

        # Fill DP from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    continue
                if i == n - 1 and j == n - 1:
                    continue

                # Get value at current cell
                if board[i][j] == 'E':
                    val = 0
                elif board[i][j] == 'S':
                    val = 0
                else:
                    val = int(board[i][j])

                # Check three directions: right, down, diagonal
                max_score = -1
                total_count = 0

                for di, dj in [(0, 1), (1, 0), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n and dp[ni][nj][0] >= 0:
                        score = dp[ni][nj][0] + val
                        if score > max_score:
                            max_score = score
                            total_count = dp[ni][nj][1]
                        elif score == max_score:
                            total_count = (total_count + dp[ni][nj][1]) % MOD

                dp[i][j] = (max_score, total_count)

        if dp[0][0][0] < 0:
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]


class SolutionBottomUp:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        """Alternative implementation with cleaner indexing"""
        MOD = 10**9 + 7
        n = len(board)

        # Convert board to list for easier manipulation
        board = [list(row) for row in board]
        board[0][0] = '0'  # E -> 0
        board[n-1][n-1] = '0'  # S -> 0

        # dp[i][j] = (max_sum, num_paths)
        INF = float('-inf')
        score = [[INF] * n for _ in range(n)]
        paths = [[0] * n for _ in range(n)]

        score[n-1][n-1] = 0
        paths[n-1][n-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n-1 and j == n-1):
                    continue

                val = int(board[i][j])

                for di, dj in [(0, 1), (1, 0), (1, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < n and nj < n:
                        new_score = score[ni][nj] + val
                        if new_score > score[i][j]:
                            score[i][j] = new_score
                            paths[i][j] = paths[ni][nj]
                        elif new_score == score[i][j]:
                            paths[i][j] = (paths[i][j] + paths[ni][nj]) % MOD

        if score[0][0] == INF:
            return [0, 0]
        return [score[0][0], paths[0][0]]
