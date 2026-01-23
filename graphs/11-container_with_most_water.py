#11. Container With Most Water
#Medium
#
#You are given an integer array height of length n. There are n vertical lines
#drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
#Find two lines that together with the x-axis form a container, such that the
#container contains the most water.
#
#Return the maximum amount of water a container can store.
#
#Notice that you may not slant the container.
#
#Example 1:
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The vertical lines are drawn at indices 0-8. The max area is
#between index 1 and 8: min(8,7) * (8-1) = 7 * 7 = 49.
#
#Example 2:
#Input: height = [1,1]
#Output: 1
#
#Constraints:
#    n == height.length
#    2 <= n <= 10^5
#    0 <= height[i] <= 10^4

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointer approach - O(n) time, O(1) space.
        Move the pointer with smaller height inward.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class SolutionOptimized:
    def maxArea(self, height: List[int]) -> int:
        """
        Optimized two pointers - skip heights that can't improve.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h_left, h_right = height[left], height[right]
            area = (right - left) * min(h_left, h_right)
            max_area = max(max_area, area)

            # Skip all heights smaller than current minimum
            if h_left < h_right:
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                while left < right and height[right] <= h_right:
                    right -= 1

        return max_area


class SolutionBruteForce:
    def maxArea(self, height: List[int]) -> int:
        """
        Brute force - check all pairs - O(n^2).
        """
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)

        return max_area
