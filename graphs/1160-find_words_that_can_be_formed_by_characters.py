#1160. Find Words That Can Be Formed by Characters
#Easy
#
#You are given an array of strings words and a string chars.
#
#A string is good if it can be formed by characters from chars (each character
#can only be used once).
#
#Return the sum of lengths of all good strings in words.
#
#Example 1:
#Input: words = ["cat","bt","hat","tree"], chars = "atach"
#Output: 6
#Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
#
#Example 2:
#Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
#Output: 10
#Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#Constraints:
#    1 <= words.length <= 1000
#    1 <= words[i].length, chars.length <= 100
#    words[i] and chars consist of lowercase English letters.

from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """Count chars available and check each word"""
        available = Counter(chars)
        result = 0

        for word in words:
            word_count = Counter(word)
            # Check if word can be formed
            if all(word_count[c] <= available[c] for c in word_count):
                result += len(word)

        return result


class SolutionExplicit:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """More explicit checking"""
        char_count = [0] * 26
        for c in chars:
            char_count[ord(c) - ord('a')] += 1

        result = 0

        for word in words:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c) - ord('a')] += 1

            # Check if valid
            valid = True
            for i in range(26):
                if word_count[i] > char_count[i]:
                    valid = False
                    break

            if valid:
                result += len(word)

        return result
