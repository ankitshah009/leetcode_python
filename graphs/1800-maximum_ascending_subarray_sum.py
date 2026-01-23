#1800. Maximum Ascending Subarray Sum
#Easy
#
#Given an array of positive integers nums, return the maximum possible sum of
#an ascending subarray in nums.
#
#A subarray is defined as a contiguous sequence of numbers in an array.
#
#A subarray [nums_l, nums_l+1, ..., nums_r-1, nums_r] is ascending if for all i
#where l <= i < r, nums_i < nums_i+1. Note that a subarray of size one is
#ascending.
#
#Example 1:
#Input: nums = [10,20,30,5,10,50]
#Output: 65
#
#Example 2:
#Input: nums = [10,20,30,40,50]
#Output: 150
#
#Example 3:
#Input: nums = [12,17,15,13,10,11,12]
#Output: 33
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 100

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Track current ascending sum and max.
        """
        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)

        return max_sum


class SolutionOnePass:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        Single pass with running sum reset.
        """
        result = 0
        i = 0

        while i < len(nums):
            current = nums[i]
            while i + 1 < len(nums) and nums[i + 1] > nums[i]:
                i += 1
                current += nums[i]
            result = max(result, current)
            i += 1

        return result
