#377. Combination Sum IV
#Medium
#
#Given an array of distinct integers nums and a target integer target, return
#the number of possible combinations that add up to target.
#
#The test cases are generated so that the answer can fit in a 32-bit integer.
#
#Example 1:
#Input: nums = [1,2,3], target = 4
#Output: 7
#Explanation:
#The possible combination ways are:
#(1, 1, 1, 1)
#(1, 1, 2)
#(1, 2, 1)
#(1, 3)
#(2, 1, 1)
#(2, 2)
#(3, 1)
#Note that different sequences are counted as different combinations.
#
#Example 2:
#Input: nums = [9], target = 3
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 200
#    1 <= nums[i] <= 1000
#    All the elements of nums are unique.
#    1 <= target <= 1000

from typing import List
from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        DP approach - similar to coin change but counting permutations.
        dp[i] = number of ways to reach sum i
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]


class SolutionMemo:
    """Top-down memoization"""

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            count = 0
            for num in nums:
                count += dp(remaining - num)
            return count

        return dp(target)


class SolutionDict:
    """Using dictionary for memoization"""

    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0: 1}

        def dp(remaining):
            if remaining in memo:
                return memo[remaining]

            count = 0
            for num in nums:
                if remaining >= num:
                    count += dp(remaining - num)

            memo[remaining] = count
            return count

        return dp(target)


class SolutionWithNegatives:
    """
    Follow-up: What if negative numbers are allowed in the given array?

    With negative numbers, there could be infinite combinations if we can
    form 0 using a subset (e.g., [1, -1]).

    Solution: Limit the length of combinations or specify that each number
    can only be used a limited number of times.
    """

    def combinationSum4WithLimit(self, nums: List[int], target: int, max_length: int) -> int:
        @lru_cache(maxsize=None)
        def dp(remaining, length):
            if remaining == 0:
                return 1
            if length >= max_length:
                return 0

            count = 0
            for num in nums:
                count += dp(remaining - num, length + 1)
            return count

        return dp(target, 0)
