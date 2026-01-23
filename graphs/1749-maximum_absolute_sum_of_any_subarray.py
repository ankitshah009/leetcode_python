#1749. Maximum Absolute Sum of Any Subarray
#Medium
#
#You are given an integer array nums. The absolute sum of a subarray
#[numsl, numsl+1, ..., numsr-1, numsr] is |numsl + numsl+1 + ... + numsr-1 + numsr|.
#
#Return the maximum absolute sum of any (possibly empty) subarray of nums.
#
#Note that |x| is defined as:
#- x if x >= 0.
#- -x if x < 0.
#
#Example 1:
#Input: nums = [1,-3,2,3,-4]
#Output: 5
#
#Example 2:
#Input: nums = [2,-5,1,-4,3,-2]
#Output: 8
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Track max and min prefix sums.
        Max absolute sum = max prefix sum - min prefix sum.
        """
        max_prefix = 0
        min_prefix = 0
        current = 0

        for num in nums:
            current += num
            max_prefix = max(max_prefix, current)
            min_prefix = min(min_prefix, current)

        return max_prefix - min_prefix


class SolutionKadane:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Kadane for max and min subarray sum.
        """
        max_sum = max_ending = 0
        min_sum = min_ending = 0

        for num in nums:
            max_ending = max(num, max_ending + num)
            max_sum = max(max_sum, max_ending)

            min_ending = min(num, min_ending + num)
            min_sum = min(min_sum, min_ending)

        return max(max_sum, -min_sum)


class SolutionCombined:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Combined Kadane variation.
        """
        max_end = min_end = 0
        max_so_far = min_so_far = 0

        for num in nums:
            max_end = max(0, max_end + num)
            min_end = min(0, min_end + num)
            max_so_far = max(max_so_far, max_end)
            min_so_far = min(min_so_far, min_end)

        return max(max_so_far, -min_so_far)
