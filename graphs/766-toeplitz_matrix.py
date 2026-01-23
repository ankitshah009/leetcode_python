#766. Toeplitz Matrix
#Easy
#
#Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
#return false.
#
#A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
#same elements.
#
#Example 1:
#Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
#Output: true
#Explanation: In the above grid, the diagonals are:
#"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
#In each diagonal all elements are the same, so the answer is True.
#
#Example 2:
#Input: matrix = [[1,2],[2,2]]
#Output: false
#Explanation: The diagonal "[1, 2]" has different elements.
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 20
#    0 <= matrix[i][j] <= 99

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        Check if each element equals its top-left neighbor.
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


class SolutionDiagonals:
    """Check each diagonal explicitly"""

    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Check diagonals starting from first column
        for start_row in range(m):
            val = matrix[start_row][0]
            r, c = start_row + 1, 1
            while r < m and c < n:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1

        # Check diagonals starting from first row (except first element)
        for start_col in range(1, n):
            val = matrix[0][start_col]
            r, c = 1, start_col + 1
            while r < m and c < n:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1

        return True


class SolutionDict:
    """Use dictionary to store diagonal values"""

    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        diagonals = {}

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                diag = i - j
                if diag in diagonals:
                    if diagonals[diag] != val:
                        return False
                else:
                    diagonals[diag] = val

        return True


class SolutionStreaming:
    """For streaming rows (memory efficient)"""

    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # Only need to compare with previous row
        prev_row = None

        for row in matrix:
            if prev_row and row[1:] != prev_row[:-1]:
                return False
            prev_row = row

        return True
