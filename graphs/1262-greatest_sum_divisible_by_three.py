#1262. Greatest Sum Divisible by Three
#Medium
#
#Given an integer array nums, return the maximum possible sum of elements of
#the array such that it is divisible by three.
#
#Example 1:
#Input: nums = [3,6,5,1,8]
#Output: 18
#Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
#
#Example 2:
#Input: nums = [4]
#Output: 0
#Explanation: Since 4 is not divisible by 3, do not pick any number.
#
#Example 3:
#Input: nums = [1,2,3,4,4]
#Output: 12
#Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
#
#Constraints:
#    1 <= nums.length <= 4 * 10^4
#    1 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        DP: Track maximum sum for each remainder (0, 1, 2).
        """
        # dp[r] = max sum with remainder r
        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            temp = dp.copy()
            for r in range(3):
                new_r = (r + num) % 3
                temp[new_r] = max(temp[new_r], dp[r] + num)
            dp = temp

        return dp[0]


class SolutionGreedy:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Greedy approach:
        Take all numbers, then remove smallest to fix remainder.
        """
        total = sum(nums)
        remainder = total % 3

        if remainder == 0:
            return total

        # Group numbers by their remainder
        mod1 = sorted([x for x in nums if x % 3 == 1])
        mod2 = sorted([x for x in nums if x % 3 == 2])

        result = 0

        if remainder == 1:
            # Remove one number with mod 1, or two numbers with mod 2
            options = []
            if mod1:
                options.append(total - mod1[0])
            if len(mod2) >= 2:
                options.append(total - mod2[0] - mod2[1])
            result = max(options) if options else 0

        else:  # remainder == 2
            # Remove one number with mod 2, or two numbers with mod 1
            options = []
            if mod2:
                options.append(total - mod2[0])
            if len(mod1) >= 2:
                options.append(total - mod1[0] - mod1[1])
            result = max(options) if options else 0

        return result
