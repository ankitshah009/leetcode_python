#54. Spiral Matrix
#Medium
#
#Given an m x n matrix, return all elements of the matrix in spiral order.
#
#Example 1:
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
#
#Example 2:
#Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 10
#    -100 <= matrix[i][j] <= 100

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Layer by layer approach with boundaries.
        """
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # Traverse left
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # Traverse up
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


class SolutionDirection:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Direction-based simulation.
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []
        seen = [[False] * n for _ in range(m)]

        # Direction vectors: right, down, left, up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        row = col = direction = 0

        for _ in range(m * n):
            result.append(matrix[row][col])
            seen[row][col] = True

            # Try next cell in current direction
            next_row = row + dr[direction]
            next_col = col + dc[direction]

            # Change direction if needed
            if (next_row < 0 or next_row >= m or
                next_col < 0 or next_col >= n or
                seen[next_row][next_col]):
                direction = (direction + 1) % 4
                next_row = row + dr[direction]
                next_col = col + dc[direction]

            row, col = next_row, next_col

        return result


class SolutionRecursive:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Recursive approach - peel off outer layer.
        """
        if not matrix or not matrix[0]:
            return []

        result = list(matrix[0])  # Top row

        if len(matrix) == 1:
            return result

        # Rotate remaining matrix counterclockwise and recurse
        remaining = list(zip(*matrix[1:]))[::-1]
        return result + self.spiralOrder([list(row) for row in remaining])
