#1879. Minimum XOR Sum of Two Arrays
#Hard
#
#You are given two integer arrays nums1 and nums2 of length n.
#
#The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1]
#XOR nums2[1]) + ... + (nums1[n-1] XOR nums2[n-1]) (0-indexed).
#
#Rearrange the elements of nums2 such that the resulting XOR sum is minimized.
#
#Return the XOR sum after the rearrangement.
#
#Example 1:
#Input: nums1 = [1,2], nums2 = [2,3]
#Output: 2
#
#Example 2:
#Input: nums1 = [1,0,3], nums2 = [5,3,4]
#Output: 8
#
#Constraints:
#    n == nums1.length
#    n == nums2.length
#    1 <= n <= 14
#    0 <= nums1[i], nums2[i] <= 10^7

from typing import List
from functools import lru_cache

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Bitmask DP - assignment problem.
        dp[mask] = min XOR sum using elements of nums2 indicated by mask.
        """
        n = len(nums1)

        @lru_cache(maxsize=None)
        def dp(i: int, mask: int) -> int:
            if i == n:
                return 0

            min_sum = float('inf')

            for j in range(n):
                if not (mask & (1 << j)):  # j not used yet
                    cost = nums1[i] ^ nums2[j]
                    min_sum = min(min_sum, cost + dp(i + 1, mask | (1 << j)))

            return min_sum

        return dp(0, 0)


class SolutionIterative:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Bottom-up bitmask DP.
        """
        n = len(nums1)
        INF = float('inf')

        # dp[mask] = min XOR sum to match first popcount(mask) elements of nums1
        dp = [INF] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == INF:
                continue

            i = bin(mask).count('1')  # Number of elements matched
            if i >= n:
                continue

            for j in range(n):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    cost = nums1[i] ^ nums2[j]
                    dp[new_mask] = min(dp[new_mask], dp[mask] + cost)

        return dp[(1 << n) - 1]


class SolutionHungarian:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        """
        This is the assignment problem - could use Hungarian algorithm
        for larger n, but bitmask DP is simpler for n <= 14.
        """
        n = len(nums1)

        # Build cost matrix
        cost = [[nums1[i] ^ nums2[j] for j in range(n)] for i in range(n)]

        # Bitmask DP
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            i = bin(mask).count('1')
            if i >= n:
                continue

            for j in range(n):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = min(dp[new_mask], dp[mask] + cost[i][j])

        return dp[(1 << n) - 1]
