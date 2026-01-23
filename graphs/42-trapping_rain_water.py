#42. Trapping Rain Water
#Hard
#
#Given n non-negative integers representing an elevation map where the width of
#each bar is 1, compute how much water it can trap after raining.
#
#Example 1:
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
#In this case, 6 units of rain water are being trapped.
#
#Example 2:
#Input: height = [4,2,0,3,2,5]
#Output: 9
#
#Constraints:
#    n == height.length
#    1 <= n <= 2 * 10^4
#    0 <= height[i] <= 10^5

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two pointers approach - O(n) time, O(1) space.
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


class SolutionDP:
    def trap(self, height: List[int]) -> int:
        """
        Dynamic Programming - precompute left and right max.
        O(n) time, O(n) space.
        """
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        # Fill left_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Fill right_max
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water


class SolutionStack:
    def trap(self, height: List[int]) -> int:
        """
        Monotonic stack approach - O(n) time, O(n) space.
        """
        stack = []
        water = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()
                if not stack:
                    break

                width = i - stack[-1] - 1
                bounded_height = min(h, height[stack[-1]]) - height[bottom]
                water += width * bounded_height

            stack.append(i)

        return water


class SolutionBruteForce:
    def trap(self, height: List[int]) -> int:
        """
        Brute force - for each position, find max on left and right.
        O(n^2) time, O(1) space.
        """
        n = len(height)
        water = 0

        for i in range(n):
            left_max = max(height[:i + 1]) if i >= 0 else 0
            right_max = max(height[i:]) if i < n else 0

            water += min(left_max, right_max) - height[i]

        return water
