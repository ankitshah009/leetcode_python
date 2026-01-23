#1955. Count Number of Special Subsequences
#Hard
#
#A sequence is special if it consists of a positive number of 0s, followed by a
#positive number of 1s, then a positive number of 2s.
#
#For example, [0,1,2] and [0,0,1,1,1,2] are special.
#In contrast, [2,1,0], [1], and [0,1,2,0] are not special.
#
#Given an array nums (consisting of only integers 0, 1, and 2), return the
#number of different subsequences that are special. Since the answer may be
#very large, return it modulo 10^9 + 7.
#
#A subsequence of an array is a sequence that can be derived from the array by
#deleting some or no elements without changing the order of the remaining
#elements. Two subsequences are different if the set of indices chosen are
#different.
#
#Example 1:
#Input: nums = [0,1,2,2]
#Output: 3
#Explanation: Special subsequences are [0,1,2,2], [0,1,2,2], and [0,1,2,2].
#
#Example 2:
#Input: nums = [2,2,0,0]
#Output: 0
#
#Example 3:
#Input: nums = [0,1,2,0,1,2]
#Output: 7
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 2

from typing import List

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        """
        DP tracking count of subsequences ending at each stage.
        dp[0] = subsequences of 0s only
        dp[1] = subsequences of 0s followed by 1s
        dp[2] = complete special subsequences (0s, 1s, 2s)
        """
        MOD = 10**9 + 7

        dp = [0, 0, 0]

        for num in nums:
            if num == 0:
                # New 0 can start new or extend existing 0-subsequences
                dp[0] = (2 * dp[0] + 1) % MOD
            elif num == 1:
                # New 1 can extend 0-subsequences or existing 01-subsequences
                dp[1] = (2 * dp[1] + dp[0]) % MOD
            else:  # num == 2
                # New 2 can extend 01-subsequences or existing 012-subsequences
                dp[2] = (2 * dp[2] + dp[1]) % MOD

        return dp[2]


class SolutionExplained:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        """
        Detailed explanation:

        For each number, we either include it or not:
        - If num=0: dp[0] = dp[0] (not include) + dp[0] (extend) + 1 (start new)
                  = 2 * dp[0] + 1
        - If num=1: dp[1] = dp[1] (not include) + dp[1] (extend) + dp[0] (transition)
                  = 2 * dp[1] + dp[0]
        - If num=2: dp[2] = dp[2] (not include) + dp[2] (extend) + dp[1] (transition)
                  = 2 * dp[2] + dp[1]
        """
        MOD = 10**9 + 7

        zeros = 0   # Subsequences of just 0s
        ones = 0    # Subsequences of 0s then 1s
        twos = 0    # Complete special subsequences

        for num in nums:
            if num == 0:
                zeros = (2 * zeros + 1) % MOD
            elif num == 1:
                ones = (2 * ones + zeros) % MOD
            else:
                twos = (2 * twos + ones) % MOD

        return twos
