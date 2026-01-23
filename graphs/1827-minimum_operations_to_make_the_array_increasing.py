#1827. Minimum Operations to Make the Array Increasing
#Easy
#
#You are given an integer array nums (0-indexed). In one operation, you can
#choose an element of the array and increment it by 1.
#
#For example, if nums = [1,2,3], you can choose to increment nums[1] to make
#nums = [1,3,3].
#
#Return the minimum number of operations needed to make nums strictly
#increasing.
#
#An array nums is strictly increasing if nums[i] < nums[i+1] for all
#0 <= i < nums.length - 1.
#
#Example 1:
#Input: nums = [1,1,1]
#Output: 3
#
#Example 2:
#Input: nums = [1,5,2,4,1]
#Output: 14
#
#Example 3:
#Input: nums = [8]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 5000
#    1 <= nums[i] <= 10^4

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Each element must be > previous.
        Track minimum required value.
        """
        ops = 0
        prev = 0

        for num in nums:
            if num <= prev:
                # Need to increase to prev + 1
                ops += prev + 1 - num
                prev = prev + 1
            else:
                prev = num

        return ops


class SolutionExplicit:
    def minOperations(self, nums: List[int]) -> int:
        """
        Same approach with explicit variable names.
        """
        total_operations = 0
        min_required = nums[0]

        for i in range(1, len(nums)):
            min_required += 1  # Must be strictly greater

            if nums[i] < min_required:
                total_operations += min_required - nums[i]
            else:
                min_required = nums[i]

        return total_operations


class SolutionOneLiner:
    def minOperations(self, nums: List[int]) -> int:
        """
        Functional approach.
        """
        from functools import reduce

        def step(acc, num):
            ops, prev = acc
            if num <= prev:
                return (ops + prev + 1 - num, prev + 1)
            return (ops, num)

        result, _ = reduce(step, nums, (0, 0))
        return result
