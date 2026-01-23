#44. Wildcard Matching
#Hard
#
#Given an input string (s) and a pattern (p), implement wildcard pattern matching
#with support for '?' and '*' where:
#    '?' Matches any single character.
#    '*' Matches any sequence of characters (including the empty sequence).
#
#The matching should cover the entire input string (not partial).
#
#Example 1:
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".
#
#Example 2:
#Input: s = "aa", p = "*"
#Output: true
#Explanation: '*' matches any sequence.
#
#Example 3:
#Input: s = "cb", p = "?a"
#Output: false
#Explanation: '?' matches 'c', but the second letter is 'a', which does not
#match 'b'.
#
#Constraints:
#    0 <= s.length, p.length <= 2000
#    s contains only lowercase English letters.
#    p contains only lowercase English letters, '?' or '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Dynamic Programming - O(mn) time and space.
        """
        m, n = len(s), len(p)

        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Empty string matches pattern of only '*'s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Match empty or match one char and continue
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


class SolutionGreedy:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Two pointer greedy approach - O(mn) worst case, often better.
        """
        s_idx = p_idx = 0
        star_idx = match_idx = -1

        while s_idx < len(s):
            # Match single character
            if p_idx < len(p) and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            # Match star - record position and try matching empty sequence
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
            # Backtrack to previous star
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
            else:
                return False

        # Check remaining pattern characters (must be all '*')
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1

        return p_idx == len(p)


class SolutionMemoization:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Top-down DP with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            # Base cases
            if j == len(p):
                return i == len(s)
            if i == len(s):
                return all(c == '*' for c in p[j:])

            if p[j] == '*':
                # Match empty or match one char
                return dp(i, j + 1) or dp(i + 1, j)
            elif p[j] == '?' or p[j] == s[i]:
                return dp(i + 1, j + 1)
            else:
                return False

        return dp(0, 0)


class SolutionSpaceOptimized:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Space-optimized DP - O(n) space.
        """
        m, n = len(s), len(p)

        # Only need previous row
        prev = [False] * (n + 1)
        prev[0] = True

        # Handle leading '*'s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        # Fill row by row
        for i in range(1, m + 1):
            curr = [False] * (n + 1)

            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    curr[j] = curr[j - 1] or prev[j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    curr[j] = prev[j - 1]

            prev = curr

        return prev[n]
