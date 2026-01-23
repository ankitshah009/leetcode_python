#1848. Minimum Distance to the Target Element
#Easy
#
#Given an integer array nums (0-indexed) and two integers target and start,
#find an index i such that nums[i] == target and abs(i - start) is minimized.
#Note that abs(x) is the absolute value of x.
#
#Return abs(i - start).
#
#It is guaranteed that target exists in nums.
#
#Example 1:
#Input: nums = [1,2,3,4,5], target = 5, start = 3
#Output: 1
#
#Example 2:
#Input: nums = [1], target = 1, start = 0
#Output: 0
#
#Example 3:
#Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i] <= 10^4
#    0 <= start < nums.length
#    target is in nums.

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Find minimum distance to any occurrence of target.
        """
        return min(abs(i - start) for i, num in enumerate(nums) if num == target)


class SolutionExpand:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Expand from start in both directions.
        """
        n = len(nums)

        for dist in range(n):
            left = start - dist
            right = start + dist

            if (0 <= left and nums[left] == target) or \
               (right < n and nums[right] == target):
                return dist

        return -1  # Should never reach here


class SolutionLoop:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        """
        Explicit loop finding minimum.
        """
        min_dist = float('inf')

        for i, num in enumerate(nums):
            if num == target:
                min_dist = min(min_dist, abs(i - start))

        return min_dist
