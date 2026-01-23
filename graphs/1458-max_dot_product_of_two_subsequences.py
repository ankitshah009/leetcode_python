#1458. Max Dot Product of Two Subsequences
#Hard
#
#Given two arrays nums1 and nums2.
#
#Return the maximum dot product between non-empty subsequences of nums1 and nums2
#with the same length.
#
#A subsequence of a array is a new array which is formed from the original array
#by deleting some (can be none) of the characters without disturbing the relative
#positions of the remaining characters. (ie, [2,3,5] is a subsequence of
#[1,2,3,4,5] while [1,5,3] is not).
#
#Example 1:
#Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
#Output: 18
#Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
#Their dot product is (2*3 + (-2)*(-6)) = 18.
#
#Example 2:
#Input: nums1 = [3,-2], nums2 = [2,-6,7]
#Output: 21
#Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
#Their dot product is (3*7) = 21.
#
#Example 3:
#Input: nums1 = [-1,-1], nums2 = [1,1]
#Output: -1
#Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
#Their dot product is -1.
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 500
#    -1000 <= nums1[i], nums2[i] <= 1000

from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        DP similar to LCS.
        dp[i][j] = max dot product using nums1[:i] and nums2[:j]

        Transitions:
        - dp[i][j] = dp[i-1][j] (skip nums1[i-1])
        - dp[i][j] = dp[i][j-1] (skip nums2[j-1])
        - dp[i][j] = max(0, dp[i-1][j-1]) + nums1[i-1]*nums2[j-1] (use both)
        """
        m, n = len(nums1), len(nums2)

        # dp[i][j] = max dot product for subsequences ending at or before i, j
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Product of current elements
                product = nums1[i - 1] * nums2[j - 1]

                # Either use this pair (optionally with previous best)
                # Or skip one of the elements
                dp[i][j] = max(
                    product,                          # Start new with just this pair
                    dp[i - 1][j - 1] + product,      # Extend previous
                    dp[i - 1][j],                     # Skip nums1[i-1]
                    dp[i][j - 1]                      # Skip nums2[j-1]
                )

        return dp[m][n]


class SolutionMemo:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """Memoization approach"""
        from functools import lru_cache

        m, n = len(nums1), len(nums2)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == m or j == n:
                return float('-inf')

            # Take both current elements
            take = nums1[i] * nums2[j] + max(0, dp(i + 1, j + 1))

            # Skip one element
            skip_i = dp(i + 1, j)
            skip_j = dp(i, j + 1)

            return max(take, skip_i, skip_j)

        return dp(0, 0)


class SolutionOptimized:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """Space-optimized O(n) solution"""
        m, n = len(nums1), len(nums2)

        prev = [float('-inf')] * (n + 1)
        curr = [float('-inf')] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i - 1] * nums2[j - 1]
                curr[j] = max(
                    product,
                    prev[j - 1] + product,
                    prev[j],
                    curr[j - 1]
                )
            prev, curr = curr, [float('-inf')] * (n + 1)

        return prev[n]
