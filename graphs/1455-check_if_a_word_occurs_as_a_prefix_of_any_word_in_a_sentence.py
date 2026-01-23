#1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
#Easy
#
#Given a sentence that consists of some words separated by a single space, and
#a searchWord, check if searchWord is a prefix of any word in sentence.
#
#Return the index of the word in sentence (1-indexed) where searchWord is a
#prefix of this word. If searchWord is a prefix of more than one word, return
#the index of the first word (minimum index). If there is no such word return -1.
#
#A prefix of a string s is any leading contiguous substring of s.
#
#Example 1:
#Input: sentence = "i love eating burger", searchWord = "burg"
#Output: 4
#Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
#
#Example 2:
#Input: sentence = "this problem is an easy problem", searchWord = "pro"
#Output: 2
#Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in
#the sentence, but we return 2 as it's the minimal index.
#
#Example 3:
#Input: sentence = "i am tired", searchWord = "you"
#Output: -1
#Explanation: "you" is not a prefix of any word in the sentence.
#
#Constraints:
#    1 <= sentence.length <= 100
#    1 <= searchWord.length <= 10
#    sentence consists of lowercase English letters and spaces.
#    searchWord consists of lowercase English letters.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Split sentence into words and check each word.
        """
        words = sentence.split()

        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1  # 1-indexed

        return -1


class SolutionManual:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """Check prefix manually"""
        words = sentence.split()

        for i, word in enumerate(words):
            if len(word) >= len(searchWord):
                if word[:len(searchWord)] == searchWord:
                    return i + 1

        return -1


class SolutionFind:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """Using find to locate search word"""
        words = sentence.split()

        for i, word in enumerate(words):
            if word.find(searchWord) == 0:  # Found at position 0 = prefix
                return i + 1

        return -1
