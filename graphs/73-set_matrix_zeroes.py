#73. Set Matrix Zeroes
#Medium
#
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and
#column to 0's.
#
#You must do it in place.
#
#Example 1:
#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#Example 2:
#Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#Constraints:
#    m == matrix.length
#    n == matrix[0].length
#    1 <= m, n <= 200
#    -2^31 <= matrix[i][j] <= 2^31 - 1
#
#Follow up:
#- A straightforward solution using O(mn) space is probably a bad idea.
#- A simple improvement uses O(m + n) space, but still not the best solution.
#- Could you devise a constant space solution?

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        O(1) space - use first row/column as markers.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row/column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


class SolutionOMN:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        O(m + n) space using sets.
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # Find all zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set zeros
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0


class SolutionOmn:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        O(mn) space - store copy (not recommended).
        """
        m, n = len(matrix), len(matrix[0])
        copy = [row[:] for row in matrix]

        for i in range(m):
            for j in range(n):
                if copy[i][j] == 0:
                    # Set row to zero
                    for k in range(n):
                        matrix[i][k] = 0
                    # Set column to zero
                    for k in range(m):
                        matrix[k][j] = 0
