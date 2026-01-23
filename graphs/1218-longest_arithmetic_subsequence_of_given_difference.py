#1218. Longest Arithmetic Subsequence of Given Difference
#Medium
#
#Given an integer array arr and an integer difference, return the length of
#the longest subsequence in arr which is an arithmetic sequence such that the
#difference between adjacent elements in the subsequence equals difference.
#
#A subsequence is a sequence that can be derived from arr by deleting some or
#no elements without changing the order of the remaining elements.
#
#Example 1:
#Input: arr = [1,2,3,4], difference = 1
#Output: 4
#Explanation: The longest arithmetic subsequence is [1,2,3,4].
#
#Example 2:
#Input: arr = [1,3,5,7], difference = 1
#Output: 1
#Explanation: The longest arithmetic subsequence is any single element.
#
#Example 3:
#Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
#Output: 4
#Explanation: The longest arithmetic subsequence is [7,5,3,1].
#
#Constraints:
#    1 <= arr.length <= 10^5
#    -10^4 <= arr[i], difference <= 10^4

from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        DP: dp[x] = length of longest arithmetic subsequence ending with value x.

        For each number, the previous number in sequence would be (num - difference).
        """
        dp = {}  # value -> longest subsequence length ending with this value
        max_length = 0

        for num in arr:
            prev = num - difference
            dp[num] = dp.get(prev, 0) + 1
            max_length = max(max_length, dp[num])

        return max_length


class SolutionDefaultDict:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """Using defaultdict"""
        from collections import defaultdict

        dp = defaultdict(int)

        for num in arr:
            dp[num] = dp[num - difference] + 1

        return max(dp.values())
