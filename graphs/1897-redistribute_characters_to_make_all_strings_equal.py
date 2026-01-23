#1897. Redistribute Characters to Make All Strings Equal
#Easy
#
#You are given an array of strings words (0-indexed).
#
#In one operation, pick two distinct indices i and j, where words[i] is a
#non-empty string, and move any character from words[i] to any position in
#words[j].
#
#Return true if you can make every string in words equal using any number of
#operations, and false otherwise.
#
#Example 1:
#Input: words = ["abc","aabc","bc"]
#Output: true
#
#Example 2:
#Input: words = ["ab","a"]
#Output: false
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 100
#    words[i] consists of lowercase English letters.

from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
        Count all characters. Each must be divisible by number of words.
        """
        n = len(words)
        total_count = Counter()

        for word in words:
            total_count.update(word)

        return all(count % n == 0 for count in total_count.values())


class SolutionOneLiner:
    def makeEqual(self, words: List[str]) -> bool:
        """
        One-liner using join and Counter.
        """
        n = len(words)
        return all(c % n == 0 for c in Counter(''.join(words)).values())


class SolutionManual:
    def makeEqual(self, words: List[str]) -> bool:
        """
        Manual counting without Counter.
        """
        n = len(words)
        counts = [0] * 26

        for word in words:
            for c in word:
                counts[ord(c) - ord('a')] += 1

        return all(count % n == 0 for count in counts)


class SolutionDetailed:
    def makeEqual(self, words: List[str]) -> bool:
        """
        Detailed explanation.

        To make all strings equal:
        - All strings must have same characters with same frequencies
        - Total count of each character must be divisible by number of words

        Example: words = ["abc", "aabc", "bc"]
        Combined: a=3, b=3, c=3
        n = 3
        Each character count is divisible by 3, so possible.
        Each word gets: a=1, b=1, c=1 -> "abc"
        """
        n = len(words)
        char_count = {}

        for word in words:
            for c in word:
                char_count[c] = char_count.get(c, 0) + 1

        for count in char_count.values():
            if count % n != 0:
                return False

        return True
