#48. Rotate Image
#Medium
#
#You are given an n x n 2D matrix representing an image, rotate the image by 90
#degrees (clockwise).
#
#You have to rotate the image in-place, which means you have to modify the input
#2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#Example 1:
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#Example 2:
#Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#Constraints:
#    n == matrix.length == matrix[i].length
#    1 <= n <= 20
#    -1000 <= matrix[i][j] <= 1000

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Transpose + Reverse each row.
        90° clockwise = transpose + reverse rows.
        """
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()


class SolutionFourWay:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate four cells at a time, layer by layer.
        """
        n = len(matrix)

        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                # Save top
                top = matrix[first][i]

                # Left -> Top
                matrix[first][i] = matrix[last - offset][first]

                # Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset]

                # Right -> Bottom
                matrix[last][last - offset] = matrix[i][last]

                # Top -> Right
                matrix[i][last] = top


class SolutionReverseTwice:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Reverse up-down, then transpose.
        Alternative: 90° clockwise = reverse rows + transpose.
        """
        n = len(matrix)

        # Reverse rows (up-down)
        matrix.reverse()

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class SolutionCounterClockwise:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        For 90° counter-clockwise: transpose + reverse columns.
        This is for 90° clockwise.
        """
        n = len(matrix)

        # For 90° clockwise: transpose then reverse rows
        # For 90° counter-clockwise: reverse rows then transpose

        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()
