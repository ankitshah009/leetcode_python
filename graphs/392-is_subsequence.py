#392. Is Subsequence
#Easy
#
#Given two strings s and t, return true if s is a subsequence of t, or false
#otherwise.
#
#A subsequence of a string is a new string that is formed from the original
#string by deleting some (can be none) of the characters without disturbing the
#relative positions of the remaining characters.
#
#Example 1:
#Input: s = "abc", t = "ahbgdc"
#Output: true
#
#Example 2:
#Input: s = "axc", t = "ahbgdc"
#Output: false
#
#Constraints:
#    0 <= s.length <= 100
#    0 <= t.length <= 10^4
#    s and t consist only of lowercase English letters.
#
#Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where
#k >= 10^9, and you want to check one by one to see if t has its subsequence.
#In this scenario, how would you change your code?

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Two pointer approach"""
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


class SolutionIterator:
    """Using iterator"""

    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)
        return all(c in t_iter for c in s)


class SolutionFollowUp:
    """
    Follow-up: Preprocess t for multiple queries.
    Build index of character positions for O(log n) per character lookup.
    """

    def __init__(self, t: str):
        from collections import defaultdict
        import bisect

        # char_indices[c] = sorted list of indices where c appears in t
        self.char_indices = defaultdict(list)
        for i, c in enumerate(t):
            self.char_indices[c].append(i)

    def isSubsequence(self, s: str) -> bool:
        import bisect

        current_pos = -1

        for c in s:
            if c not in self.char_indices:
                return False

            indices = self.char_indices[c]
            # Find first index > current_pos
            idx = bisect.bisect_right(indices, current_pos)

            if idx == len(indices):
                return False

            current_pos = indices[idx]

        return True


class SolutionDP:
    """DP approach (overkill for this problem but educational)"""

    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # dp[i][j] = True if s[:i] is subsequence of t[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string is subsequence of anything
        for j in range(n + 1):
            dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n]
