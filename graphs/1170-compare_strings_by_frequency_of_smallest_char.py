#1170. Compare Strings by Frequency of the Smallest Character
#Medium
#
#Let the function f(s) be the frequency of the lexicographically smallest
#character in a non-empty string s. For example, if s = "dcce" then f(s) = 2
#because the lexicographically smallest character is 'c', which has a frequency of 2.
#
#You are given an array of strings words and another array of query strings queries.
#For each query queries[i], count the number of words in words such that
#f(queries[i]) < f(W) for each W in words.
#
#Return an integer array answer, where each answer[i] is the answer to the ith query.
#
#Example 1:
#Input: queries = ["cbd"], words = ["zaaaz"]
#Output: [1]
#Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
#
#Example 2:
#Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
#Output: [1,2]
#Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both
#f("cc") < f("aaa") and f("cc") < f("aaaa").
#
#Constraints:
#    1 <= queries.length <= 2000
#    1 <= words.length <= 2000
#    1 <= queries[i].length, words[i].length <= 10
#    queries[i][j], words[i][j] consist of lowercase English letters.

from typing import List
import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        """
        Compute f for all words, sort, use binary search for each query.
        """
        def f(s):
            min_char = min(s)
            return s.count(min_char)

        # Compute f values for words and sort
        word_freqs = sorted(f(w) for w in words)
        n = len(words)

        result = []
        for q in queries:
            query_freq = f(q)
            # Find first word with f(word) > query_freq
            # Count of words with f(word) > query_freq
            idx = bisect.bisect_right(word_freqs, query_freq)
            result.append(n - idx)

        return result


class SolutionCounting:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        """
        Use counting array since f(s) <= 10 (max string length).
        """
        def f(s):
            min_char = min(s)
            return s.count(min_char)

        # Count words by frequency
        # freq_count[i] = number of words with f(word) == i
        freq_count = [0] * 12
        for w in words:
            freq_count[f(w)] += 1

        # Build suffix sum: suffix[i] = count of words with f(word) > i
        suffix = [0] * 12
        for i in range(10, -1, -1):
            suffix[i] = suffix[i + 1] + freq_count[i + 1] if i < 11 else 0

        # Correct suffix calculation
        suffix = [0] * 12
        count = 0
        for i in range(11, -1, -1):
            suffix[i] = count
            count += freq_count[i]

        return [suffix[f(q)] for q in queries]


class SolutionSimple:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        """Simple but less efficient approach"""
        def f(s):
            min_char = min(s)
            return s.count(min_char)

        word_freqs = [f(w) for w in words]

        result = []
        for q in queries:
            query_freq = f(q)
            count = sum(1 for wf in word_freqs if query_freq < wf)
            result.append(count)

        return result
