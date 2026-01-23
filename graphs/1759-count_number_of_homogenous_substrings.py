#1759. Count Number of Homogenous Substrings
#Medium
#
#Given a string s, return the number of homogenous substrings of s. Since the
#answer may be too large, return it modulo 10^9 + 7.
#
#A string is homogenous if all the characters of the string are the same.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: s = "abbcccaa"
#Output: 13
#
#Example 2:
#Input: s = "xy"
#Output: 2
#
#Example 3:
#Input: s = "zzzzz"
#Output: 15
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of lowercase letters.

class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        Count consecutive runs and sum n*(n+1)/2 for each run of length n.
        """
        MOD = 10**9 + 7
        result = 0
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result = (result + count * (count + 1) // 2) % MOD
                count = 1

        # Add last run
        result = (result + count * (count + 1) // 2) % MOD

        return result


class SolutionGroupBy:
    def countHomogenous(self, s: str) -> int:
        """
        Using itertools.groupby.
        """
        from itertools import groupby

        MOD = 10**9 + 7
        result = 0

        for _, group in groupby(s):
            n = len(list(group))
            result = (result + n * (n + 1) // 2) % MOD

        return result


class SolutionRunning:
    def countHomogenous(self, s: str) -> int:
        """
        Running count approach.
        """
        MOD = 10**9 + 7
        result = 0
        run_length = 0

        for i, c in enumerate(s):
            if i == 0 or c == s[i - 1]:
                run_length += 1
            else:
                run_length = 1
            result = (result + run_length) % MOD

        return result
