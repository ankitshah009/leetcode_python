#1768. Merge Strings Alternately
#Easy
#
#You are given two strings word1 and word2. Merge the strings by adding letters
#in alternating order, starting with word1. If a string is longer than the other,
#append the additional letters onto the end of the merged string.
#
#Return the merged string.
#
#Example 1:
#Input: word1 = "abc", word2 = "pqr"
#Output: "apbqcr"
#Explanation: The merged string will be merged as so:
#word1:  a   b   c
#word2:    p   q   r
#merged: a p b q c r
#
#Example 2:
#Input: word1 = "ab", word2 = "pqrs"
#Output: "apbqrs"
#
#Example 3:
#Input: word1 = "abcd", word2 = "pq"
#Output: "apbqcd"
#
#Constraints:
#    1 <= word1.length, word2.length <= 100
#    word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Two pointers"""
        result = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters
        result.append(word1[i:])
        result.append(word2[j:])

        return ''.join(result)


class SolutionZip:
    """Using zip and concatenation"""

    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for c1, c2 in zip(word1, word2):
            merged.append(c1)
            merged.append(c2)

        # Append longer suffix
        i = min(len(word1), len(word2))
        merged.append(word1[i:])
        merged.append(word2[i:])

        return ''.join(merged)


class SolutionItertools:
    """Using itertools.zip_longest"""

    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest

        return ''.join(
            c1 + c2
            for c1, c2 in zip_longest(word1, word2, fillvalue='')
        )


class SolutionOneLiner:
    """Compact one-liner"""

    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]
