#1143. Longest Common Subsequence
#Medium
#
#Given two strings text1 and text2, return the length of their longest common
#subsequence. If there is no common subsequence, return 0.
#
#A subsequence of a string is a new string generated from the original string
#with some characters (can be none) deleted without changing the relative order
#of the remaining characters.
#
#A common subsequence of two strings is a subsequence that is common to both strings.
#
#Example 1:
#Input: text1 = "abcde", text2 = "ace"
#Output: 3
#Explanation: The longest common subsequence is "ace" and its length is 3.
#
#Example 2:
#Input: text1 = "abc", text2 = "abc"
#Output: 3
#
#Example 3:
#Input: text1 = "abc", text2 = "def"
#Output: 0
#
#Constraints:
#    1 <= text1.length, text2.length <= 1000
#    text1 and text2 consist of only lowercase English characters.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """2D DP - O(mn) time and space"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


class SolutionSpaceOptimized:
    """O(n) space using 1D array"""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Use shorter string for dp array
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m

        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n]


class SolutionMemoization:
    """Top-down with memoization"""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)


class SolutionGetLCS:
    """Also return the actual LCS string"""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Backtrack to find LCS
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                lcs.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        # lcs is reversed, but we just need length
        return dp[m][n]
