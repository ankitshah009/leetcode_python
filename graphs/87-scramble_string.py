#87. Scramble String
#Hard
#
#We can scramble a string s to get a string t using the following algorithm:
#1. If the length of the string is 1, stop.
#2. If the length of the string is > 1, do the following:
#   - Split the string into two non-empty substrings at a random index.
#   - Randomly decide to swap the two substrings or keep them in the same order.
#   - Apply step 1 recursively on each of the two substrings.
#
#Given two strings s1 and s2 of the same length, return true if s2 is a scrambled
#string of s1, otherwise, return false.
#
#Example 1:
#Input: s1 = "great", s2 = "rgeat"
#Output: true
#
#Example 2:
#Input: s1 = "abcde", s2 = "caebd"
#Output: false
#
#Example 3:
#Input: s1 = "a", s2 = "a"
#Output: true
#
#Constraints:
#    s1.length == s2.length
#    1 <= s1.length <= 30
#    s1 and s2 consist of lowercase English letters.

from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Memoized recursion.
        """
        @lru_cache(maxsize=None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True

            if Counter(a) != Counter(b):
                return False

            n = len(a)
            for i in range(1, n):
                # No swap: compare a[:i] with b[:i] and a[i:] with b[i:]
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True

                # Swap: compare a[:i] with b[n-i:] and a[i:] with b[:n-i]
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    return True

            return False

        return dfs(s1, s2)


class SolutionDP:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        3D DP approach.
        dp[length][i][j] = True if s1[i:i+length] can be scrambled to s2[j:j+length]
        """
        n = len(s1)
        if n != len(s2):
            return False

        # dp[length][i][j]
        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]

        # Base case: length 1
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        # Fill for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        # No swap
                        if dp[k][i][j] and dp[length - k][i + k][j + k]:
                            dp[length][i][j] = True
                            break

                        # Swap
                        if dp[k][i][j + length - k] and dp[length - k][i + k][j]:
                            dp[length][i][j] = True
                            break

        return dp[n][0][0]


class SolutionRecursive:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Simple recursive with early termination.
        """
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)
        for i in range(1, n):
            # No swap
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            # Swap
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True

        return False
