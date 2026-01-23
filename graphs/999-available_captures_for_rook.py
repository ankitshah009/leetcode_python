#999. Available Captures for Rook
#Easy
#
#On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of
#white bishops 'B', black pawns 'p', and empty squares '.'.
#
#When the rook moves, it chooses one of four cardinal directions (north, east,
#south, or west), then moves in that direction until it chooses to stop, reaches
#the edge of the board, captures a black pawn, or is blocked by a white bishop.
#
#Return the number of black pawns the rook can capture in one move.
#
#Example 1:
#Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
#Output: 3
#
#Constraints:
#    board.length == 8
#    board[i].length == 8
#    board[i][j] is either 'R', '.', 'B', or 'p'.
#    There is exactly one cell with board[i][j] == 'R'.

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        """
        Find rook, check 4 directions.
        """
        # Find rook position
        rook_r, rook_c = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_r, rook_c = i, j
                    break

        captures = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            r, c = rook_r + dr, rook_c + dc

            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 'B':
                    break  # Blocked by bishop
                if board[r][c] == 'p':
                    captures += 1
                    break  # Captured pawn

                r += dr
                c += dc

        return captures


class SolutionExplicit:
    """More explicit direction checking"""

    def numRookCaptures(self, board: list[list[str]]) -> int:
        # Find rook
        rook_pos = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_pos = (i, j)
                    break
            if rook_pos:
                break

        r, c = rook_pos
        captures = 0

        # Check up
        for i in range(r - 1, -1, -1):
            if board[i][c] == 'B':
                break
            if board[i][c] == 'p':
                captures += 1
                break

        # Check down
        for i in range(r + 1, 8):
            if board[i][c] == 'B':
                break
            if board[i][c] == 'p':
                captures += 1
                break

        # Check left
        for j in range(c - 1, -1, -1):
            if board[r][j] == 'B':
                break
            if board[r][j] == 'p':
                captures += 1
                break

        # Check right
        for j in range(c + 1, 8):
            if board[r][j] == 'B':
                break
            if board[r][j] == 'p':
                captures += 1
                break

        return captures
