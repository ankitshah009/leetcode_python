#820. Short Encoding of Words
#Medium
#
#A valid encoding of an array of words is any reference string s and array of
#indices indices such that:
#- words.length == indices.length
#- The reference string s ends with the '#' character.
#- For each index indices[i], the substring of s starting from indices[i] and
#  up to (but not including) the next '#' character is equal to words[i].
#
#Given an array of words, return the length of the shortest reference string s
#possible of any valid encoding of words.
#
#Example 1:
#Input: words = ["time", "me", "bell"]
#Output: 10
#Explanation: "time#bell#" is the reference string.
#"me" is a suffix of "time", so it's covered.
#
#Example 2:
#Input: words = ["t"]
#Output: 2
#
#Constraints:
#    1 <= words.length <= 2000
#    1 <= words[i].length <= 7
#    words[i] consists of only lowercase letters.

class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        """
        Remove words that are suffixes of other words.
        Use set operations: if word is suffix of another, remove it.
        """
        word_set = set(words)

        for word in words:
            # Remove all proper suffixes
            for i in range(1, len(word)):
                word_set.discard(word[i:])

        # Sum lengths + 1 for each '#'
        return sum(len(word) + 1 for word in word_set)


class SolutionTrie:
    """Trie with reversed words"""

    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Remove duplicates and sort by length (longest first)
        words = list(set(words))

        # Build trie with reversed words
        root = {}

        def insert(word):
            node = root
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True  # Mark end

        for word in words:
            insert(word)

        # Count leaf nodes (words not suffixes of others)
        def count_leaves(node, depth):
            if len(node) == 0 or (len(node) == 1 and '$' in node):
                return depth + 1  # word length + '#'

            total = 0
            for key, child in node.items():
                if key != '$':
                    total += count_leaves(child, depth + 1)
            return total

        return count_leaves(root, 0)


class SolutionSort:
    """Sort by reversed words"""

    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Sort by reversed words
        words = sorted(set(words), key=lambda w: w[::-1])

        total = 0
        for i, word in enumerate(words):
            # If next word doesn't have current as suffix, count it
            if i + 1 == len(words) or not words[i + 1].endswith(word):
                total += len(word) + 1

        return total
