#85. Maximal Rectangle
#Hard
#
#Given a rows x cols binary matrix filled with 0's and 1's, find the largest
#rectangle containing only 1's and return its area.
#
#Example 1:
#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 6
#
#Example 2:
#Input: matrix = [["0"]]
#Output: 0
#
#Example 3:
#Input: matrix = [["1"]]
#Output: 1
#
#Constraints:
#    rows == matrix.length
#    cols == matrix[i].length
#    1 <= rows, cols <= 200
#    matrix[i][j] is '0' or '1'.

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Histogram approach - build heights for each row, apply largest rectangle.
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram heights
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            # Find largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleInHistogram(heights))

        return max_area

    def largestRectangleInHistogram(self, heights: List[int]) -> int:
        """Monotonic stack for largest rectangle."""
        stack = []
        max_area = 0
        heights = heights + [0]  # Sentinel

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


class SolutionDP:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        DP approach - track height, left, and right boundaries.
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols
        left = [0] * cols
        right = [cols] * cols
        max_area = 0

        for row in matrix:
            # Update height
            for j in range(cols):
                height[j] = height[j] + 1 if row[j] == '1' else 0

            # Update left boundary
            cur_left = 0
            for j in range(cols):
                if row[j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            # Update right boundary
            cur_right = cols
            for j in range(cols - 1, -1, -1):
                if row[j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = cols
                    cur_right = j

            # Calculate max area
            for j in range(cols):
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area


class SolutionBruteForce:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Brute force - check all possible rectangles.
        O(n^2 * m^2) time complexity.
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_area = 0

        # Precompute width at each position
        width = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    width[i][j] = 1 if j == 0 else width[i][j - 1] + 1

        # For each cell, expand upward to find rectangles
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '0':
                    continue

                min_width = width[i][j]
                for k in range(i, -1, -1):
                    if matrix[k][j] == '0':
                        break
                    min_width = min(min_width, width[k][j])
                    height = i - k + 1
                    max_area = max(max_area, min_width * height)

        return max_area
