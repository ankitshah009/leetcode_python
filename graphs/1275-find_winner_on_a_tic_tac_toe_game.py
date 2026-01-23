#1275. Find Winner on a Tic Tac Toe Game
#Easy
#
#Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of
#Tic-Tac-Toe are:
#    Players take turns placing characters into empty squares ' '.
#    The first player A always places 'X' characters, while the second player B
#    always places 'O' characters.
#    'X' and 'O' characters are always placed into empty squares, never on
#    filled ones.
#    The game ends when there are three of the same (non-empty) character
#    filling any row, column, or diagonal.
#    The game also ends if all squares are non-empty.
#    No more moves can be played if the game is over.
#
#Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that
#the ith move will be played on grid[rowi][coli]. return the winner of the
#game if it exists (A or B). In case the game ends in a draw return "Draw".
#If there are still movements to play return "Pending".
#
#You can assume that moves is valid, follows the rules of Tic-Tac-Toe, and
#the grid is initially empty.
#
#Example 1:
#Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
#Output: "A"
#
#Example 2:
#Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
#Output: "B"
#
#Example 3:
#Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
#Output: "Draw"
#
#Constraints:
#    1 <= moves.length <= 9
#    moves[i].length == 2
#    0 <= rowi, coli <= 2
#    There are no repeated elements on moves.
#    moves follow the rules of tic-tac-toe.

from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        Track row sums, column sums, and diagonal sums.
        A adds 1, B subtracts 1. Winner if sum = 3 or -3.
        """
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1  # A = 1, B = -1

            rows[r] += player
            cols[c] += player

            if r == c:
                diag += player
            if r + c == 2:
                anti_diag += player

            # Check for winner
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(anti_diag) == 3:
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"


class SolutionGrid:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """Using actual grid"""
        grid = [[' '] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            grid[r][c] = 'X' if i % 2 == 0 else 'O'

        # Check for winner
        def check_winner(char):
            # Rows
            for r in range(3):
                if all(grid[r][c] == char for c in range(3)):
                    return True
            # Columns
            for c in range(3):
                if all(grid[r][c] == char for r in range(3)):
                    return True
            # Diagonals
            if all(grid[i][i] == char for i in range(3)):
                return True
            if all(grid[i][2 - i] == char for i in range(3)):
                return True
            return False

        if check_winner('X'):
            return "A"
        if check_winner('O'):
            return "B"

        return "Draw" if len(moves) == 9 else "Pending"
