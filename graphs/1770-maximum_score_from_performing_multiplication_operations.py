#1770. Maximum Score from Performing Multiplication Operations
#Hard
#
#You are given two 0-indexed integer arrays nums and multipliers of size n and m
#respectively, where n >= m.
#
#You begin with a score of 0. You want to perform exactly m operations. On the
#ith operation (0-indexed) you will:
#
#- Choose one integer x from either the start or the end of the array nums.
#- Add multipliers[i] * x to your score.
#- Remove x from the array nums.
#
#Return the maximum score after performing m operations.
#
#Example 1:
#Input: nums = [1,2,3], multipliers = [3,2,1]
#Output: 14
#
#Example 2:
#Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
#Output: 102
#
#Constraints:
#    n == nums.length
#    m == multipliers.length
#    1 <= m <= 300
#    m <= n <= 10^5
#    -1000 <= nums[i], multipliers[i] <= 1000

from typing import List
from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        DP with memoization.
        State: (operation_index, left_count) -> right_count is derived
        """
        n, m = len(nums), len(multipliers)

        @lru_cache(maxsize=None)
        def dp(op: int, left: int) -> int:
            if op == m:
                return 0

            right = n - 1 - (op - left)

            # Take from left
            take_left = multipliers[op] * nums[left] + dp(op + 1, left + 1)

            # Take from right
            take_right = multipliers[op] * nums[right] + dp(op + 1, left)

            return max(take_left, take_right)

        return dp(0, 0)


class SolutionDP:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        Bottom-up DP.
        """
        n, m = len(nums), len(multipliers)

        # dp[i][left] = max score using operations i..m-1, with left elements taken from left
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                right = n - 1 - (op - left)

                take_left = multipliers[op] * nums[left] + dp[op + 1][left + 1]
                take_right = multipliers[op] * nums[right] + dp[op + 1][left]

                dp[op][left] = max(take_left, take_right)

        return dp[0][0]


class SolutionSpaceOptimized:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """
        Space-optimized DP.
        """
        n, m = len(nums), len(multipliers)

        # Only need current and next row
        dp = [0] * (m + 1)

        for op in range(m - 1, -1, -1):
            new_dp = [0] * (m + 1)
            for left in range(op + 1):
                right = n - 1 - (op - left)
                take_left = multipliers[op] * nums[left] + dp[left + 1]
                take_right = multipliers[op] * nums[right] + dp[left]
                new_dp[left] = max(take_left, take_right)
            dp = new_dp

        return dp[0]
