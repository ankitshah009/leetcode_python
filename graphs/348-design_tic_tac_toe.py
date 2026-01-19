#348. Design Tic-Tac-Toe
#Medium
#
#Assume the following rules are for the tic-tac-toe game on an n x n board
#between two players:
#
#1. A move is guaranteed to be valid and is placed on an empty block.
#2. Once a winning condition is reached, no more moves are allowed.
#3. A player who succeeds in placing n of their marks in a horizontal,
#   vertical, or diagonal row wins the game.
#
#Implement the TicTacToe class:
#- TicTacToe(int n) Initializes the object the size of the board n.
#- int move(int row, int col, int player) Indicates that the player with id
#  player plays at the cell (row, col) of the board. The move is guaranteed to
#  be a valid move, and the two players alternate in making moves. Return:
#    - 0 if there is no winner after the move,
#    - 1 if player 1 is the winner after the move, or
#    - 2 if player 2 is the winner after the move.
#
#Example 1:
#Input: ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
#       [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2],
#        [2, 1, 1]]
#Output: [null, 0, 0, 0, 0, 0, 0, 1]
#
#Constraints:
#    2 <= n <= 100
#    player is 1 or 2.
#    0 <= row, col < n
#    (row, col) are unique for each different call to move.
#    At most n^2 calls will be made to move.

class TicTacToe:
    """O(1) move with O(n) space"""

    def __init__(self, n: int):
        self.n = n
        # Count for each row, column, and diagonals
        # Player 1 adds +1, Player 2 adds -1
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0      # Main diagonal
        self.anti_diag = 0  # Anti diagonal

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        delta = 1 if player == 1 else -1

        # Update row and column counts
        self.rows[row] += delta
        self.cols[col] += delta

        # Update diagonal if applicable
        if row == col:
            self.diag += delta
        if row + col == n - 1:
            self.anti_diag += delta

        # Check win condition
        if (abs(self.rows[row]) == n or
            abs(self.cols[col]) == n or
            abs(self.diag) == n or
            abs(self.anti_diag) == n):
            return player

        return 0


class TicTacToeSimple:
    """O(n) move with O(n^2) space - stores full board"""

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        self.board[row][col] = player

        # Check row
        if all(self.board[row][c] == player for c in range(n)):
            return player

        # Check column
        if all(self.board[r][col] == player for r in range(n)):
            return player

        # Check main diagonal
        if row == col:
            if all(self.board[i][i] == player for i in range(n)):
                return player

        # Check anti diagonal
        if row + col == n - 1:
            if all(self.board[i][n - 1 - i] == player for i in range(n)):
                return player

        return 0
