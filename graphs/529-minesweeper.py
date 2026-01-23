#529. Minesweeper
#Medium
#
#Let's play the minesweeper game!
#
#You are given an m x n char matrix board representing the game board where:
#- 'M' represents an unrevealed mine,
#- 'E' represents an unrevealed empty square,
#- 'B' represents a revealed blank square that has no adjacent mines,
#- digit ('1' to '8') represents how many mines are adjacent to this revealed square
#- 'X' represents a revealed mine.
#
#You are also given an integer array click where click = [r, c] represents the next
#click position among all the unrevealed squares ('M' or 'E').
#
#Return the board after revealing this position according to the following rules:
#- If a mine 'M' is revealed, then the game is over. Change it to 'X'.
#- If an empty square 'E' with no adjacent mines is revealed, then change it to 'B'
#  and all of its adjacent unrevealed squares should be revealed recursively.
#- If an empty square 'E' with at least one adjacent mine is revealed, then change
#  it to a digit representing the number of adjacent mines.
#- Return the board when no more squares will be revealed.
#
#Constraints:
#    m == board.length
#    n == board[i].length
#    1 <= m, n <= 50
#    board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
#    click.length == 2
#    0 <= click[0] < m
#    0 <= click[1] < n
#    board[click[0]][click[1]] is either 'M' or 'E'.

from typing import List
from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """DFS approach"""
        m, n = len(board), len(board[0])
        r, c = click

        # If clicked on mine, game over
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def count_mines(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return
            if board[row][col] != 'E':
                return

            mines = count_mines(row, col)

            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for dr, dc in directions:
                    dfs(row + dr, col + dc)

        dfs(r, c)
        return board


class SolutionBFS:
    """BFS approach"""

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def count_mines(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count

        queue = deque([(r, c)])

        while queue:
            row, col = queue.popleft()

            if board[row][col] != 'E':
                continue

            mines = count_mines(row, col)

            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'E':
                        queue.append((nr, nc))

        return board
