#1684. Count the Number of Consistent Strings
#Easy
#
#You are given a string allowed consisting of distinct characters and an array
#of strings words. A string is consistent if all characters in the string
#appear in the string allowed.
#
#Return the number of consistent strings in the array words.
#
#Example 1:
#Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
#Output: 2
#Explanation: "aaab" and "baa" are consistent since they only contain 'a' and 'b'.
#
#Example 2:
#Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
#Output: 7
#Explanation: All strings are consistent.
#
#Example 3:
#Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
#Output: 4
#Explanation: "cc", "acd", "ac", and "d" are consistent.
#
#Constraints:
#    1 <= words.length <= 10^4
#    1 <= allowed.length <= 26
#    1 <= words[i].length <= 10
#    The characters in allowed are distinct.
#    words[i] and allowed contain only lowercase English letters.

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Use set for O(1) character lookup.
        """
        allowed_set = set(allowed)
        count = 0

        for word in words:
            if all(c in allowed_set for c in word):
                count += 1

        return count


class SolutionBitmask:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Use bitmask for efficient comparison.
        """
        allowed_mask = 0
        for c in allowed:
            allowed_mask |= (1 << (ord(c) - ord('a')))

        count = 0

        for word in words:
            word_mask = 0
            for c in word:
                word_mask |= (1 << (ord(c) - ord('a')))

            if (word_mask & ~allowed_mask) == 0:
                count += 1

        return count


class SolutionSetOps:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Using set operations.
        """
        allowed_set = set(allowed)
        return sum(1 for word in words if set(word) <= allowed_set)


class SolutionExplicit:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        Explicit nested loops.
        """
        allowed_set = set(allowed)
        count = 0

        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed_set:
                    is_consistent = False
                    break

            if is_consistent:
                count += 1

        return count


class SolutionCompact:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        One-liner solution.
        """
        a = set(allowed)
        return sum(set(w) <= a for w in words)
