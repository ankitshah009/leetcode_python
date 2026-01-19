#126. Word Ladder II
#Hard
#
#A transformation sequence from word beginWord to word endWord using a dictionary
#wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#    Every adjacent pair of words differs by a single letter.
#    Every si for 1 <= i <= k is in wordList.
#    sk == endWord
#
#Given two words, beginWord and endWord, and a dictionary wordList, return all
#the shortest transformation sequences from beginWord to endWord.
#
#Example 1:
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
#
#Example 2:
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#Output: []
#Explanation: The endWord "cog" is not in wordList.

from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # BFS to find shortest path length and build graph
        # Track parents for path reconstruction
        parents = defaultdict(set)

        # BFS layer by layer
        current_level = {beginWord}
        visited = {beginWord}
        found = False

        while current_level and not found:
            # Mark all words in current level as visited
            visited.update(current_level)
            next_level = set()

            for word in current_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word == endWord:
                            found = True
                            parents[endWord].add(word)
                        elif new_word in word_set and new_word not in visited:
                            next_level.add(new_word)
                            parents[new_word].add(word)

            current_level = next_level

        # Backtrack to build all paths
        def backtrack(word):
            if word == beginWord:
                return [[beginWord]]

            paths = []
            for parent in parents[word]:
                for path in backtrack(parent):
                    paths.append(path + [word])
            return paths

        return backtrack(endWord) if found else []


class SolutionBidirectional:
    """Bidirectional BFS for better performance"""

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # Forward and backward sets
        front = {beginWord}
        back = {endWord}

        # Direction: True = forward, False = backward
        direction = True
        parents = defaultdict(set)

        while front and back:
            # Always expand smaller set
            if len(front) > len(back):
                front, back = back, front
                direction = not direction

            word_set -= front
            next_front = set()

            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in word_set or new_word in back:
                            if new_word in back:
                                # Found connection
                                if direction:
                                    parents[new_word].add(word)
                                else:
                                    parents[word].add(new_word)

                            if new_word in word_set:
                                next_front.add(new_word)
                                if direction:
                                    parents[new_word].add(word)
                                else:
                                    parents[word].add(new_word)

            if front & back:
                break

            front = next_front

        # Build paths
        def build_paths(word):
            if word == beginWord:
                return [[beginWord]]
            return [path + [word] for parent in parents[word] for path in build_paths(parent)]

        return build_paths(endWord)
