#36. Valid Sudoku
#Medium
#
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
#validated according to the following rules:
#
#1. Each row must contain the digits 1-9 without repetition.
#2. Each column must contain the digits 1-9 without repetition.
#3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
#   without repetition.
#
#Note:
#- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#- Only the filled cells need to be validated according to the mentioned rules.
#
#Example 1:
#Input: board =
#[["5","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: true
#
#Example 2:
#Input: board =
#[["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: false
#
#Constraints:
#    board.length == 9
#    board[i].length == 9
#    board[i][j] is a digit 1-9 or '.'.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Use sets to track seen numbers in rows, columns, and boxes.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue

                # Calculate box index
                box_idx = (i // 3) * 3 + (j // 3)

                # Check for duplicates
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)

        return True


class SolutionSingleSet:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Use a single set with encoded keys.
        """
        seen = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue

                row_key = f"row{i}:{num}"
                col_key = f"col{j}:{num}"
                box_key = f"box{i // 3},{j // 3}:{num}"

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True


class SolutionBitmask:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Use bitmasks for space efficiency.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                bit = 1 << num
                box_idx = (i // 3) * 3 + (j // 3)

                if (rows[i] & bit) or (cols[j] & bit) or (boxes[box_idx] & bit):
                    return False

                rows[i] |= bit
                cols[j] |= bit
                boxes[box_idx] |= bit

        return True


class SolutionArray:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Using boolean arrays instead of sets.
        """
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = int(board[i][j])
                box_idx = (i // 3) * 3 + (j // 3)

                if rows[i][num] or cols[j][num] or boxes[box_idx][num]:
                    return False

                rows[i][num] = True
                cols[j][num] = True
                boxes[box_idx][num] = True

        return True
