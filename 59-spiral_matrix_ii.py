#59. Spiral Matrix II
#Medium
#
#Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in
#spiral order.
#
#Example 1:
#Input: n = 3
#Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#Example 2:
#Input: n = 1
#Output: [[1]]
#
#Constraints:
#    1 <= n <= 20

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # Fill right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Fill down
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Fill left
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            # Fill up
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix
