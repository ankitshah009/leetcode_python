#723. Candy Crush
#Medium
#
#This question is about implementing a basic elimination algorithm for Candy
#Crush.
#
#Given an m x n integer array board representing the grid of candy where
#board[i][j] represents the type of candy. A value of board[i][j] == 0
#represents that the cell is empty.
#
#The given board represents the state of the game following the player's move.
#Now, you need to restore the board to a stable state by crushing candies
#according to the following rules:
#
#1. If three or more candies of the same type are adjacent vertically or
#   horizontally, crush them all at the same time - these positions become empty.
#2. After crushing all candies simultaneously, if an empty space on the board
#   has candies on top of itself, then these candies will drop until they hit
#   a candy or the bottom at the same time. No new candies will drop outside
#   the top boundary.
#3. After the above steps, there may exist more candies that can be crushed.
#   If so, you need to repeat the above steps.
#4. If there does not exist more candies that can be crushed, then return the
#   current board.
#
#Example:
#Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],
#                [410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],
#                [710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
#Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],
#         [310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],
#         [710,311,412,613,714],[810,411,512,713,1014]]
#
#Constraints:
#    m == board.length
#    n == board[i].length
#    3 <= m, n <= 50
#    1 <= board[i][j] <= 2000

class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        """
        Repeatedly mark, crush, and drop until stable.
        """
        m, n = len(board), len(board[0])

        def mark_and_crush():
            # Mark cells to crush (use negative values)
            crushed = False

            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0:
                        continue

                    val = abs(board[i][j])

                    # Check horizontal
                    if j + 2 < n and abs(board[i][j+1]) == val and abs(board[i][j+2]) == val:
                        board[i][j] = board[i][j+1] = board[i][j+2] = -val
                        crushed = True

                    # Check vertical
                    if i + 2 < m and abs(board[i+1][j]) == val and abs(board[i+2][j]) == val:
                        board[i][j] = board[i+1][j] = board[i+2][j] = -val
                        crushed = True

            # Actually crush (set to 0)
            for i in range(m):
                for j in range(n):
                    if board[i][j] < 0:
                        board[i][j] = 0

            return crushed

        def drop():
            # Drop candies down to fill empty spaces
            for j in range(n):
                write_row = m - 1

                for read_row in range(m - 1, -1, -1):
                    if board[read_row][j] != 0:
                        board[write_row][j] = board[read_row][j]
                        write_row -= 1

                # Fill remaining with 0
                while write_row >= 0:
                    board[write_row][j] = 0
                    write_row -= 1

        while mark_and_crush():
            drop()

        return board


class SolutionExplicit:
    """More explicit marking with sets"""

    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        m, n = len(board), len(board[0])

        while True:
            to_crush = set()

            # Find horizontal matches
            for i in range(m):
                for j in range(n - 2):
                    if board[i][j] and board[i][j] == board[i][j+1] == board[i][j+2]:
                        to_crush |= {(i, j), (i, j+1), (i, j+2)}

            # Find vertical matches
            for i in range(m - 2):
                for j in range(n):
                    if board[i][j] and board[i][j] == board[i+1][j] == board[i+2][j]:
                        to_crush |= {(i, j), (i+1, j), (i+2, j)}

            if not to_crush:
                break

            # Crush
            for i, j in to_crush:
                board[i][j] = 0

            # Drop
            for j in range(n):
                write = m - 1
                for read in range(m - 1, -1, -1):
                    if board[read][j]:
                        board[write][j] = board[read][j]
                        write -= 1
                for i in range(write + 1):
                    board[i][j] = 0

        return board
