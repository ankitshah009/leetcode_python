#74. Search a 2D Matrix
#Medium
#
#You are given an m x n integer matrix matrix with the following two properties:
#- Each row is sorted in non-decreasing order.
#- The first integer of each row is greater than the last integer of the previous
#  row.
#
#Given an integer target, return true if target is in matrix or false otherwise.
#
#You must write a solution in O(log(m * n)) time complexity.
#
#Example 1:
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true
#
#Example 2:
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: false
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 100
#    -10^4 <= matrix[i][j], target <= 10^4

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Treat as 1D sorted array - single binary search.
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


class SolutionTwoBinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Two binary searches - find row, then search in row.
        """
        m, n = len(matrix), len(matrix[0])

        # Binary search for row
        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        else:
            return False

        row = (top + bottom) // 2

        # Binary search in row
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


class SolutionStaircase:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Start from top-right corner - O(m + n).
        """
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False


class SolutionBisect:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Using bisect module.
        """
        import bisect

        m, n = len(matrix), len(matrix[0])

        # Find potential row
        first_col = [row[0] for row in matrix]
        row = bisect.bisect_right(first_col, target) - 1

        if row < 0:
            return False

        # Search in row
        col = bisect.bisect_left(matrix[row], target)
        return col < n and matrix[row][col] == target
