#127. Word Ladder
#Hard
#
#A transformation sequence from word beginWord to word endWord using a dictionary wordList
#is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#    Every adjacent pair of words differs by a single letter.
#    Every si for 1 <= i <= k is in wordList.
#    sk == endWord
#
#Given two words, beginWord and endWord, and a dictionary wordList, return the number of
#words in the shortest transformation sequence from beginWord to endWord, or 0 if no such
#sequence exists.
#
#Example 1:
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#Output: 5
#Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog".
#
#Example 2:
#Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#Output: 0
#
#Constraints:
#    1 <= beginWord.length <= 10
#    endWord.length == beginWord.length
#    1 <= wordList.length <= 5000
#    wordList[i].length == beginWord.length
#    beginWord, endWord, and wordList[i] consist of lowercase English letters.
#    beginWord != endWord
#    All the words in wordList are unique.

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i + 1:]
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

        return 0
