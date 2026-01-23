#1413. Minimum Value to Get Positive Step by Step Sum
#Easy
#
#Given an array of integers nums, you start with an initial positive value
#startValue.
#
#In each iteration, you calculate the step by step sum of startValue plus
#elements in nums (from left to right).
#
#Return the minimum positive value of startValue such that the step by step sum
#is never less than 1.
#
#Example 1:
#Input: nums = [-3,2,-3,4,2]
#Output: 5
#Explanation: If you choose startValue = 4, in the third iteration your step by
#step sum is less than 1.
#step by step sum:
#startValue = 4 | startValue = 5
#  (4 -3 ) = 1  | (5 -3 ) = 2
#  (1 +2 ) = 3  | (2 +2 ) = 4
#  (3 -3 ) = 0  | (4 -3 ) = 1
#  (0 +4 ) = 4  | (1 +4 ) = 5
#  (4 +2 ) = 6  | (5 +2 ) = 7
#
#Example 2:
#Input: nums = [1,2]
#Output: 1
#Explanation: Minimum start value should be positive.
#
#Example 3:
#Input: nums = [1,-2,-3]
#Output: 5
#
#Constraints:
#    1 <= nums.length <= 100
#    -100 <= nums[i] <= 100

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Find minimum prefix sum. StartValue must offset the minimum prefix sum
        to keep running total >= 1.

        If min_prefix_sum = m, then startValue + m >= 1, so startValue >= 1 - m.
        Return max(1, 1 - min_prefix_sum).
        """
        prefix_sum = 0
        min_prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max(1, 1 - min_prefix_sum)


class SolutionExplicit:
    def minStartValue(self, nums: List[int]) -> int:
        """More explicit version"""
        # Calculate all prefix sums
        prefix_sums = []
        total = 0
        for num in nums:
            total += num
            prefix_sums.append(total)

        # Find minimum prefix sum
        min_prefix = min(prefix_sums)

        # startValue + min_prefix >= 1
        # startValue >= 1 - min_prefix
        return max(1, 1 - min_prefix)


class SolutionBinarySearch:
    def minStartValue(self, nums: List[int]) -> int:
        """Binary search approach (overkill but demonstrates concept)"""
        def is_valid(start_value: int) -> bool:
            total = start_value
            for num in nums:
                total += num
                if total < 1:
                    return False
            return True

        left, right = 1, 1 + sum(abs(x) for x in nums)

        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1

        return left
