#1312. Minimum Insertion Steps to Make a String Palindrome
#Hard
#
#Given a string s. In one step you can insert any character at any index of
#the string.
#
#Return the minimum number of steps to make s palindrome.
#
#A Palindrome String is one that reads the same backward as well as forward.
#
#Example 1:
#Input: s = "zzazz"
#Output: 0
#Explanation: The string "zzazz" is already palindrome we do not need any insertions.
#
#Example 2:
#Input: s = "mbadm"
#Output: 2
#Explanation: String can be "mbdadbm" or "mdbabdm".
#
#Example 3:
#Input: s = "leetcode"
#Output: 5
#Explanation: Inserting 5 characters the string becomes "leetcodocteel".
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of lowercase English letters.

class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Minimum insertions = n - LPS (Longest Palindromic Subsequence)
        LPS can be found using DP similar to LCS of s and reverse(s).
        """
        n = len(s)
        t = s[::-1]

        # LCS of s and reverse(s) = LPS of s
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lps = dp[n][n]
        return n - lps


class SolutionOptimized:
    def minInsertions(self, s: str) -> int:
        """Space optimized: O(n) space"""
        n = len(s)
        t = s[::-1]

        prev = [0] * (n + 1)

        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        return n - prev[n]


class SolutionDirectDP:
    def minInsertions(self, s: str) -> int:
        """
        Direct DP approach:
        dp[i][j] = min insertions to make s[i:j+1] palindrome
        """
        n = len(s)

        # dp[i][j] = min insertions for substring s[i..j]
        dp = [[0] * n for _ in range(n)]

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


class SolutionMemo:
    def minInsertions(self, s: str) -> int:
        """Top-down with memoization"""
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            return 1 + min(dp(i + 1, j), dp(i, j - 1))

        return dp(0, len(s) - 1)
