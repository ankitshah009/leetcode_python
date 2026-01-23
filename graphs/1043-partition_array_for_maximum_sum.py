#1043. Partition Array for Maximum Sum
#Medium
#
#Given an integer array arr, partition the array into (contiguous) subarrays
#of length at most k. After partitioning, each subarray has their values
#changed to become the maximum value of that subarray.
#
#Return the largest sum of the given array after partitioning.
#
#Example 1:
#Input: arr = [1,15,7,9,2,5,10], k = 3
#Output: 84
#Explanation: arr becomes [15,15,15,9,10,10,10]
#
#Example 2:
#Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
#Output: 83
#
#Example 3:
#Input: arr = [1], k = 1
#Output: 1
#
#Constraints:
#    1 <= arr.length <= 500
#    0 <= arr[i] <= 10^9
#    1 <= k <= arr.length

from typing import List
from functools import lru_cache

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        DP: dp[i] = max sum for arr[0:i]
        For each position i, try all partition lengths 1 to k ending at i.
        """
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        return dp[n]


class SolutionMemo:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """Memoized recursion"""
        n = len(arr)

        @lru_cache(maxsize=None)
        def dp(start):
            if start >= n:
                return 0

            max_val = 0
            result = 0

            for length in range(1, min(k, n - start) + 1):
                max_val = max(max_val, arr[start + length - 1])
                result = max(result, max_val * length + dp(start + length))

            return result

        return dp(0)


class SolutionReverse:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """DP from right to left"""
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            max_val = 0
            for j in range(1, min(k, n - i) + 1):
                max_val = max(max_val, arr[i + j - 1])
                dp[i] = max(dp[i], max_val * j + dp[i + j])

        return dp[0]
