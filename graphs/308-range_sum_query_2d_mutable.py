#308. Range Sum Query 2D - Mutable
#Hard
#
#Given a 2D matrix matrix, handle multiple queries of the following types:
#1. Update the value of a cell in matrix.
#2. Calculate the sum of the elements of matrix inside the rectangle.
#
#Implement the NumMatrix class:
#    NumMatrix(int[][] matrix) Initializes the object with the integer matrix.
#    void update(int row, int col, int val) Updates the value of matrix[row][col].
#    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of
#    the elements of matrix inside the rectangle.
#
#Example 1:
#Input
#["NumMatrix", "sumRegion", "update", "sumRegion"]
#[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
#Output
#[null, 8, null, 10]
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 200
#    -1000 <= matrix[i][j] <= 1000
#    0 <= row < m
#    0 <= col < n
#    -1000 <= val <= 1000
#    0 <= row1 <= row2 < m
#    0 <= col1 <= col2 < n
#    At most 5000 calls will be made to sumRegion and update.

from typing import List

class NumMatrix:
    """2D Binary Indexed Tree"""

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def _sum(self, row, col):
        """Sum from (0,0) to (row-1, col-1)"""
        total = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                total += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self._sum(row2 + 1, col2 + 1) -
                self._sum(row1, col2 + 1) -
                self._sum(row2 + 1, col1) +
                self._sum(row1, col1))


class NumMatrixSquareRoot:
    """Square root decomposition - O(sqrt(n)) per operation"""

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])

        # Row-wise prefix sums for quick row queries
        self.row_sums = []
        for row in matrix:
            prefix = [0]
            for val in row:
                prefix.append(prefix[-1] + val)
            self.row_sums.append(prefix)

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        # Update prefix sums for this row
        for j in range(col + 1, self.n + 1):
            self.row_sums[row][j] += delta

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            total += self.row_sums[i][col2 + 1] - self.row_sums[i][col1]
        return total
