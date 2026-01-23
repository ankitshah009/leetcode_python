#59. Spiral Matrix II
#Medium
#
#Given a positive integer n, generate an n x n matrix filled with elements from
#1 to n^2 in spiral order.
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

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Layer by layer approach with boundaries.
        """
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
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


class SolutionDirection:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Direction-based simulation.
        """
        matrix = [[0] * n for _ in range(n)]

        # Direction vectors: right, down, left, up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        row = col = direction = 0

        for num in range(1, n * n + 1):
            matrix[row][col] = num

            # Try next cell in current direction
            next_row = row + dr[direction]
            next_col = col + dc[direction]

            # Change direction if needed
            if (next_row < 0 or next_row >= n or
                next_col < 0 or next_col >= n or
                matrix[next_row][next_col] != 0):
                direction = (direction + 1) % 4
                next_row = row + dr[direction]
                next_col = col + dc[direction]

            row, col = next_row, next_col

        return matrix


class SolutionRecursive:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Recursive layer peeling approach.
        """
        matrix = [[0] * n for _ in range(n)]

        def fill_layer(start: int, end: int, num: int):
            if start > end:
                return num

            if start == end:
                matrix[start][start] = num
                return num + 1

            # Top row
            for col in range(start, end + 1):
                matrix[start][col] = num
                num += 1

            # Right column
            for row in range(start + 1, end + 1):
                matrix[row][end] = num
                num += 1

            # Bottom row
            for col in range(end - 1, start - 1, -1):
                matrix[end][col] = num
                num += 1

            # Left column
            for row in range(end - 1, start, -1):
                matrix[row][start] = num
                num += 1

            return fill_layer(start + 1, end - 1, num)

        fill_layer(0, n - 1, 1)
        return matrix
