#74. Search a 2D Matrix
#Medium
#
#You are given an m x n integer matrix matrix with the following two properties:
#    Each row is sorted in non-decreasing order.
#    The first integer of each row is greater than the last integer of the previous row.
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

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

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
