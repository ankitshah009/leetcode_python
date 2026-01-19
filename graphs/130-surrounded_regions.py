#130. Surrounded Regions
#Medium
#
#Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally
#surrounded by 'X'.
#
#A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#Example 1:
#Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#Explanation: Surrounded regions should not be on the border.
#
#Example 2:
#Input: board = [["X"]]
#Output: [["X"]]
#
#Constraints:
#    m == board.length
#    n == board[i].length
#    1 <= m, n <= 200
#    board[i][j] is 'X' or 'O'.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Mark border-connected O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # Flip O's to X's and T's back to O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
