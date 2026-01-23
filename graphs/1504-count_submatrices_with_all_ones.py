#1504. Count Submatrices With All Ones
#Medium
#
#Given an m x n binary matrix mat, return the number of submatrices that have
#all ones.
#
#Example 1:
#Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
#Output: 13
#Explanation:
#There are 6 rectangles of side 1x1.
#There are 2 rectangles of side 1x2.
#There are 3 rectangles of side 2x1.
#There are 1 rectangle of side 2x2.
#There are 1 rectangle of side 3x1.
#From Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
#
#Example 2:
#Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
#Output: 24
#Explanation:
#There are 8 rectangles of side 1x1.
#There are 5 rectangles of side 1x2.
#There are 2 rectangles of side 1x3.
#There are 4 rectangles of side 2x1.
#There are 2 rectangles of side 2x2.
#There are 2 rectangles of side 3x1.
#There are 1 rectangle of side 3x2.
#From Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
#
#Constraints:
#    1 <= m, n <= 150
#    mat[i][j] is either 0 or 1.

from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        For each cell, compute height of consecutive 1's above.
        Then for each row, count submatrices ending at that row.
        Use monotonic stack to efficiently count.
        """
        if not mat or not mat[0]:
            return 0

        m, n = len(mat), len(mat[0])

        # Compute heights (consecutive 1's above including current)
        heights = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i - 1][j] + 1 if i > 0 else 1

        total = 0

        # For each row, count submatrices ending at this row
        for i in range(m):
            total += self.countWithStack(heights[i])

        return total

    def countWithStack(self, heights: List[int]) -> int:
        """
        Count submatrices in a histogram.
        For each bar, count rectangles where this bar is the rightmost.
        """
        n = len(heights)
        stack = []  # (index, height, count of rectangles)
        count = 0
        total = 0

        for i in range(n):
            h = heights[i]
            curr_count = 0

            # Pop taller bars
            while stack and stack[-1][1] >= h:
                idx, height, cnt = stack.pop()
                curr_count += cnt

            # Rectangles with height h, ending at column i
            curr_count += 1  # Just this column

            # Add contribution
            total += curr_count * h

            stack.append((i, h, curr_count))

        return total


class SolutionDP:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        DP approach: for each cell (i,j), count submatrices ending at (i,j).
        """
        m, n = len(mat), len(mat[0])
        total = 0

        # heights[j] = height of consecutive 1s ending at current row, column j
        heights = [0] * n

        for i in range(m):
            for j in range(n):
                # Update height
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Count submatrices ending at row i
            for j in range(n):
                if heights[j] == 0:
                    continue

                # Count submatrices with right edge at column j
                min_height = heights[j]
                for k in range(j, -1, -1):
                    if heights[k] == 0:
                        break
                    min_height = min(min_height, heights[k])
                    total += min_height

        return total


class SolutionOptimized:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Optimized O(m*n) solution using monotonic stack.
        """
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            # Update heights
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] else 0

            # Count using monotonic stack
            stack = []  # (index, count)
            sum_count = 0

            for j in range(n):
                count = 1

                while stack and heights[stack[-1][0]] >= heights[j]:
                    _, prev_count = stack.pop()
                    count += prev_count

                sum_count -= count * (heights[stack[-1][0]] if stack else 0)
                sum_count += count * heights[j]

                stack.append((j, count))
                total += sum_count

        return total
