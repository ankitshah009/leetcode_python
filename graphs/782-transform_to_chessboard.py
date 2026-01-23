#782. Transform to Chessboard
#Hard
#
#You are given an n x n binary grid board. In each move, you can swap any two
#rows with each other, or any two columns with each other.
#
#Return the minimum number of moves to transform the board into a "chessboard"
#- a board where no 0's and no 1's are 4-directionally adjacent. If the task is
#impossible, return -1.
#
#Example 1:
#Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
#Output: 2
#Explanation: One potential sequence of moves is shown.
#
#Example 2:
#Input: board = [[0,1],[1,0]]
#Output: 0
#
#Example 3:
#Input: board = [[1,0],[1,0]]
#Output: -1
#
#Constraints:
#    n == board.length
#    n == board[i].length
#    2 <= n <= 30
#    board[i][j] is either 0 or 1.

class Solution:
    def movesToChessboard(self, board: list[list[int]]) -> int:
        n = len(board)

        # Check validity: only 2 types of rows/cols allowed
        row_set = set(tuple(row) for row in board)
        if len(row_set) != 2:
            return -1

        row1, row2 = row_set
        # Rows must be complements
        if not all(a ^ b for a, b in zip(row1, row2)):
            return -1

        # Check column counts
        col_set = set(tuple(board[i][j] for i in range(n)) for j in range(n))
        if len(col_set) != 2:
            return -1

        col1, col2 = col_set
        if not all(a ^ b for a, b in zip(col1, col2)):
            return -1

        # Count occurrences
        row1_count = sum(1 for row in board if tuple(row) == row1)
        col1_count = sum(1 for j in range(n) if tuple(board[i][j] for i in range(n)) == col1)

        # For valid chessboard, counts must be n//2 and (n+1)//2
        if not (row1_count == n // 2 or row1_count == (n + 1) // 2):
            return -1
        if not (col1_count == n // 2 or col1_count == (n + 1) // 2):
            return -1

        # Count mismatches for row/col swaps
        def count_swaps(line, n):
            # Count elements not matching 010101... pattern
            ones_even = sum(1 for i in range(n) if i % 2 == 0 and line[i] == 1)
            ones_odd = sum(1 for i in range(n) if i % 2 == 1 and line[i] == 1)

            if n % 2 == 0:
                # Both patterns possible, choose min
                return min(ones_even, ones_odd)
            else:
                # Only one pattern valid
                # If more 1s, 1 must start at even positions
                if sum(line) > n // 2:
                    return ones_odd
                else:
                    return ones_even

        first_row = board[0]
        first_col = [board[i][0] for i in range(n)]

        return count_swaps(first_row, n) + count_swaps(first_col, n)
