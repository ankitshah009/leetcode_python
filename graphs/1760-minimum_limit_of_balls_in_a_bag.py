#1760. Minimum Limit of Balls in a Bag
#Medium
#
#You are given an integer array nums where the ith bag contains nums[i] balls.
#You are also given an integer maxOperations.
#
#You can perform the following operation at most maxOperations times:
#- Take any bag of balls and divide it into two new bags with a positive number
#  of balls.
#
#Your penalty is the maximum number of balls in a bag. You want to minimize your
#penalty after the operations.
#
#Return the minimum possible penalty after performing the operations.
#
#Example 1:
#Input: nums = [9], maxOperations = 2
#Output: 3
#
#Example 2:
#Input: nums = [2,4,8,2], maxOperations = 4
#Output: 2
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= maxOperations, nums[i] <= 10^9

from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        Binary search on answer.
        For penalty p, count operations needed: ceil(n/p) - 1 for each bag of n balls.
        """
        def operations_needed(penalty: int) -> int:
            """Count total operations to make all bags <= penalty."""
            return sum((n - 1) // penalty for n in nums)

        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            if operations_needed(mid) <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left


class SolutionDetailed:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        Same approach with detailed explanation.
        """
        def can_achieve(max_balls: int) -> bool:
            """Check if we can make all bags have at most max_balls."""
            ops = 0
            for n in nums:
                # To split n balls into bags of at most max_balls:
                # We need ceil(n / max_balls) bags
                # This requires ceil(n / max_balls) - 1 operations
                # = (n - 1) // max_balls
                ops += (n - 1) // max_balls
                if ops > maxOperations:
                    return False
            return True

        lo, hi = 1, max(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if can_achieve(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


class SolutionMath:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        Mathematical formulation.
        """
        import math

        def min_ops(penalty):
            return sum(math.ceil(x / penalty) - 1 for x in nums)

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2
            if min_ops(mid) <= maxOperations:
                right = mid
            else:
                left = mid + 1

        return left
