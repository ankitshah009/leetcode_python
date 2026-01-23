#1785. Minimum Elements to Add to Form a Given Sum
#Medium
#
#You are given an integer array nums and two integers limit and goal. The array
#nums has an interesting property that abs(nums[i]) <= limit.
#
#Return the minimum number of elements you need to add to make the sum of the
#array equal to goal. The added elements must satisfy abs(x) <= limit.
#
#Example 1:
#Input: nums = [1,-1,1], limit = 3, goal = -4
#Output: 2
#
#Example 2:
#Input: nums = [1,-10,9,1], limit = 100, goal = 0
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 10^5
#    1 <= limit <= 10^6
#    -limit <= nums[i] <= limit
#    -10^9 <= goal <= 10^9

from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        """
        Find difference and divide by limit (ceiling).
        """
        current_sum = sum(nums)
        diff = abs(goal - current_sum)

        # Each element can contribute at most 'limit' towards the goal
        # Need ceil(diff / limit) elements
        return (diff + limit - 1) // limit


class SolutionMath:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        """
        Using math.ceil.
        """
        import math

        diff = abs(goal - sum(nums))
        return math.ceil(diff / limit)


class SolutionDivMod:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        """
        Using divmod.
        """
        diff = abs(goal - sum(nums))
        q, r = divmod(diff, limit)
        return q + (1 if r > 0 else 0)
