#521. Longest Uncommon Subsequence I
#Easy
#
#Given two strings a and b, return the length of the longest uncommon subsequence
#between a and b. If no such uncommon subsequence exists, return -1.
#
#An uncommon subsequence between two strings is a string that is a subsequence of
#exactly one of them.
#
#Example 1:
#Input: a = "aba", b = "cdc"
#Output: 3
#Explanation: One longest uncommon subsequence is "aba" because "aba" is a
#subsequence of "aba" but not "cdc".
#
#Example 2:
#Input: a = "aaa", b = "bbb"
#Output: 3
#
#Example 3:
#Input: a = "aaa", b = "aaa"
#Output: -1
#
#Constraints:
#    1 <= a.length, b.length <= 100
#    a and b consist of lower-case English letters.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        """
        If strings are equal, no uncommon subsequence exists.
        Otherwise, the longer string itself is the answer
        (it can't be a subsequence of the shorter one).
        If same length but different, either string works.
        """
        if a == b:
            return -1
        return max(len(a), len(b))


class SolutionExplicit:
    """More explicit logic"""

    def findLUSlength(self, a: str, b: str) -> int:
        # If strings are identical, no uncommon subsequence
        if a == b:
            return -1

        # The longer string can't be a subsequence of shorter
        # If same length but different, both are valid answers
        return max(len(a), len(b))
