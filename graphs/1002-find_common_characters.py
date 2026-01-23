#1002. Find Common Characters
#Easy
#
#Given a string array words, return an array of all characters that show up in
#all strings within the words (including duplicates). You may return the answer
#in any order.
#
#Example 1:
#Input: words = ["bella","label","roller"]
#Output: ["e","l","l"]
#
#Example 2:
#Input: words = ["cool","lock","cook"]
#Output: ["c","o"]
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 100
#    words[i] consists of lowercase English letters.

from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        Intersection of character counts.
        """
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        return list(common.elements())


class SolutionExplicit:
    """More explicit counting"""

    def commonChars(self, words: list[str]) -> list[str]:
        # Min count of each char across all words
        min_count = [float('inf')] * 26

        for word in words:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            for i in range(26):
                min_count[i] = min(min_count[i], count[i])

        result = []
        for i in range(26):
            result.extend([chr(ord('a') + i)] * min_count[i])

        return result


class SolutionReduce:
    """Using reduce"""

    def commonChars(self, words: list[str]) -> list[str]:
        from functools import reduce

        common = reduce(lambda a, b: a & b, map(Counter, words))
        return list(common.elements())
