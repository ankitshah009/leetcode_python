#516. Longest Palindromic Subsequence
#Medium
#
#Given a string s, find the longest palindromic subsequence's length in s.
#
#A subsequence is a sequence that can be derived from another sequence by deleting some or
#no elements without changing the order of the remaining elements.
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
        n = len(s)
        # dp[i][j] = length of longest palindromic subsequence in s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
