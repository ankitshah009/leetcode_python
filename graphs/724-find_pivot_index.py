#724. Find Pivot Index
#Easy
#
#Given an array of integers nums, calculate the pivot index of this array.
#
#The pivot index is the index where the sum of all the numbers strictly to the
#left of the index is equal to the sum of all the numbers strictly to the index's
#right.
#
#If the index is on the left edge of the array, then the left sum is 0 because
#there are no elements to the left. This also applies to the right edge of the array.
#
#Return the leftmost pivot index. If no such index exists, return -1.
#
#Example 1:
#Input: nums = [1,7,3,6,5,6]
#Output: 3
#Explanation: The pivot index is 3.
#Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
#Right sum = nums[4] + nums[5] = 5 + 6 = 11
#
#Example 2:
#Input: nums = [1,2,3]
#Output: -1
#
#Example 3:
#Input: nums = [2,1,-1]
#Output: 0
#Explanation: The pivot index is 0.
#Left sum = 0 (no elements)
#Right sum = nums[1] + nums[2] = 1 + -1 = 0
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -1000 <= nums[i] <= 1000

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """Single pass with running sums"""
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Right sum = total - left_sum - nums[i]
            if left_sum == total - left_sum - num:
                return i
            left_sum += num

        return -1


class SolutionPrefixSum:
    """Using prefix sum array"""

    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        total = prefix[n]

        for i in range(n):
            left_sum = prefix[i]
            right_sum = total - prefix[i + 1]
            if left_sum == right_sum:
                return i

        return -1


class SolutionTwoArrays:
    """Track left and right sums separately"""

    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        right_sum = [0] * n
        right_sum[-1] = 0
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        left_sum = 0
        for i in range(n):
            if left_sum == right_sum[i]:
                return i
            left_sum += nums[i]

        return -1
