#1790. Check if One String Swap Can Make Strings Equal
#Easy
#
#You are given two strings s1 and s2 of equal length. A string swap is an
#operation where you choose two indices in a string (not necessarily different)
#and swap the characters at these indices.
#
#Return true if it is possible to make both strings equal by performing at most
#one string swap on exactly one of the strings. Otherwise, return false.
#
#Example 1:
#Input: s1 = "bank", s2 = "kanb"
#Output: true
#
#Example 2:
#Input: s1 = "attack", s2 = "defend"
#Output: false
#
#Example 3:
#Input: s1 = "kelb", s2 = "kelb"
#Output: true
#
#Constraints:
#    1 <= s1.length, s2.length <= 100
#    s1.length == s2.length
#    s1 and s2 consist of only lowercase English letters.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Find positions where strings differ.
        Must be 0 or 2 differences, and swapping must fix them.
        """
        diffs = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]

        if len(diffs) == 0:
            return True

        if len(diffs) == 2:
            return diffs[0] == diffs[1][::-1]

        return False


class SolutionExplicit:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Explicit index tracking.
        """
        diff_indices = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
                if len(diff_indices) > 2:
                    return False

        if len(diff_indices) == 0:
            return True

        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]

        return False


class SolutionCounter:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Using Counter to verify same characters.
        """
        from collections import Counter

        diffs = sum(1 for a, b in zip(s1, s2) if a != b)

        if diffs == 0:
            return True
        if diffs != 2:
            return False

        return Counter(s1) == Counter(s2)
