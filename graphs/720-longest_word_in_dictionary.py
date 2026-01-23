#720. Longest Word in Dictionary
#Medium
#
#Given an array of strings words representing an English Dictionary, return
#the longest word in words that can be built one character at a time by other
#words in words.
#
#If there is more than one possible answer, return the longest word with the
#smallest lexicographical order. If there is no answer, return an empty string.
#
#Note that the word should be built from left to right with each additional
#character being added to the end of a previous word.
#
#Example 1:
#Input: words = ["w","wo","wor","worl","world"]
#Output: "world"
#Explanation: The word "world" can be built one character at a time by "w",
#"wo", "wor", and "worl".
#
#Example 2:
#Input: words = ["a","banana","app","appl","ap","apply","apple"]
#Output: "apple"
#Explanation: Both "apply" and "apple" can be built from other words in the
#dictionary. However, "apple" is lexicographically smaller than "apply".
#
#Constraints:
#    1 <= words.length <= 1000
#    1 <= words[i].length <= 30
#    words[i] consists of lowercase English letters.

class Solution:
    def longestWord(self, words: list[str]) -> str:
        """
        Sort words and check if each word can be built from previous words.
        """
        words.sort()  # Shorter words and lexicographically smaller first
        word_set = {""}  # Empty string as base
        result = ""

        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(result):
                    result = word

        return result


class SolutionTrie:
    """Trie-based solution"""

    def longestWord(self, words: list[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.is_word = False

        root = TrieNode()

        # Build trie
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True

        # DFS to find longest word
        result = ""

        def dfs(node, path):
            nonlocal result

            if len(path) > len(result) or (len(path) == len(result) and path < result):
                result = path

            for c in sorted(node.children.keys()):
                child = node.children[c]
                if child.is_word:
                    dfs(child, path + c)

        dfs(root, "")
        return result


class SolutionBFS:
    """BFS level by level"""

    def longestWord(self, words: list[str]) -> str:
        from collections import deque

        word_set = set(words)
        result = ""

        # Start with single characters
        queue = deque([w for w in words if len(w) == 1])

        while queue:
            word = queue.popleft()

            if len(word) > len(result) or (len(word) == len(result) and word < result):
                result = word

            # Try extending by one character
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word + c
                if new_word in word_set:
                    queue.append(new_word)
                    word_set.remove(new_word)  # Avoid revisiting

        return result
