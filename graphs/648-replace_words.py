#648. Replace Words
#Medium
#
#In English, we have a concept called root, which can be followed by some other
#word to form another longer word - let's call this word derivative. For example,
#when the root "help" is followed by the word "ful", we can form a derivative "helpful".
#
#Given a dictionary consisting of many roots and a sentence consisting of words
#separated by spaces, replace all the derivatives in the sentence with the root
#forming it. If a derivative can be replaced by more than one root, replace it
#with the root that has the shortest length.
#
#Return the sentence after the replacement.
#
#Example 1:
#Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
#Output: "the cat was rat by the bat"
#
#Example 2:
#Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfabd"
#Output: "a]a b c"
#
#Constraints:
#    1 <= dictionary.length <= 1000
#    1 <= dictionary[i].length <= 100
#    dictionary[i] consists of only lower-case letters.
#    1 <= sentence.length <= 10^6
#    sentence consists of only lower-case letters and spaces.

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Using Trie for efficient prefix matching"""
        # Build Trie
        trie = {}

        for root in dictionary:
            node = trie
            for c in root:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True  # Mark end of word

        def find_root(word):
            node = trie
            for i, c in enumerate(word):
                if c not in node:
                    return word
                node = node[c]
                if '$' in node:
                    return word[:i + 1]
            return word

        words = sentence.split()
        return ' '.join(find_root(word) for word in words)


class SolutionSet:
    """Using set with prefix checking"""

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)

        def find_root(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    return prefix
            return word

        words = sentence.split()
        return ' '.join(find_root(word) for word in words)


class SolutionSorted:
    """Sort dictionary by length"""

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        roots = set(dictionary)

        def find_root(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word

        words = sentence.split()
        return ' '.join(find_root(word) for word in words)
