#1727. Largest Submatrix With Rearrangements
#Medium
#
#You are given a binary matrix matrix of size m x n, and you are allowed to
#rearrange the columns of the matrix in any order.
#
#Return the area of the largest submatrix within matrix where every element of
#the submatrix is 1 after reordering the columns optimally.
#
#Example 1:
#Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
#Output: 4
#
#Example 2:
#Input: matrix = [[1,0,1,0,1]]
#Output: 3
#
#Example 3:
#Input: matrix = [[1,1,0],[1,0,1]]
#Output: 2
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m * n <= 10^5
#    matrix[i][j] is either 0 or 1.

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        For each row, compute heights (consecutive 1s above including current).
        Sort heights in each row and compute max area.
        """
        m, n = len(matrix), len(matrix[0])

        # Compute heights
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        max_area = 0

        for row in matrix:
            # Sort heights in descending order
            sorted_row = sorted(row, reverse=True)

            # For each position, area = height * width
            for j, height in enumerate(sorted_row):
                if height == 0:
                    break
                width = j + 1
                max_area = max(max_area, height * width)

        return max_area


class SolutionOptimized:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        Process without modifying original matrix.
        """
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            # Update heights
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Sort and compute area
            sorted_heights = sorted(heights, reverse=True)
            for j, h in enumerate(sorted_heights):
                if h == 0:
                    break
                max_area = max(max_area, h * (j + 1))

        return max_area


class SolutionWithoutSort:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        """
        Track previous sorted order to avoid full sort each row.
        """
        m, n = len(matrix), len(matrix[0])

        # Start with column indices
        prev_heights = [(0, j) for j in range(n)]
        max_area = 0

        for i in range(m):
            # Update heights and sort
            heights = []
            for j in range(n):
                h = prev_heights[j][0]
                col = prev_heights[j][1]
                if matrix[i][col] == 1:
                    heights.append((h + 1, col))
                else:
                    heights.append((0, col))

            # Sort by height descending
            heights.sort(reverse=True)
            prev_heights = heights

            # Compute max area
            for j, (h, _) in enumerate(heights):
                if h == 0:
                    break
                max_area = max(max_area, h * (j + 1))

        return max_area
