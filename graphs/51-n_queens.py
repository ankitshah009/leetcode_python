#51. N-Queens
#Hard
#
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard
#such that no two queens attack each other.
#
#Given an integer n, return all distinct solutions to the n-queens puzzle. You
#may return the answer in any order.
#
#Each solution contains a distinct board configuration of the n-queens' placement,
#where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#Example 1:
#Input: n = 4
#Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
#Example 2:
#Input: n = 1
#Output: [["Q"]]
#
#Constraints:
#    1 <= n <= 9

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Backtracking with sets for O(1) conflict checking.
        """
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        board = [['.'] * n for _ in range(n)]

        def backtrack(row: int):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = '.'

        backtrack(0)
        return result


class SolutionBitmask:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Backtracking with bitmask for conflict checking.
        """
        result = []

        def backtrack(row: int, cols: int, diag1: int, diag2: int, queens: List[int]):
            if row == n:
                board = []
                for col in queens:
                    board.append('.' * col + 'Q' + '.' * (n - col - 1))
                result.append(board)
                return

            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

            while available:
                pos = available & (-available)
                available ^= pos
                col = pos.bit_length() - 1

                backtrack(
                    row + 1,
                    cols | pos,
                    (diag1 | pos) << 1,
                    (diag2 | pos) >> 1,
                    queens + [col]
                )

        backtrack(0, 0, 0, 0, [])
        return result


class SolutionArray:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Using arrays instead of sets.
        """
        result = []
        queens = [-1] * n  # queens[row] = column

        def is_valid(row: int, col: int) -> bool:
            for prev_row in range(row):
                prev_col = queens[prev_row]
                if prev_col == col:
                    return False
                if abs(prev_row - row) == abs(prev_col - col):
                    return False
            return True

        def backtrack(row: int):
            if row == n:
                board = []
                for col in queens:
                    board.append('.' * col + 'Q' + '.' * (n - col - 1))
                result.append(board)
                return

            for col in range(n):
                if is_valid(row, col):
                    queens[row] = col
                    backtrack(row + 1)
                    queens[row] = -1

        backtrack(0)
        return result
