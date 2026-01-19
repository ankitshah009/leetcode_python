#336. Palindrome Pairs
#Hard
#
#You are given a 0-indexed array of unique strings words.
#
#A palindrome pair is a pair of integers (i, j) such that:
#- 0 <= i, j < words.length,
#- i != j, and
#- words[i] + words[j] (the concatenation of the two strings) is a palindrome.
#
#Return an array of all the palindrome pairs of words.
#
#Example 1:
#Input: words = ["abcd","dcba","lls","s","sssll"]
#Output: [[0,1],[1,0],[3,2],[2,4]]
#Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
#
#Example 2:
#Input: words = ["bat","tab","cat"]
#Output: [[0,1],[1,0]]
#Explanation: The palindromes are ["battab","tabbat"]
#
#Example 3:
#Input: words = ["a",""]
#Output: [[0,1],[1,0]]
#Explanation: The palindromes are ["a","a"]
#
#Constraints:
#    1 <= words.length <= 5000
#    0 <= words[i].length <= 300
#    words[i] consists of lowercase English letters.

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """Hash map approach with prefix/suffix checking"""
        word_to_idx = {word: i for i, word in enumerate(words)}
        result = []

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                # Split word into prefix and suffix
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: prefix is palindrome, check if reversed suffix exists
                # reversed_suffix + word = reversed_suffix + prefix + suffix
                # If prefix is palindrome and reversed_suffix exists, result is palindrome
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_idx and word_to_idx[reversed_suffix] != i:
                        result.append([word_to_idx[reversed_suffix], i])

                # Case 2: suffix is palindrome, check if reversed prefix exists
                # word + reversed_prefix = prefix + suffix + reversed_prefix
                # If suffix is palindrome and reversed_prefix exists, result is palindrome
                if j < n and is_palindrome(suffix):  # j < n to avoid duplicates
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_idx and word_to_idx[reversed_prefix] != i:
                        result.append([i, word_to_idx[reversed_prefix]])

        return result


class SolutionTrie:
    """Trie-based approach"""

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word_idx = -1
                self.palindrome_suffixes = []  # Indices of words where suffix is palindrome

        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Build trie with reversed words
        root = TrieNode()

        for i, word in enumerate(words):
            node = root
            for j in range(len(word) - 1, -1, -1):
                # If suffix is palindrome, record this word index
                if is_palindrome(word, 0, j):
                    node.palindrome_suffixes.append(i)

                c = word[j]
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

            node.palindrome_suffixes.append(i)
            node.word_idx = i

        result = []

        # Search for palindrome pairs
        for i, word in enumerate(words):
            node = root

            for j, c in enumerate(word):
                # Check if remaining suffix is palindrome
                if node.word_idx >= 0 and node.word_idx != i and is_palindrome(word, j, len(word) - 1):
                    result.append([i, node.word_idx])

                if c not in node.children:
                    break
                node = node.children[c]
            else:
                # Reached end of word, check all palindrome suffixes in trie
                for k in node.palindrome_suffixes:
                    if k != i:
                        result.append([i, k])

        return result


class SolutionBruteForce:
    """Brute force O(n^2 * k) - for reference"""

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and is_palindrome(words[i] + words[j]):
                    result.append([i, j])

        return result
