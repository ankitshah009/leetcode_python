#115. Distinct Subsequences
#Hard
#
#Given two strings s and t, return the number of distinct subsequences of s which
#equals t.
#
#The test cases are generated so that the answer fits on a 32-bit signed integer.
#
#Example 1:
#Input: s = "rabbbit", t = "rabbit"
#Output: 3
#Explanation:
#There are 3 ways you can generate "rabbit" from s.
#
#Example 2:
#Input: s = "babgbag", t = "bag"
#Output: 5
#Explanation:
#There are 5 ways you can generate "bag" from s.
#
#Constraints:
#    1 <= s.length, t.length <= 1000
#    s and t consist of English letters.

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] = number of ways to form t[0:j] from s[0:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty t can be formed from any prefix of s in exactly 1 way
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Don't use s[i-1]
                dp[i][j] = dp[i-1][j]

                # Use s[i-1] if it matches t[j-1]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[m][n]

    # Space-optimized version
    def numDistinctOptimized(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            # Traverse backwards to avoid using updated values
            for j in range(min(i, n), 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]

        return dp[n]
