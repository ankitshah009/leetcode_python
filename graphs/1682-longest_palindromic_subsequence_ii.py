#1682. Longest Palindromic Subsequence II
#Medium
#
#A subsequence of a string s is considered a good palindromic subsequence if:
#- It is a subsequence of s.
#- It is a palindrome (has the same value if reversed).
#- It has an even length.
#- No two consecutive characters are equal, except the two middle ones.
#
#For example, if s = "abcabcabb", then "abba" is considered a good palindromic
#subsequence, while "bcb" (not even length) and "bbbb" (has equal consecutive
#characters) are not.
#
#Given a string s, return the length of the longest good palindromic subsequence
#in s.
#
#Example 1:
#Input: s = "bbabab"
#Output: 4
#Explanation: The longest good palindromic subsequence of s is "baab".
#
#Example 2:
#Input: s = "dcbccacdb"
#Output: 4
#Explanation: The longest good palindromic subsequence of s is "dccd".
#
#Constraints:
#    1 <= s.length <= 250
#    s consists of lowercase English letters.

from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        DP with state (left, right, last_char).
        last_char tracks the last character used on each end.
        """
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(left: int, right: int, last: str) -> int:
            if left >= right:
                return 0

            result = 0

            # Try to match s[left] with some s[j] where j <= right
            # and s[left] == s[j] and s[left] != last

            if s[left] == s[right] and s[left] != last:
                result = 2 + dp(left + 1, right - 1, s[left])

            # Skip left or right
            result = max(result, dp(left + 1, right, last))
            result = max(result, dp(left, right - 1, last))

            return result

        return dp(0, n - 1, '')


class SolutionIterative:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Iterative DP with 3D array.
        dp[i][j][c] = longest good palindrome in s[i:j+1] with last char c
        """
        n = len(s)
        # Use 26 for characters, 26 = no last char
        INF_CHAR = 26

        # dp[i][j][last] = length
        dp = [[[0] * 27 for _ in range(n)] for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for last in range(27):
                    last_char = chr(ord('a') + last) if last < 26 else ''

                    # Option 1: Match s[i] and s[j]
                    if s[i] == s[j] and s[i] != last_char:
                        char_idx = ord(s[i]) - ord('a')
                        if length == 2:
                            dp[i][j][last] = 2
                        else:
                            dp[i][j][last] = 2 + dp[i + 1][j - 1][char_idx]

                    # Option 2: Skip s[i]
                    if i + 1 <= j:
                        dp[i][j][last] = max(dp[i][j][last], dp[i + 1][j][last])

                    # Option 3: Skip s[j]
                    if i <= j - 1:
                        dp[i][j][last] = max(dp[i][j][last], dp[i][j - 1][last])

        return dp[0][n - 1][INF_CHAR]


class SolutionOptimized:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Optimized with memoization.
        """
        n = len(s)

        @lru_cache(maxsize=None)
        def solve(i: int, j: int, prev: int) -> int:
            """
            prev: index of last used character (0-25) or -1 for none
            """
            if i >= j:
                return 0

            result = max(solve(i + 1, j, prev), solve(i, j - 1, prev))

            if s[i] == s[j]:
                curr = ord(s[i]) - ord('a')
                if curr != prev:
                    result = max(result, 2 + solve(i + 1, j - 1, curr))

            return result

        return solve(0, n - 1, -1)


class SolutionClean:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Clean recursive solution.
        """
        n = len(s)
        memo = {}

        def dp(l: int, r: int, prev: str) -> int:
            if l >= r:
                return 0

            if (l, r, prev) in memo:
                return memo[(l, r, prev)]

            ans = max(dp(l + 1, r, prev), dp(l, r - 1, prev))

            if s[l] == s[r] and s[l] != prev:
                ans = max(ans, 2 + dp(l + 1, r - 1, s[l]))

            memo[(l, r, prev)] = ans
            return ans

        return dp(0, n - 1, '')
