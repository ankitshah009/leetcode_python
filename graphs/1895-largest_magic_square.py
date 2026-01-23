#1895. Largest Magic Square
#Medium
#
#A k x k magic square is a k x k grid filled with integers such that every row
#sum, every column sum, and both diagonal sums are all equal. The integers in
#the magic square do not have to be distinct.
#
#Given an m x n integer grid, return the size (i.e., the side length k) of the
#largest magic square that can be found within this grid.
#
#Example 1:
#Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
#Output: 3
#
#Example 2:
#Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
#Output: 2
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 50
#    1 <= grid[i][j] <= 10^6

from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        Precompute prefix sums for rows and columns.
        Check each possible square.
        """
        m, n = len(grid), len(grid[0])

        # Row prefix sums
        row_sum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]

        # Column prefix sums
        col_sum = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]

        def get_row_sum(r, c1, c2):
            """Sum of row r from column c1 to c2 inclusive."""
            return row_sum[r][c2 + 1] - row_sum[r][c1]

        def get_col_sum(c, r1, r2):
            """Sum of column c from row r1 to r2 inclusive."""
            return col_sum[r2 + 1][c] - col_sum[r1][c]

        def is_magic(r, c, k):
            """Check if k x k square starting at (r, c) is magic."""
            target = get_row_sum(r, c, c + k - 1)

            # Check all rows
            for i in range(r, r + k):
                if get_row_sum(i, c, c + k - 1) != target:
                    return False

            # Check all columns
            for j in range(c, c + k):
                if get_col_sum(j, r, r + k - 1) != target:
                    return False

            # Check main diagonal
            diag1 = sum(grid[r + i][c + i] for i in range(k))
            if diag1 != target:
                return False

            # Check anti-diagonal
            diag2 = sum(grid[r + i][c + k - 1 - i] for i in range(k))
            if diag2 != target:
                return False

            return True

        # Check from largest possible size down
        max_k = min(m, n)

        for k in range(max_k, 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k

        return 1


class SolutionBruteForce:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        Brute force without prefix sums.
        """
        m, n = len(grid), len(grid[0])

        def check_magic(r, c, k):
            target = sum(grid[r][c:c+k])

            # Rows
            for i in range(k):
                if sum(grid[r+i][c:c+k]) != target:
                    return False

            # Columns
            for j in range(k):
                if sum(grid[r+i][c+j] for i in range(k)) != target:
                    return False

            # Diagonals
            if sum(grid[r+i][c+i] for i in range(k)) != target:
                return False
            if sum(grid[r+i][c+k-1-i] for i in range(k)) != target:
                return False

            return True

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if check_magic(r, c, k):
                        return k

        return 1
