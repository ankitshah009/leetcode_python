#85. Maximal Rectangle
#Hard
#
#Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle
#containing only 1's and return its area.
#
#Example 1:
#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 6
#Explanation: The maximal rectangle is shown in the above picture.
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

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights = heights + [0]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
