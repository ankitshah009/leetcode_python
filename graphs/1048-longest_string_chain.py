#1048. Longest String Chain
#Medium
#
#You are given an array of words where each word consists of lowercase
#English letters.
#
#wordA is a predecessor of wordB if and only if we can insert exactly one
#letter anywhere in wordA without changing the order of the other characters
#to make it equal to wordB.
#
#A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
#where word1 is a predecessor of word2, word2 is a predecessor of word3,
#and so on. A single word is trivially a word chain with k == 1.
#
#Return the length of the longest possible word chain with words chosen
#from the given list of words.
#
#Example 1:
#Input: words = ["a","b","ba","bca","bda","bdca"]
#Output: 4
#Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
#
#Example 2:
#Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
#Output: 5
#Explanation: All words can be part of chain ["xb","xbc","cxbc","pcxbc","pcxbcf"].
#
#Example 3:
#Input: words = ["abcd","dbqca"]
#Output: 1
#Explanation: The trivial chain ["abcd"] is longest. "abcd" -> "dbqca" is not valid.
#
#Constraints:
#    1 <= words.length <= 1000
#    1 <= words[i].length <= 16
#    words[i] only consists of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        DP with hash map. Sort by length, then for each word,
        check all predecessors (remove one char at a time).
        """
        words.sort(key=len)
        dp = {}  # word -> longest chain ending with this word

        result = 1

        for word in words:
            dp[word] = 1

            # Try removing each character
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            result = max(result, dp[word])

        return result


class SolutionByLength:
    def longestStrChain(self, words: List[str]) -> int:
        """Group words by length for efficient lookup"""
        by_length = defaultdict(set)
        for word in words:
            by_length[len(word)].add(word)

        dp = {}
        result = 1

        lengths = sorted(by_length.keys())

        for length in lengths:
            for word in by_length[length]:
                dp[word] = 1

                if length - 1 in by_length:
                    for i in range(length):
                        pred = word[:i] + word[i+1:]
                        if pred in dp:
                            dp[word] = max(dp[word], dp[pred] + 1)

                result = max(result, dp[word])

        return result


class SolutionMemo:
    def longestStrChain(self, words: List[str]) -> int:
        """Memoized DFS"""
        word_set = set(words)
        memo = {}

        def dfs(word):
            if word not in word_set:
                return 0
            if word in memo:
                return memo[word]

            max_chain = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                max_chain = max(max_chain, 1 + dfs(pred))

            memo[word] = max_chain
            return max_chain

        return max(dfs(word) for word in words)
