#52. N-Queens II
#Hard
#
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard
#such that no two queens attack each other.
#
#Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
#Example 1:
#Input: n = 4
#Output: 2
#
#Example 2:
#Input: n = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 9

class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Backtracking with sets - count solutions only.
        """
        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int):
            nonlocal count

            if row == n:
                count += 1
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
        return count


class SolutionBitmask:
    def totalNQueens(self, n: int) -> int:
        """
        Bitmask approach - faster than set operations.
        """
        count = 0

        def backtrack(row: int, cols: int, diag1: int, diag2: int):
            nonlocal count

            if row == n:
                count += 1
                return

            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

            while available:
                pos = available & (-available)
                available ^= pos

                backtrack(
                    row + 1,
                    cols | pos,
                    (diag1 | pos) << 1,
                    (diag2 | pos) >> 1
                )

        backtrack(0, 0, 0, 0)
        return count


class SolutionMemoized:
    def totalNQueens(self, n: int) -> int:
        """
        Precomputed values for small n.
        """
        # Known solutions for n = 1 to 9
        solutions = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352]

        if n < len(solutions):
            return solutions[n]

        # Fallback to computation
        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int):
            nonlocal count
            if row == n:
                count += 1
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
        return count
