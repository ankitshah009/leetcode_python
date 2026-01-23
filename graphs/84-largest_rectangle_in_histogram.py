#84. Largest Rectangle in Histogram
#Hard
#
#Given an array of integers heights representing the histogram's bar height where
#the width of each bar is 1, return the area of the largest rectangle in the
#histogram.
#
#Example 1:
#Input: heights = [2,1,5,6,2,3]
#Output: 10
#Explanation: The largest rectangle has an area = 10 units (5 * 2 = 10).
#
#Example 2:
#Input: heights = [2,4]
#Output: 4
#
#Constraints:
#    1 <= heights.length <= 10^5
#    0 <= heights[i] <= 10^4

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Monotonic stack approach - O(n) time.
        """
        stack = []  # Indices of heights in increasing order
        max_area = 0
        heights.append(0)  # Sentinel to flush stack

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Remove sentinel
        return max_area


class SolutionTwoPass:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Precompute left and right boundaries using stack.
        """
        n = len(heights)
        left_bound = [0] * n
        right_bound = [n] * n

        # Find left boundary (first smaller element to the left)
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left_bound[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        # Find right boundary (first smaller element to the right)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right_bound[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate max area
        max_area = 0
        for i in range(n):
            area = heights[i] * (right_bound[i] - left_bound[i])
            max_area = max(max_area, area)

        return max_area


class SolutionDivideConquer:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Divide and conquer - O(n log n) average.
        """
        def helper(left: int, right: int) -> int:
            if left > right:
                return 0

            min_idx = left
            for i in range(left, right + 1):
                if heights[i] < heights[min_idx]:
                    min_idx = i

            return max(
                heights[min_idx] * (right - left + 1),
                helper(left, min_idx - 1),
                helper(min_idx + 1, right)
            )

        return helper(0, len(heights) - 1)


class SolutionBruteForce:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Brute force - O(n^2) - for comparison.
        """
        max_area = 0
        n = len(heights)

        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                max_area = max(max_area, area)

        return max_area
