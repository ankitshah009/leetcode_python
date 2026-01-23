#1035. Uncrossed Lines
#Medium
#
#You are given two integer arrays nums1 and nums2. We write the integers of
#nums1 and nums2 (in the order they are given) on two separate horizontal
#lines.
#
#We may draw connecting lines: a straight line connecting two numbers
#nums1[i] and nums2[j] such that:
#    nums1[i] == nums2[j], and
#    the line we draw does not intersect any other connecting (non-horizontal)
#    line.
#
#Note that a connecting line cannot intersect even at the endpoints.
#
#Each number can only belong to one connecting line.
#
#Return the maximum number of connecting lines we can draw in this way.
#
#Example 1:
#Input: nums1 = [1,4,2], nums2 = [1,2,4]
#Output: 2
#Explanation: We can draw 2 uncrossed lines: 1-1 and 4-4 (or 2-2)
#
#Example 2:
#Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
#Output: 3
#
#Example 3:
#Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
#Output: 2
#
#Constraints:
#    1 <= nums1.length, nums2.length <= 500
#    1 <= nums1[i], nums2[j] <= 2000

from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        This is equivalent to Longest Common Subsequence (LCS).
        Lines don't cross iff we pick elements in increasing order of indices.
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


class SolutionSpaceOptimized:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """Space-optimized LCS using 1D array"""
        m, n = len(nums1), len(nums2)

        # Use shorter array for column dimension
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n]


class SolutionMemo:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """Memoized recursion"""
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dp(i + 1, j + 1)
            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)
