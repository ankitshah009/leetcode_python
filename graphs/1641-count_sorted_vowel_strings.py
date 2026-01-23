#1641. Count Sorted Vowel Strings
#Medium
#
#Given an integer n, return the number of strings of length n that consist only
#of vowels (a, e, i, o, u) and are lexicographically sorted.
#
#A string s is lexicographically sorted if for all valid i, s[i] is the same as
#or comes before s[i+1] in the alphabet.
#
#Example 1:
#Input: n = 1
#Output: 5
#Explanation: The 5 sorted strings are ["a","e","i","o","u"].
#
#Example 2:
#Input: n = 2
#Output: 15
#Explanation: The 15 sorted strings are:
#["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
#
#Example 3:
#Input: n = 33
#Output: 66045
#
#Constraints:
#    1 <= n <= 50

class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        Combinatorics: This is choosing n items from 5 with repetition allowed,
        where order doesn't matter (since we only care about sorted strings).

        This is C(n + 4, 4) = (n+4)! / (4! * n!)
        """
        # C(n+4, 4) = (n+4) * (n+3) * (n+2) * (n+1) / 24
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


class SolutionDP:
    def countVowelStrings(self, n: int) -> int:
        """
        DP approach: dp[i][j] = count of strings of length i ending with vowel j
        """
        # dp[j] = count of strings ending with j-th vowel (0=a, 1=e, 2=i, 3=o, 4=u)
        dp = [1, 1, 1, 1, 1]

        for _ in range(n - 1):
            # Each position can use vowels >= previous vowel
            # Compute prefix sums
            for i in range(1, 5):
                dp[i] += dp[i - 1]

        return sum(dp)


class SolutionRecursive:
    def countVowelStrings(self, n: int) -> int:
        """
        Recursive approach with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def count(length: int, start_vowel: int) -> int:
            # length = remaining characters to place
            # start_vowel = minimum vowel index (0-4)

            if length == 0:
                return 1

            total = 0
            for vowel in range(start_vowel, 5):
                total += count(length - 1, vowel)

            return total

        return count(n, 0)


class SolutionIterative:
    def countVowelStrings(self, n: int) -> int:
        """
        Iterative DP building up counts.
        """
        # counts[i] = strings that can start with vowel i or later
        # For n=1: all 5 vowels work
        # We track cumulative counts from right

        a = e = i = o = u = 1

        for _ in range(n - 1):
            # Update in order: u, o, i, e, a
            # u can only follow u
            # o can follow o or u
            # etc.
            a = a + e + i + o + u
            e = e + i + o + u
            i = i + o + u
            o = o + u
            # u stays the same

        return a + e + i + o + u


class SolutionMath:
    def countVowelStrings(self, n: int) -> int:
        """
        Pure math: stars and bars.
        Place n identical balls into 5 bins (vowels).
        Answer: C(n + 5 - 1, 5 - 1) = C(n + 4, 4)
        """
        from math import comb
        return comb(n + 4, 4)
