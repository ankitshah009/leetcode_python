#1180. Count Substrings with Only One Distinct Letter
#Easy
#
#Given a string s, return the number of substrings that have only one distinct letter.
#
#Example 1:
#Input: s = "aaaba"
#Output: 8
#Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
#"aaa" occurs 1 time.
#"aa" occurs 2 times.
#"a" occurs 4 times.
#"b" occurs 1 time.
#So the answer is 1 + 2 + 4 + 1 = 8.
#
#Example 2:
#Input: s = "aaaaaaaaaa"
#Output: 55
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] consists of only lowercase English letters.

class Solution:
    def countLetters(self, s: str) -> int:
        """
        For a run of k same characters, number of substrings = k*(k+1)/2
        """
        if not s:
            return 0

        total = 0
        i = 0

        while i < len(s):
            # Count consecutive same characters
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1

            length = j - i
            # Number of substrings in a run of length k is k*(k+1)/2
            total += length * (length + 1) // 2
            i = j

        return total


class SolutionOnePass:
    def countLetters(self, s: str) -> int:
        """One-pass solution counting incrementally"""
        total = 0
        count = 1  # Current run length

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            total += count

        return total


class SolutionGroupBy:
    def countLetters(self, s: str) -> int:
        """Using itertools.groupby"""
        from itertools import groupby

        total = 0
        for _, group in groupby(s):
            length = len(list(group))
            total += length * (length + 1) // 2

        return total
