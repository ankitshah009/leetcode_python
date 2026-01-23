#1582. Special Positions in a Binary Matrix
#Easy
#
#Given an m x n binary matrix mat, return the number of special positions in mat.
#
#A position (i, j) is called special if mat[i][j] == 1 and all other elements in
#row i and column j are 0 (rows and columns are 0-indexed).
#
#Example 1:
#Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
#Output: 1
#Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other
#elements in row 1 and column 2 are 0.
#
#Example 2:
#Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
#Output: 3
#Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 100
#    mat[i][j] is either 0 or 1.

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Precompute row sums and column sums.
        A position is special if value is 1 and both row/col sums are 1.
        """
        m, n = len(mat), len(mat[0])

        row_sums = [sum(row) for row in mat]
        col_sums = [sum(mat[i][j] for i in range(m)) for j in range(n)]

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    count += 1

        return count


class SolutionOnePass:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Find positions where row and column have exactly one 1.
        """
        m, n = len(mat), len(mat[0])

        # Precompute
        row_sum = [sum(row) for row in mat]
        col_sum = [0] * n
        for j in range(n):
            col_sum[j] = sum(mat[i][j] for i in range(m))

        return sum(
            1 for i in range(m) for j in range(n)
            if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1
        )


class SolutionDirect:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Direct check for each cell.
        """
        m, n = len(mat), len(mat[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Check if only 1 in row and column
                    row_ok = sum(mat[i]) == 1
                    col_ok = sum(mat[r][j] for r in range(m)) == 1
                    if row_ok and col_ok:
                        count += 1

        return count


class SolutionZip:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Using zip for column sums.
        """
        m, n = len(mat), len(mat[0])
        row_sums = list(map(sum, mat))
        col_sums = list(map(sum, zip(*mat)))

        return sum(
            mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1
            for i in range(m) for j in range(n)
        )
