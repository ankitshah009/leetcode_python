#516. Longest Palindromic Subsequence
#Medium
#
#Given a string s, find the longest palindromic subsequence's length in s.
#
#A subsequence is a sequence that can be derived from another sequence by deleting
#some or no elements without changing the order of the remaining elements.
#
#Example 1:
#Input: s = "bbbab"
#Output: 4
#Explanation: One possible longest palindromic subsequence is "bbbb".
#
#Example 2:
#Input: s = "cbbd"
#Output: 2
#Explanation: One possible longest palindromic subsequence is "bb".
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists only of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        DP approach: dp[i][j] = longest palindromic subsequence in s[i:j+1]
        This is equivalent to LCS of s and reverse(s)
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]


class SolutionLCS:
    """LCS of string and its reverse"""

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]

        # LCS DP
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][n]


class SolutionSpaceOptimized:
    """O(n) space optimization"""

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n

        for i in range(n - 2, -1, -1):
            prev = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp

        return dp[n-1]


class SolutionMemo:
    """Top-down with memoization"""

    def longestPalindromeSubseq(self, s: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dp(i+1, j-1) + 2
            return max(dp(i+1, j), dp(i, j-1))

        return dp(0, len(s) - 1)
