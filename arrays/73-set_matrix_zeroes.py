#73. Set Matrix Zeroes
#Medium
#
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
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

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Mark zeros in first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeros based on marks
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
