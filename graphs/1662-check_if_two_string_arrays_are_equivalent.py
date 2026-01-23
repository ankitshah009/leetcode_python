#1662. Check If Two String Arrays are Equivalent
#Easy
#
#Given two string arrays word1 and word2, return true if the two arrays
#represent the same string, and false otherwise.
#
#A string is represented by an array if the array elements concatenated in
#order forms the string.
#
#Example 1:
#Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
#Output: true
#Explanation: word1 -> "ab" + "c" -> "abc"
#            word2 -> "a" + "bc" -> "abc"
#
#Example 2:
#Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
#Output: false
#
#Example 3:
#Input: word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]
#Output: true
#
#Constraints:
#    1 <= word1.length, word2.length <= 10^3
#    1 <= word1[i].length, word2[i].length <= 10^3
#    1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
#    word1[i] and word2[i] consist of lowercase letters.

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Simple concatenation comparison.
        """
        return ''.join(word1) == ''.join(word2)


class SolutionGenerator:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Generator-based character comparison (O(1) extra space).
        """
        def gen_chars(words):
            for word in words:
                for char in word:
                    yield char

        gen1 = gen_chars(word1)
        gen2 = gen_chars(word2)

        for c1, c2 in zip(gen1, gen2):
            if c1 != c2:
                return False

        # Check both generators exhausted
        try:
            next(gen1)
            return False
        except StopIteration:
            pass

        try:
            next(gen2)
            return False
        except StopIteration:
            pass

        return True


class SolutionTwoPointer:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Two pointer approach without creating new strings.
        """
        # Pointers for word arrays
        i1, i2 = 0, 0
        # Pointers for characters within current word
        j1, j2 = 0, 0

        while i1 < len(word1) and i2 < len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False

            # Move character pointers
            j1 += 1
            j2 += 1

            # Move to next word if needed
            if j1 == len(word1[i1]):
                i1 += 1
                j1 = 0

            if j2 == len(word2[i2]):
                i2 += 1
                j2 = 0

        # Both should be exhausted
        return i1 == len(word1) and i2 == len(word2)


class SolutionItertools:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Using itertools.chain and zip_longest.
        """
        from itertools import chain, zip_longest

        for c1, c2 in zip_longest(chain(*word1), chain(*word2)):
            if c1 != c2:
                return False

        return True


class SolutionCompact:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        One-liner with itertools.
        """
        from itertools import chain, zip_longest
        return all(c1 == c2 for c1, c2 in zip_longest(chain(*word1), chain(*word2)))
