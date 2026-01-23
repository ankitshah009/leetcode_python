#1657. Determine if Two Strings Are Close
#Medium
#
#Two strings are considered close if you can attain one from the other using
#the following operations:
#
#Operation 1: Swap any two existing characters.
#    For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another
#             existing character, and do the same with the other character.
#    For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#
#You can use the operations on either string as many times as necessary.
#
#Given two strings, word1 and word2, return true if word1 and word2 are close,
#and false otherwise.
#
#Example 1:
#Input: word1 = "abc", word2 = "bca"
#Output: true
#Explanation: You can attain word2 from word1 in 2 operations.
#Apply Operation 1: "abc" -> "acb"
#Apply Operation 1: "acb" -> "bca"
#
#Example 2:
#Input: word1 = "a", word2 = "aa"
#Output: false
#Explanation: It is impossible to attain word2 from word1, or vice versa.
#
#Example 3:
#Input: word1 = "cabbba", word2 = "abbccc"
#Output: true
#Explanation: You can attain word2 from word1 in 3 operations.
#Apply Operation 1: "cabbba" -> "caabbb"
#Apply Operation 2: "caabbb" -> "baaccc"
#Apply Operation 2: "baaccc" -> "abbccc"
#
#Constraints:
#    1 <= word1.length, word2.length <= 10^5
#    word1 and word2 contain only lowercase English letters.

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Two strings are close if:
        1. They have the same set of characters
        2. They have the same frequency distribution (sorted frequencies match)
        """
        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Check same character set
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # Check same frequency distribution
        return sorted(freq1.values()) == sorted(freq2.values())


class SolutionDetailed:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Detailed implementation with explicit checks.
        """
        # Length check
        if len(word1) != len(word2):
            return False

        # Count frequencies
        count1 = [0] * 26
        count2 = [0] * 26

        for c in word1:
            count1[ord(c) - ord('a')] += 1
        for c in word2:
            count2[ord(c) - ord('a')] += 1

        # Check same character set
        for i in range(26):
            if (count1[i] == 0) != (count2[i] == 0):
                return False

        # Check frequency distribution
        return sorted(count1) == sorted(count2)


class SolutionSet:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Using set operations.
        """
        set1, set2 = set(word1), set(word2)

        if set1 != set2:
            return False

        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())

        return freq1 == freq2


class SolutionCounter:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Using Counter for both checks.
        """
        c1, c2 = Counter(word1), Counter(word2)

        return (c1.keys() == c2.keys() and
                Counter(c1.values()) == Counter(c2.values()))


class SolutionCompact:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        One-liner approach.
        """
        c1, c2 = Counter(word1), Counter(word2)
        return (set(c1) == set(c2) and
                sorted(c1.values()) == sorted(c2.values()))
