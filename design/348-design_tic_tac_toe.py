#348. Design Tic-Tac-Toe
#Medium
#
#Assume the following rules are for the tic-tac-toe game on an n x n board
#between two players:
#
#A move is guaranteed to be valid and is placed on an empty block.
#Once a winning condition is reached, no more moves are allowed.
#A player who succeeds in placing n of their marks in a horizontal, vertical,
#or diagonal row wins the game.
#
#Implement the TicTacToe class:
#    TicTacToe(int n) Initializes the object the size of the board n.
#    int move(int row, int col, int player) Indicates that the player with id
#    player plays at the cell (row, col) of the board. The move is guaranteed
#    to be a valid move, and the two players alternate in making moves. Return
#        0 if there is no winner after the move,
#        1 if player 1 is the winner after the move, or
#        2 if player 2 is the winner after the move.
#
#Example 1:
#Input
#["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
#[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
#Output
#[null, 0, 0, 0, 0, 0, 0, 1]
#
#Constraints:
#    2 <= n <= 100
#    player is 1 or 2.
#    0 <= row, col < n
#    (row, col) are unique for each different call to move.
#    At most n^2 calls will be made to move.
#
#Follow-up: Could you do better than O(n^2) per move() operation?

class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        # rows[i] = sum for row i (player 1 adds 1, player 2 subtracts 1)
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        # Player 1 adds 1, Player 2 subtracts 1
        delta = 1 if player == 1 else -1

        self.rows[row] += delta
        self.cols[col] += delta

        if row == col:
            self.diagonal += delta

        if row + col == n - 1:
            self.anti_diagonal += delta

        # Check win condition
        if (abs(self.rows[row]) == n or
            abs(self.cols[col]) == n or
            abs(self.diagonal) == n or
            abs(self.anti_diagonal) == n):
            return player

        return 0


class TicTacToeSimple:
    """Simple O(n) per move solution for clarity"""

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

        # Check diagonal
        if row == col:
            if all(self.board[i][i] == player for i in range(n)):
                return player

        # Check anti-diagonal
        if row + col == n - 1:
            if all(self.board[i][n-1-i] == player for i in range(n)):
                return player

        return 0
