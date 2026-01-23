#1252. Cells with Odd Values in a Matrix
#Easy
#
#There is an m x n matrix that is initialized to all 0's. There is also a 2D
#array indices where each indices[i] = [ri, ci] represents a 0-indexed location
#to perform some increment operations on the matrix.
#
#For each location indices[i], do both of the following:
#    Increment all the cells on row ri.
#    Increment all the cells on column ci.
#
#Given m, n, and indices, return the number of odd-valued cells in the matrix
#after applying the increment to all locations in indices.
#
#Example 1:
#Input: m = 2, n = 3, indices = [[0,1],[1,1]]
#Output: 6
#Explanation: Initial matrix = [[0,0,0],[0,0,0]].
#After applying first index: [[1,2,1],[0,1,0]].
#After applying second index: [[1,3,1],[1,3,1]].
#There are 6 odd numbers in the final matrix.
#
#Example 2:
#Input: m = 2, n = 2, indices = [[1,1],[0,0]]
#Output: 0
#Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers.
#
#Constraints:
#    1 <= m, n <= 50
#    1 <= indices.length <= 100
#    0 <= ri < m
#    0 <= ci < n

from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        """
        Count increments for each row and column.
        Cell (i, j) is odd if row_count[i] + col_count[j] is odd.
        """
        row_count = [0] * m
        col_count = [0] * n

        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        # Count cells with odd total
        odd_rows = sum(1 for x in row_count if x % 2 == 1)
        odd_cols = sum(1 for x in col_count if x % 2 == 1)

        # Cell is odd if exactly one of (row, col) has odd count
        # = odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols


class SolutionSimulation:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        """Direct simulation"""
        matrix = [[0] * n for _ in range(m)]

        for r, c in indices:
            for j in range(n):
                matrix[r][j] += 1
            for i in range(m):
                matrix[i][c] += 1

        return sum(1 for row in matrix for cell in row if cell % 2 == 1)
