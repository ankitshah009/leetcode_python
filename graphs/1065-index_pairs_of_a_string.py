#1065. Index Pairs of a String
#Easy
#
#Given a string text and an array of strings words, return an array of all
#index pairs [i, j] so that the substring text[i...j] is in words.
#
#Return the pairs [i, j] in sorted order (i.e., sort them by their first
#coordinate, and in case of ties sort them by their second coordinate).
#
#Example 1:
#Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
#Output: [[3,7],[9,13],[10,17]]
#
#Example 2:
#Input: text = "ababa", words = ["aba","ab"]
#Output: [[0,1],[0,2],[2,3],[2,4]]
#Explanation: Note that matches can overlap.
#
#Constraints:
#    1 <= text.length <= 100
#    1 <= words.length <= 20
#    1 <= words[i].length <= 50
#    text and words[i] consist of lowercase English letters.
#    All the strings of words are unique.

from typing import List

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """
        Check each word at each position.
        """
        result = []
        word_set = set(words)

        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i:j+1] in word_set:
                    result.append([i, j])

        return sorted(result)


class SolutionOptimized:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """Check only up to max word length"""
        result = []
        word_set = set(words)
        max_len = max(len(w) for w in words)

        for i in range(len(text)):
            for length in range(1, min(max_len, len(text) - i) + 1):
                if text[i:i+length] in word_set:
                    result.append([i, i + length - 1])

        return sorted(result)


class SolutionTrie:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        """Trie-based approach"""
        # Build trie
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True  # End marker

        result = []
        n = len(text)

        for i in range(n):
            node = trie
            for j in range(i, n):
                if text[j] not in node:
                    break
                node = node[text[j]]
                if '$' in node:
                    result.append([i, j])

        return result
