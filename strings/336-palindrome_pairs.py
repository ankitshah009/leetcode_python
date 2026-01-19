#336. Palindrome Pairs
#Hard
#
#You are given a 0-indexed array of unique strings words.
#
#A palindrome pair is a pair of integers (i, j) such that:
#    0 <= i, j < words.length,
#    i != j, and
#    words[i] + words[j] (the concatenation of the two strings) is a palindrome.
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

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        word_to_idx = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: prefix is palindrome, check if reversed suffix exists
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_idx and word_to_idx[reversed_suffix] != i:
                        result.append([word_to_idx[reversed_suffix], i])

                # Case 2: suffix is palindrome, check if reversed prefix exists
                # j > 0 to avoid duplicates with Case 1 when j = 0
                if j > 0 and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_idx and word_to_idx[reversed_prefix] != i:
                        result.append([i, word_to_idx[reversed_prefix]])

        return result


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_idx = -1
        self.palindrome_suffixes = []  # Indices of words with palindrome suffix


class SolutionTrie:
    """Trie-based solution"""

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        # Build trie with reversed words
        root = TrieNode()

        for i, word in enumerate(words):
            node = root
            reversed_word = word[::-1]

            for j, char in enumerate(reversed_word):
                # If remaining suffix is palindrome, store word index
                if is_palindrome(reversed_word[j:]):
                    node.palindrome_suffixes.append(i)

                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.word_idx = i

        result = []

        for i, word in enumerate(words):
            node = root

            for j, char in enumerate(word):
                # Current word is longer, check if remaining is palindrome
                if node.word_idx >= 0 and node.word_idx != i and is_palindrome(word[j:]):
                    result.append([i, node.word_idx])

                if char not in node.children:
                    break
                node = node.children[char]
            else:
                # Reached end of word
                if node.word_idx >= 0 and node.word_idx != i:
                    result.append([i, node.word_idx])

                # Check words that have palindrome suffix
                for idx in node.palindrome_suffixes:
                    if idx != i:
                        result.append([i, idx])

        return result
