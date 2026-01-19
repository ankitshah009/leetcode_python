#213. House Robber II
#Medium
#
#You are a professional robber planning to rob houses along a street. Each house
#has a certain amount of money stashed. All houses at this place are arranged
#in a circle. That means the first house is the neighbor of the last one.
#Meanwhile, adjacent houses have a security system connected, and it will
#automatically contact the police if two adjacent houses were broken into on
#the same night.
#
#Given an integer array nums representing the amount of money of each house,
#return the maximum amount of money you can rob tonight without alerting the police.
#
#Example 1:
#Input: nums = [2,3,2]
#Output: 3
#Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#because they are adjacent houses.
#
#Example 2:
#Input: nums = [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount = 1 + 3 = 4.
#
#Example 3:
#Input: nums = [1,2,3]
#Output: 3
#
#Constraints:
#    1 <= nums.length <= 100
#    0 <= nums[i] <= 1000

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Since houses are in a circle, we can't rob both first and last.
        So we solve two subproblems:
        1. Rob houses 0 to n-2 (exclude last)
        2. Rob houses 1 to n-1 (exclude first)
        Take the maximum.
        """
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            if not houses:
                return 0

            prev2 = 0  # rob[i-2]
            prev1 = 0  # rob[i-1]

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Exclude last house
        # Case 2: Exclude first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


class SolutionDP:
    """Explicit DP array approach"""

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def rob_range(start, end):
            dp = [0] * n
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])

            for i in range(start + 2, end + 1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

            return dp[end]

        return max(rob_range(0, n - 2), rob_range(1, n - 1))


class SolutionMemo:
    """Memoization approach"""

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_range(start, end, memo):
            if start > end:
                return 0
            if start in memo:
                return memo[start]

            memo[start] = max(
                nums[start] + rob_range(start + 2, end, memo),
                rob_range(start + 1, end, memo)
            )
            return memo[start]

        return max(
            rob_range(0, n - 2, {}),
            rob_range(1, n - 1, {})
        )
