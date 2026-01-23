#1959. Minimum Total Space Wasted With K Resizing Operations
#Medium
#
#You are currently designing a dynamic array. You are given a 0-indexed integer
#array nums, where nums[i] is the number of elements that will be in the array
#at time i. In addition, you are given an integer k, the maximum number of times
#you can resize the array (to any size).
#
#The size of the array at any time must be at least nums[i] (no fewer elements
#than required at time i). The wasted space is the total number of positions
#that are not used at all times in the array. The wasted space at time i is
#size - nums[i], and the total wasted space is the sum of wasted space over all
#times.
#
#Return the minimum total wasted space possible after k resizing operations.
#
#Example 1:
#Input: nums = [10,20], k = 0
#Output: 10
#Explanation: We can use size 20 for the entire time.
#Wasted space = 20 - 10 + 20 - 20 = 10.
#
#Example 2:
#Input: nums = [10,20,30], k = 1
#Output: 10
#
#Example 3:
#Input: nums = [10,20,15,30,20], k = 2
#Output: 15
#
#Constraints:
#    1 <= nums.length <= 200
#    1 <= nums[i] <= 10^6
#    0 <= k <= nums.length - 1

from typing import List
from functools import lru_cache

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        DP with precomputed waste for segments.
        """
        n = len(nums)

        # Precompute waste for segment [i, j]
        # Waste = max(segment) * length - sum(segment)
        waste = [[0] * n for _ in range(n)]

        for i in range(n):
            max_val = 0
            total = 0
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                total += nums[j]
                waste[i][j] = max_val * (j - i + 1) - total

        @lru_cache(maxsize=None)
        def dp(idx: int, resizes: int) -> int:
            if idx == n:
                return 0

            if resizes < 0:
                return float('inf')

            min_waste = float('inf')

            # Try each possible end position for current segment
            for end in range(idx, n):
                min_waste = min(min_waste,
                              waste[idx][end] + dp(end + 1, resizes - 1))

            return min_waste

        return dp(0, k)


class SolutionIterative:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        Iterative DP approach.
        """
        n = len(nums)

        # Precompute waste
        waste = [[0] * n for _ in range(n)]
        for i in range(n):
            max_val = total = 0
            for j in range(i, n):
                max_val = max(max_val, nums[j])
                total += nums[j]
                waste[i][j] = max_val * (j - i + 1) - total

        # dp[i][j] = min waste for first i elements with j resizes
        INF = float('inf')
        dp = [[INF] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(min(i, k + 1) + 1):
                for prev in range(i):
                    if j > 0 or prev == 0:
                        prev_resizes = j - 1 if prev > 0 else 0
                        dp[i][j] = min(dp[i][j],
                                      dp[prev][prev_resizes] + waste[prev][i - 1])

        return min(dp[n])
