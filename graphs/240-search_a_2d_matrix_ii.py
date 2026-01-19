#240. Search a 2D Matrix II
#Medium
#
#Write an efficient algorithm that searches for a value target in an m x n
#integer matrix. This matrix has the following properties:
#    Integers in each row are sorted in ascending from left to right.
#    Integers in each column are sorted in ascending from top to bottom.
#
#Example 1:
#Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
#Output: true
#
#Example 2:
#Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
#Output: false
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= n, m <= 300
#    -10^9 <= matrix[i][j] <= 10^9
#    All the integers in each row are sorted in ascending order.
#    All the integers in each column are sorted in ascending order.
#    -10^9 <= target <= 10^9

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Start from top-right corner (or bottom-left).
        O(m + n) time complexity.
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Target must be in a column to the left
            else:
                row += 1  # Target must be in a row below

        return False


class SolutionBottomLeft:
    """Start from bottom-left corner"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1

        return False


class SolutionBinarySearch:
    """Binary search on each row - O(m log n)"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import bisect

        for row in matrix:
            # Skip row if target is out of range
            if row[0] > target or row[-1] < target:
                continue

            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True

        return False


class SolutionDivideConquer:
    """Divide and conquer - O(n log n)"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        def search(row_start, row_end, col_start, col_end):
            if row_start > row_end or col_start > col_end:
                return False

            mid_row = (row_start + row_end) // 2
            mid_col = (col_start + col_end) // 2
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True
            elif mid_val < target:
                # Exclude top-left quadrant
                return (search(mid_row + 1, row_end, col_start, col_end) or
                        search(row_start, mid_row, mid_col + 1, col_end))
            else:
                # Exclude bottom-right quadrant
                return (search(row_start, mid_row - 1, col_start, col_end) or
                        search(mid_row, row_end, col_start, mid_col - 1))

        return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
