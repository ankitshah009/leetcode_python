#1027. Longest Arithmetic Subsequence
#Medium
#
#Given an array nums of integers, return the length of the longest
#arithmetic subsequence in nums.
#
#A subsequence of an array is a sequence that can be derived from the
#array by deleting some or no elements without changing the order of the
#remaining elements.
#
#A sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value
#(for 0 <= i < seq.length - 1).
#
#Example 1:
#Input: nums = [3,6,9,12]
#Output: 4
#Explanation: The whole array is an arithmetic sequence with steps of 3.
#
#Example 2:
#Input: nums = [9,4,7,2,10]
#Output: 3
#Explanation: The longest arithmetic subsequence is [4,7,10].
#
#Example 3:
#Input: nums = [20,1,15,3,10,5,8]
#Output: 4
#Explanation: The longest arithmetic subsequence is [20,15,10,5].
#
#Constraints:
#    2 <= nums.length <= 1000
#    0 <= nums[i] <= 500

from typing import List
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        DP with dictionary: dp[i][diff] = length of arithmetic
        subsequence ending at i with common difference diff.
        """
        n = len(nums)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        result = 2

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j][diff] + 1
                result = max(result, dp[i][diff])

        return result


class SolutionOptimized:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        Single dictionary mapping (index, diff) -> length
        """
        dp = {}
        result = 2

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
                result = max(result, dp[(i, diff)])

        return result


class SolutionArray:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
        Use array instead of dict (faster for small value ranges).
        Since nums[i] <= 500, diff ranges from -500 to 500.
        """
        n = len(nums)
        # Offset diff by 500 to handle negative
        dp = [[1] * 1001 for _ in range(n)]
        result = 2

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j] + 500
                dp[i][diff] = dp[j][diff] + 1
                result = max(result, dp[i][diff])

        return result
