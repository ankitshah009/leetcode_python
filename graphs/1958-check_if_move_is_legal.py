#1958. Check if Move is Legal
#Medium
#
#You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the
#cell (r, c) on a game board. On the board, free cells are represented by '.',
#white cells are represented by 'W', and black cells are represented by 'B'.
#
#Each move in this game consists of choosing a free cell and changing it to the
#color you are playing as (either white or black). However, a move is only legal
#if, after changing it, the cell becomes the endpoint of a good line (horizontal,
#vertical, or diagonal).
#
#A good line is a line of three or more cells (including the endpoints) where
#the endpoints of the line are one color, and the remaining cells in the middle
#are the opposite color.
#
#Given two integers rMove and cMove and a character color representing the color
#you are playing as (white or black), return true if changing cell (rMove,
#cMove) to color color is a legal move, or false if it is not legal.
#
#Example 1:
#Input: board = [[".",".",".",".",".",".",".","."],
#                [".","B",".",".","W",".",".","."],
#                [".",".","W",".",".",".",".","."],[...]]
#       rMove = 4, cMove = 3, color = "B"
#Output: true
#
#Constraints:
#    board.length == board[r].length == 8
#    0 <= rMove, cMove < 8
#    board[rMove][cMove] == '.'
#    color is either 'B' or 'W'.

from typing import List

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        """
        Check all 8 directions for a valid line.
        """
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # horizontal and vertical
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonals
        ]

        opposite = 'W' if color == 'B' else 'B'

        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            length = 1

            # Move through opposite color cells
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opposite:
                r += dr
                c += dc
                length += 1

            # Check if we end at same color with length >= 3
            if length >= 2 and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True

        return False


class SolutionVerbose:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        """
        More explicit direction checking.
        """
        def check_direction(dr: int, dc: int) -> bool:
            opposite = 'W' if color == 'B' else 'B'
            r, c = rMove + dr, cMove + dc
            middle_count = 0

            # Count opposite color cells in this direction
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opposite:
                middle_count += 1
                r += dr
                c += dc

            # Valid if at least 1 middle cell and ends with same color
            if middle_count >= 1 and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True

            return False

        # Check all 8 directions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if check_direction(dr, dc):
                    return True

        return False
