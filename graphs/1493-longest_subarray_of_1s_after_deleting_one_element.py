#1493. Longest Subarray of 1's After Deleting One Element
#Medium
#
#Given a binary array nums, you should delete one element from it.
#
#Return the size of the longest non-empty subarray containing only 1's in the
#resulting array. Return 0 if there is no such subarray.
#
#Example 1:
#Input: nums = [1,1,0,1]
#Output: 3
#Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers
#with value of 1's.
#
#Example 2:
#Input: nums = [0,1,1,1,0,1,1,0,1]
#Output: 5
#Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest
#subarray with value of 1's is [1,1,1,1,1].
#
#Example 3:
#Input: nums = [1,1,1]
#Output: 2
#Explanation: You must delete one element.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    nums[i] is either 0 or 1.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """Sliding window with at most one 0"""
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Length is right - left (not +1 because we must delete one element)
            max_len = max(max_len, right - left)

        return max_len


class SolutionNoShrink:
    """Window never shrinks"""

    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            if zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

        # Must delete one element, so length is n - left - 1
        return len(nums) - left - 1


class SolutionTwoArrays:
    """Track consecutive 1s before and after each position"""

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # left[i] = number of consecutive 1s ending at i-1
        left = [0] * n
        for i in range(1, n):
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1

        # right[i] = number of consecutive 1s starting at i+1
        right = [0] * n
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1

        # Delete element at i and combine left and right
        max_len = 0
        for i in range(n):
            max_len = max(max_len, left[i] + right[i])

        return max_len
