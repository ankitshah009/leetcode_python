#676. Implement Magic Dictionary
#Medium
#
#Design a data structure that is initialized with a list of different words.
#Provided a string, you should determine if you can change exactly one character
#in this string to match any word in the data structure.
#
#Implement the MagicDictionary class:
#- MagicDictionary() Initializes the object.
#- void buildDict(String[] dictionary) Sets the data structure with an array of
#  distinct strings dictionary.
#- bool search(String searchWord) Returns true if you can change exactly one
#  character in searchWord to match any string in the data structure, otherwise
#  returns false.
#
#Example 1:
#Input: ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
#       [[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
#Output: [null, null, false, true, false, false]
#
#Constraints:
#    1 <= dictionary.length <= 100
#    1 <= dictionary[i].length <= 100
#    dictionary[i] consists of only lower-case English letters.
#    All the strings in dictionary are distinct.
#    1 <= searchWord.length <= 100
#    searchWord consists of only lower-case English letters.
#    buildDict will be called only once before search.
#    At most 100 calls will be made to search.

from typing import List
from collections import defaultdict

class MagicDictionary:
    """
    Store words by length, then compare character by character.
    """

    def __init__(self):
        self.words_by_length = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words_by_length[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)

        for word in self.words_by_length[n]:
            diff = 0
            for c1, c2 in zip(searchWord, word):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True

        return False


class MagicDictionaryTrie:
    """Trie-based solution"""

    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True

    def search(self, searchWord: str) -> bool:
        def dfs(node, i, modified):
            if i == len(searchWord):
                return modified and '$' in node

            c = searchWord[i]

            # Try exact match
            if c in node:
                if dfs(node[c], i + 1, modified):
                    return True

            # Try modification (only if not already modified)
            if not modified:
                for char in node:
                    if char != '$' and char != c:
                        if dfs(node[char], i + 1, True):
                            return True

            return False

        return dfs(self.trie, 0, False)


class MagicDictionaryPattern:
    """Store patterns with wildcards"""

    def __init__(self):
        self.patterns = defaultdict(set)
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)

        for word in dictionary:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                self.patterns[pattern].add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            pattern = searchWord[:i] + '*' + searchWord[i+1:]

            if pattern in self.patterns:
                # Check if there's a different word matching
                for word in self.patterns[pattern]:
                    if word != searchWord:
                        return True

        return False
