#37. Sudoku Solver
#Hard
#
#Write a program to solve a Sudoku puzzle by filling the empty cells.
#
#A sudoku solution must satisfy all of the following rules:
#1. Each of the digits 1-9 must occur exactly once in each row.
#2. Each of the digits 1-9 must occur exactly once in each column.
#3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.
#
#The '.' character indicates empty cells.
#
#Example 1:
#Input: board =
#[["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]
#Output: [["5","3","4","6","7","8","9","1","2"],
#         ["6","7","2","1","9","5","3","4","8"],
#         ["1","9","8","3","4","2","5","6","7"],
#         ["8","5","9","7","6","1","4","2","3"],
#         ["4","2","6","8","5","3","7","9","1"],
#         ["7","1","3","9","2","4","8","5","6"],
#         ["9","6","1","5","3","7","2","8","4"],
#         ["2","8","7","4","1","9","6","3","5"],
#         ["3","4","5","2","8","6","1","7","9"]]
#
#Constraints:
#    board.length == 9
#    board[i].length == 9
#    board[i][j] is a digit or '.'.
#    It is guaranteed that the input board has only one solution.

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Backtracking with constraint propagation.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize constraints
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + j // 3].add(num)

        def backtrack(idx: int) -> bool:
            if idx == len(empty):
                return True

            i, j = empty[idx]
            box_idx = (i // 3) * 3 + j // 3

            for num in '123456789':
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(idx + 1):
                        return True

                    # Backtrack
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack(0)


class SolutionBitmask:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Backtracking with bitmask constraints.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        # Initialize constraints
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    bit = 1 << num
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit

        def backtrack(i: int, j: int) -> bool:
            if i == 9:
                return True
            if j == 9:
                return backtrack(i + 1, 0)
            if board[i][j] != '.':
                return backtrack(i, j + 1)

            box_idx = (i // 3) * 3 + j // 3
            available = ~(rows[i] | cols[j] | boxes[box_idx]) & 0x3FE

            while available:
                bit = available & (-available)
                available ^= bit
                num = bit.bit_length() - 1

                board[i][j] = str(num)
                rows[i] |= bit
                cols[j] |= bit
                boxes[box_idx] |= bit

                if backtrack(i, j + 1):
                    return True

                board[i][j] = '.'
                rows[i] ^= bit
                cols[j] ^= bit
                boxes[box_idx] ^= bit

            return False

        backtrack(0, 0)


class SolutionSimple:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Simple backtracking without optimization.
        """
        def is_valid(board: List[List[str]], row: int, col: int, num: str) -> bool:
            # Check row
            if num in board[row]:
                return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve(board: List[List[str]]) -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)
