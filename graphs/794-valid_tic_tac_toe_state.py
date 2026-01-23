#794. Valid Tic-Tac-Toe State
#Medium
#
#Given a Tic-Tac-Toe board as a string array board, return true if and only if
#it is possible to reach this board position during the course of a valid
#tic-tac-toe game.
#
#The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'.
#The ' ' character represents an empty square.
#
#Here are the rules of Tic-Tac-Toe:
#- Players take turns placing characters into empty squares ' '.
#- The first player always places 'X' characters, while the second player
#  always places 'O' characters.
#- 'X' and 'O' characters are always placed into empty squares, never filled ones.
#- The game ends when there are three of the same (non-empty) character filling
#  any row, column, or diagonal.
#- The game also ends if all squares are non-empty.
#- No more moves can be played if the game is over.
#
#Example 1:
#Input: board = ["O  ","   ","   "]
#Output: false
#Explanation: The first player always plays "X".
#
#Example 2:
#Input: board = ["XOX"," X ","   "]
#Output: false
#Explanation: Players take turns making moves.
#
#Example 3:
#Input: board = ["XOX","O O","XOX"]
#Output: true
#
#Constraints:
#    board.length == 3
#    board[i].length == 3
#    board[i][j] is either 'X', 'O', or ' '.

class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        """
        Check all validity conditions:
        1. X count = O count or X count = O count + 1
        2. If X wins, X count = O count + 1
        3. If O wins, X count = O count
        4. Both can't win
        """
        def wins(player):
            # Check rows
            for row in board:
                if row == player * 3:
                    return True
            # Check columns
            for c in range(3):
                if all(board[r][c] == player for r in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2-i] == player for i in range(3)):
                return True
            return False

        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        # X always goes first, so X count >= O count
        if x_count < o_count or x_count > o_count + 1:
            return False

        x_wins = wins('X')
        o_wins = wins('O')

        # Both can't win
        if x_wins and o_wins:
            return False

        # If X wins, it must be X's turn (x_count = o_count + 1)
        if x_wins and x_count != o_count + 1:
            return False

        # If O wins, it must be O's turn (x_count = o_count)
        if o_wins and x_count != o_count:
            return False

        return True


class SolutionCompact:
    """More compact implementation"""

    def validTicTacToe(self, board: list[str]) -> bool:
        def check_win(p):
            for i in range(3):
                if board[i] == p*3 or all(board[j][i] == p for j in range(3)):
                    return True
            return board[0][0] == board[1][1] == board[2][2] == p or \
                   board[0][2] == board[1][1] == board[2][0] == p

        flat = ''.join(board)
        x, o = flat.count('X'), flat.count('O')

        if not (x == o or x == o + 1):
            return False

        x_win, o_win = check_win('X'), check_win('O')

        if x_win and o_win:
            return False
        if x_win and x != o + 1:
            return False
        if o_win and x != o:
            return False

        return True
