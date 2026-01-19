#52. N-Queens II
#Hard
#
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
#no two queens attack each other.
#
#Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
#Example 1:
#Input: n = 4
#Output: 2
#Explanation: There are two distinct solutions to the 4-queens puzzle.
#
#Example 2:
#Input: n = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 9

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return self.count
