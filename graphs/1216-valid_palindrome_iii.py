#1216. Valid Palindrome III
#Hard
#
#Given a string s and an integer k, return true if s is a k-palindrome.
#
#A string is k-palindrome if it can be transformed into a palindrome by
#removing at most k characters from it.
#
#Example 1:
#Input: s = "abcdeca", k = 2
#Output: true
#Explanation: Remove 'b' and 'e' characters.
#
#Example 2:
#Input: s = "abbababa", k = 1
#Output: true
#
#Constraints:
#    1 <= s.length <= 1000
#    s consists of only lowercase English letters.
#    1 <= k <= s.length

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        Find longest palindromic subsequence (LPS).
        If len(s) - LPS <= k, then it's k-palindrome.

        LPS is equivalent to LCS of s and reverse(s).
        """
        n = len(s)
        rev = s[::-1]

        # LCS DP
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lps = dp[n][n]
        return n - lps <= k


class SolutionOptimized:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """Space-optimized LCS"""
        n = len(s)
        rev = s[::-1]

        # Use two rows
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev, curr = curr, prev

        lps = prev[n]
        return n - lps <= k


class SolutionMemo:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """Direct palindrome check with memoization"""
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def min_deletions(left, right):
            """Minimum deletions to make s[left:right+1] a palindrome"""
            if left >= right:
                return 0

            if s[left] == s[right]:
                return min_deletions(left + 1, right - 1)

            # Delete either left or right character
            return 1 + min(min_deletions(left + 1, right),
                          min_deletions(left, right - 1))

        return min_deletions(0, len(s) - 1) <= k
