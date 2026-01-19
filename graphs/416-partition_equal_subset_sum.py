#416. Partition Equal Subset Sum
#Medium
#
#Given an integer array nums, return true if you can partition the array into
#two subsets such that the sum of the elements in both subsets is equal or
#false otherwise.
#
#Example 1:
#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#Example 2:
#Input: nums = [1,2,3,5]
#Output: false
#Explanation: The array cannot be partitioned into equal sum subsets.
#
#Constraints:
#    1 <= nums.length <= 200
#    1 <= nums[i] <= 100

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        0/1 Knapsack: Can we select items summing to total/2?
        """
        total = sum(nums)

        # If odd, can't split equally
        if total % 2 == 1:
            return False

        target = total // 2

        # dp[i] = True if sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Iterate backwards to avoid using same number twice
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


class SolutionSet:
    """Using set to track achievable sums"""

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        achievable = {0}

        for num in nums:
            achievable = achievable | {s + num for s in achievable if s + num <= target}
            if target in achievable:
                return True

        return target in achievable


class SolutionMemo:
    """Top-down memoization"""

    def canPartition(self, nums: List[int]) -> bool:
        from functools import lru_cache

        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        @lru_cache(maxsize=None)
        def dp(index, remaining):
            if remaining == 0:
                return True
            if index >= len(nums) or remaining < 0:
                return False

            # Include or exclude current number
            return dp(index + 1, remaining - nums[index]) or dp(index + 1, remaining)

        return dp(0, target)


class SolutionBitset:
    """Bitset approach using integer"""

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        # Use integer as bitset
        # bit i is set if sum i is achievable
        bits = 1  # Initially only sum 0 is achievable

        for num in nums:
            bits |= bits << num

        return (bits >> target) & 1 == 1
