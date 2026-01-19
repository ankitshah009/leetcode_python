#318. Maximum Product of Word Lengths
#Medium
#
#Given a string array words, return the maximum value of
#length(word[i]) * length(word[j]) where the two words do not share common
#letters. If no such two words exist, return 0.
#
#Example 1:
#Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
#Output: 16
#Explanation: The two words can be "abcw", "xtfn".
#
#Example 2:
#Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
#Output: 4
#Explanation: The two words can be "ab", "cd".
#
#Example 3:
#Input: words = ["a","aa","aaa","aaaa"]
#Output: 0
#Explanation: No such pair exists.
#
#Constraints:
#    2 <= words.length <= 1000
#    1 <= words[i].length <= 1000
#    words[i] consists only of lowercase English letters.

from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """Use bitmask to represent character set"""
        n = len(words)

        # Convert each word to bitmask
        masks = []
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks.append(mask)

        max_product = 0

        for i in range(n):
            for j in range(i + 1, n):
                # No common letters if AND is 0
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product


class SolutionOptimized:
    """Optimized with hash map for same masks"""

    def maxProduct(self, words: List[str]) -> int:
        # For same mask, keep only the longest word
        mask_to_len = {}

        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))

            # Keep maximum length for each mask
            mask_to_len[mask] = max(mask_to_len.get(mask, 0), len(word))

        max_product = 0
        masks = list(mask_to_len.keys())

        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, mask_to_len[masks[i]] * mask_to_len[masks[j]])

        return max_product


class SolutionSet:
    """Using set for character comparison"""

    def maxProduct(self, words: List[str]) -> int:
        char_sets = [set(word) for word in words]
        max_product = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if char_sets[i].isdisjoint(char_sets[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product
