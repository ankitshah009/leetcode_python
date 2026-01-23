#10. Regular Expression Matching
#Hard
#
#Given an input string s and a pattern p, implement regular expression matching
#with support for '.' and '*' where:
#    '.' Matches any single character.
#    '*' Matches zero or more of the preceding element.
#
#The matching should cover the entire input string (not partial).
#
#Example 1:
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#
#Example 2:
#Input: s = "aa", p = "a*"
#Output: true
#Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
#by repeating 'a' once, it becomes "aa".
#
#Example 3:
#Input: s = "ab", p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".
#
#Constraints:
#    1 <= s.length <= 20
#    1 <= p.length <= 20
#    s contains only lowercase English letters.
#    p contains only lowercase English letters, '.', and '*'.
#    It is guaranteed for each appearance of '*', there will be a previous
#    valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Dynamic Programming - Bottom Up.
        dp[i][j] = True if s[0:i] matches p[0:j]
        """
        m, n = len(s), len(p)

        # dp[i][j] represents if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Zero occurrences of preceding element
                    dp[i][j] = dp[i][j - 2]

                    # One or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


class SolutionMemoization:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Top-down recursion with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            # Base case: pattern exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # If next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Skip pattern (zero occurrences) OR match one and continue
                return dp(i, j + 2) or (first_match and dp(i + 1, j))

            # No '*', must match current character
            return first_match and dp(i + 1, j + 1)

        return dp(0, 0)


class SolutionRecursive:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Pure recursive solution (slower, for understanding).
        """
        if not p:
            return not s

        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')

        if len(p) >= 2 and p[1] == '*':
            # Try zero occurrences or one occurrence of p[0]
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
