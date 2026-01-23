#1408. String Matching in an Array
#Easy
#
#Given an array of string words, return all strings in words that is a substring
#of another word. You can return the answer in any order.
#
#A substring is a contiguous sequence of characters within a string
#
#Example 1:
#Input: words = ["mass","as","hero","superhero"]
#Output: ["as","hero"]
#Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
#["hero","as"] is also a valid answer.
#
#Example 2:
#Input: words = ["leetcode","et","code"]
#Output: ["et","code"]
#Explanation: "et", "code" are substring of "leetcode".
#
#Example 3:
#Input: words = ["blue","green","bu"]
#Output: []
#Explanation: No string of words is substring of another string.
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 30
#    words[i] contains only lowercase English letters.
#    All the strings of words are unique.

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        For each word, check if it's a substring of any other word.
        O(n^2 * m) where m is max word length.
        """
        result = []

        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    result.append(word)
                    break

        return result


class SolutionOneLiner:
    def stringMatching(self, words: List[str]) -> List[str]:
        """Pythonic one-liner"""
        return [w for w in words if any(w in other and w != other for other in words)]


class SolutionConcatenate:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Concatenate all words with separator.
        Check if each word appears more than once (itself + in another).
        """
        # Join with unique separator
        joined = ' '.join(words)

        result = []
        for word in words:
            # If word appears in joined more than its own occurrence
            # Actually, we just check if it appears as substring of another word
            # By checking if it appears in the joined string excluding itself
            # Simpler: check count in joined vs expected
            if joined.count(word) > 1:
                result.append(word)

        return result


class SolutionSorted:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        Sort by length - shorter words can only be substrings of longer ones.
        """
        sorted_words = sorted(words, key=len)
        result = []

        for i, word in enumerate(sorted_words):
            # Only check against longer words
            for j in range(i + 1, len(sorted_words)):
                if word in sorted_words[j]:
                    result.append(word)
                    break

        return result
