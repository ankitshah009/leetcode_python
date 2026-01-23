#1967. Number of Strings That Appear as Substrings in Word
#Easy
#
#Given an array of strings patterns and a string word, return the number of
#strings in patterns that exist as a substring in word.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: patterns = ["a","abc","bc","d"], word = "abc"
#Output: 3
#Explanation: "a" is a substring of "abc".
#"abc" is a substring of "abc".
#"bc" is a substring of "abc".
#
#Example 2:
#Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
#Output: 2
#
#Example 3:
#Input: patterns = ["a","a","a"], word = "ab"
#Output: 3
#
#Constraints:
#    1 <= patterns.length <= 100
#    1 <= patterns[i].length <= 100
#    1 <= word.length <= 100
#    patterns[i] and word consist of lowercase English letters.

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Count patterns that are substrings of word.
        """
        return sum(1 for p in patterns if p in word)


class SolutionExplicit:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Explicit loop version.
        """
        count = 0

        for pattern in patterns:
            if pattern in word:
                count += 1

        return count


class SolutionFind:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Using find method.
        """
        count = 0

        for pattern in patterns:
            if word.find(pattern) != -1:
                count += 1

        return count
