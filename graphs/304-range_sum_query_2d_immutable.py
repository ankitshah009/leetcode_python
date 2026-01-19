#304. Range Sum Query 2D - Immutable
#Medium
#
#Given a 2D matrix matrix, handle multiple queries of the following type:
#Calculate the sum of the elements of matrix inside the rectangle defined by
#its upper left corner (row1, col1) and lower right corner (row2, col2).
#
#Implement the NumMatrix class:
#    NumMatrix(int[][] matrix) Initializes the object with the integer matrix.
#    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of
#    the elements of matrix inside the rectangle.
#
#Example 1:
#Input
#["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
#[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
#Output
#[null, 8, 11, 12]
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 200
#    -10^4 <= matrix[i][j] <= 10^4
#    0 <= row1 <= row2 < m
#    0 <= col1 <= col2 < n
#    At most 10^4 calls will be made to sumRegion.

from typing import List

class NumMatrix:
    """2D prefix sum - O(mn) preprocessing, O(1) query"""

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        m, n = len(matrix), len(matrix[0])

        # prefix[i][j] = sum of matrix[0..i-1][0..j-1]
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix[i][j] = (
                    matrix[i-1][j-1] +
                    self.prefix[i-1][j] +
                    self.prefix[i][j-1] -
                    self.prefix[i-1][j-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Inclusion-exclusion principle
        return (
            self.prefix[row2 + 1][col2 + 1] -
            self.prefix[row1][col2 + 1] -
            self.prefix[row2 + 1][col1] +
            self.prefix[row1][col1]
        )


class NumMatrixBruteForce:
    """Brute force - O(1) preprocessing, O(mn) query"""

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                total += self.matrix[i][j]
        return total


class NumMatrixRowPrefix:
    """Row-wise prefix sum - O(mn) preprocessing, O(m) query"""

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        m, n = len(matrix), len(matrix[0])

        # Row-wise prefix sums
        self.prefix = [[0] * (n + 1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                self.prefix[i][j + 1] = self.prefix[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            total += self.prefix[i][col2 + 1] - self.prefix[i][col1]
        return total
