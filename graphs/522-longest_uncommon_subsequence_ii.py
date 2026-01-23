#522. Longest Uncommon Subsequence II
#Medium
#
#Given an array of strings strs, return the length of the longest uncommon
#subsequence between them. If the longest uncommon subsequence does not exist,
#return -1.
#
#An uncommon subsequence between an array of strings is a string that is a
#subsequence of one string but not the others.
#
#A subsequence of a string s is a string that can be obtained after deleting any
#number of characters from s.
#
#Example 1:
#Input: strs = ["aba","cdc","eae"]
#Output: 3
#
#Example 2:
#Input: strs = ["aaa","aaa","aa"]
#Output: -1
#
#Constraints:
#    2 <= strs.length <= 50
#    1 <= strs[i].length <= 10
#    strs[i] consists of lowercase English letters.

from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        Check each string to see if it's a subsequence of any other.
        Return longest string that isn't a subsequence of others.
        """
        def is_subsequence(s, t):
            """Check if s is subsequence of t"""
            if len(s) > len(t):
                return False
            it = iter(t)
            return all(c in it for c in s)

        # Sort by length descending
        strs.sort(key=len, reverse=True)

        for i, s in enumerate(strs):
            # Check if s is subsequence of any other string
            is_uncommon = True
            for j, t in enumerate(strs):
                if i != j and is_subsequence(s, t):
                    is_uncommon = False
                    break

            if is_uncommon:
                return len(s)

        return -1


class SolutionWithCount:
    """Handle duplicates explicitly"""

    def findLUSlength(self, strs: List[str]) -> int:
        from collections import Counter

        def is_subsequence(s, t):
            it = iter(t)
            return all(c in it for c in s)

        count = Counter(strs)

        # Sort unique strings by length descending
        unique = sorted(count.keys(), key=len, reverse=True)

        for s in unique:
            # If string appears more than once, skip
            if count[s] > 1:
                continue

            # Check if s is subsequence of any longer string
            is_uncommon = True
            for t in strs:
                if len(t) > len(s) and is_subsequence(s, t):
                    is_uncommon = False
                    break

            if is_uncommon:
                return len(s)

        return -1
