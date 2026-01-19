#289. Game of Life
#Medium
#
#The board is made up of an m x n grid of cells, where each cell has an initial
#state: live (1) or dead (0). Each cell interacts with its eight neighbors
#(horizontal, vertical, diagonal) using these rules:
#
#1. Any live cell with fewer than two live neighbors dies (underpopulation).
#2. Any live cell with two or three live neighbors lives on.
#3. Any live cell with more than three live neighbors dies (overpopulation).
#4. Any dead cell with exactly three live neighbors becomes a live cell.
#
#The next state is created by applying the above rules simultaneously to every
#cell in the current state, where births and deaths occur simultaneously.
#Given the current state of the m × n grid board, return the next state.
#
#Example 1:
#Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
#Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#
#Example 2:
#Input: board = [[1,1],[1,0]]
#Output: [[1,1],[1,1]]
#
#Constraints:
#    m == board.length
#    n == board[i].length
#    1 <= m, n <= 25
#    board[i][j] is 0 or 1.
#
#Follow up: Can you solve it in-place?

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        In-place solution using state encoding.
        States: 0 (dead->dead), 1 (live->?), 2 (dead->live), 3 (live->live)
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def count_live_neighbors(row, col):
            count = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    # Count cells that were originally alive (1 or 3)
                    if board[new_row][new_col] in (1, 3):
                        count += 1
            return count

        # First pass: encode next state
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1:  # Currently alive
                    if live_neighbors in (2, 3):
                        board[i][j] = 3  # Stays alive
                    # Otherwise stays 1 (will become dead)
                else:  # Currently dead
                    if live_neighbors == 3:
                        board[i][j] = 2  # Becomes alive

        # Second pass: decode to final state
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] >= 2 else 0


class SolutionCopy:
    """Using a copy of the board"""

    def gameOfLife(self, board: List[List[int]]) -> None:
        import copy

        m, n = len(board), len(board[0])
        original = copy.deepcopy(board)
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < m and 0 <= nj < n:
                        live_neighbors += original[ni][nj]

                # Apply rules
                if original[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0
                else:
                    if live_neighbors == 3:
                        board[i][j] = 1
