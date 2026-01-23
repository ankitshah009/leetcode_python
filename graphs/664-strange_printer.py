#664. Strange Printer
#Hard
#
#There is a strange printer with the following two special properties:
#
#- The printer can only print a sequence of the same character each time.
#- At each turn, the printer can print new characters starting from and ending
#  at any place and will cover the original existing characters.
#
#Given a string s, return the minimum number of turns the printer needed to print it.
#
#Example 1:
#Input: s = "aaabbb"
#Output: 2
#Explanation: Print "aaa" first and then print "bbb".
#
#Example 2:
#Input: s = "aba"
#Output: 2
#Explanation: Print "aaa" first and then print "b" from the second place.
#
#Constraints:
#    1 <= s.length <= 100
#    s consists of lowercase English letters.

class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        Interval DP.
        dp[i][j] = minimum turns to print s[i:j+1]
        """
        # Remove consecutive duplicates
        s = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i-1])
        n = len(s)

        if n == 0:
            return 0

        # dp[i][j] = min turns to print s[i..j]
        dp = [[0] * n for _ in range(n)]

        # Base case: single character
        for i in range(n):
            dp[i][i] = 1

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Worst case: print s[i] alone, then print s[i+1..j]
                dp[i][j] = dp[i + 1][j] + 1

                # Try to combine s[i] with matching character s[k]
                for k in range(i + 1, j + 1):
                    if s[k] == s[i]:
                        # Print s[i..k] together with s[k..j]
                        cost = dp[i + 1][k] + (dp[k + 1][j] if k + 1 <= j else 0)
                        dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]


class SolutionMemo:
    """Top-down memoization"""

    def strangePrinter(self, s: str) -> int:
        from functools import lru_cache

        # Remove consecutive duplicates
        s = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i-1])
        n = len(s)

        if n == 0:
            return 0

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1

            # Print s[i] alone
            result = dp(i + 1, j) + 1

            # Try matching s[i] with later characters
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    result = min(result, dp(i + 1, k) + dp(k + 1, j))

            return result

        return dp(0, n - 1)


class SolutionAlt:
    """Alternative DP formulation"""

    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][n - 1]
