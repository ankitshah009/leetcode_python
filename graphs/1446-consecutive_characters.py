#1446. Consecutive Characters
#Easy
#
#The power of the string is the maximum length of a non-empty substring that
#contains only one unique character.
#
#Given a string s, return the power of s.
#
#Example 1:
#Input: s = "leetcode"
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.
#
#Example 2:
#Input: s = "abbcccddddeeeeedcba"
#Output: 5
#Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of only lowercase English letters.

class Solution:
    def maxPower(self, s: str) -> int:
        """
        Track current run length and update max.
        """
        if not s:
            return 0

        max_power = 1
        current_length = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_length += 1
                max_power = max(max_power, current_length)
            else:
                current_length = 1

        return max_power


class SolutionGroupby:
    def maxPower(self, s: str) -> int:
        """Using itertools.groupby"""
        from itertools import groupby

        return max(len(list(group)) for _, group in groupby(s))


class SolutionTwoPointer:
    def maxPower(self, s: str) -> int:
        """Two pointer approach"""
        max_len = 0
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            max_len = max(max_len, j - i)
            i = j

        return max_len


class SolutionRegex:
    def maxPower(self, s: str) -> int:
        """Using regex to find runs"""
        import re

        # Find all runs of same character
        runs = re.findall(r'(.)\1*', s)
        return max(len(run) for run in runs)
