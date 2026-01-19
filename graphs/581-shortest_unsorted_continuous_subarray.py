#581. Shortest Unsorted Continuous Subarray
#Medium
#
#Given an integer array nums, you need to find one continuous subarray such that
#if you only sort this subarray in non-decreasing order, then the whole array
#will be sorted in non-decreasing order.
#
#Return the shortest such subarray and output its length.
#
#Example 1:
#Input: nums = [2,6,4,8,10,9,15]
#Output: 5
#Explanation: You need to sort [6, 4, 8, 10, 9] to make the whole array sorted.
#
#Example 2:
#Input: nums = [1,2,3,4]
#Output: 0
#
#Example 3:
#Input: nums = [1]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^5 <= nums[i] <= 10^5

from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """O(n) time, O(1) space using two passes"""
        n = len(nums)

        # Find right boundary - rightmost element smaller than max seen so far
        max_seen = float('-inf')
        right = -1
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            max_seen = max(max_seen, nums[i])

        # Find left boundary - leftmost element larger than min seen from right
        min_seen = float('inf')
        left = 0
        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            min_seen = min(min_seen, nums[i])

        return right - left + 1 if right > left else 0


class SolutionSort:
    """Using sorting - O(n log n) time, O(n) space"""

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        left = 0
        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1

        if left == len(nums):
            return 0

        right = len(nums) - 1
        while nums[right] == sorted_nums[right]:
            right -= 1

        return right - left + 1


class SolutionStack:
    """Using monotonic stack"""

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, 0
        stack = []

        # Find left boundary
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []

        # Find right boundary
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)

        return right - left + 1 if right > left else 0
