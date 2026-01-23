#916. Word Subsets
#Medium
#
#You are given two string arrays words1 and words2.
#
#A string b is a subset of string a if every letter in b occurs in a including
#multiplicity.
#
#A string a from words1 is universal if for every string b in words2, b is a
#subset of a.
#
#Return an array of all the universal strings in words1. You may return the
#answer in any order.
#
#Example 1:
#Input: words1 = ["amazon","apple","facebook","google","leetcode"],
#       words2 = ["e","o"]
#Output: ["facebook","google","leetcode"]
#
#Example 2:
#Input: words1 = ["amazon","apple","facebook","google","leetcode"],
#       words2 = ["l","e"]
#Output: ["apple","google","leetcode"]
#
#Constraints:
#    1 <= words1.length, words2.length <= 10^4
#    1 <= words1[i].length, words2[i].length <= 10
#    words1[i] and words2[i] consist only of lowercase English letters.
#    All the strings of words1 are unique.

from collections import Counter

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        """
        Combine all words2 requirements into single max-count requirement.
        """
        # Find max count needed for each character across all words2
        max_count = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, cnt in word_count.items():
                max_count[char] = max(max_count[char], cnt)

        # Check each word in words1
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= cnt for char, cnt in max_count.items()):
                result.append(word)

        return result


class SolutionExplicit:
    """Using explicit array counts"""

    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        def count(word: str) -> list[int]:
            cnt = [0] * 26
            for c in word:
                cnt[ord(c) - ord('a')] += 1
            return cnt

        # Max requirement from words2
        max_req = [0] * 26
        for word in words2:
            cnt = count(word)
            for i in range(26):
                max_req[i] = max(max_req[i], cnt[i])

        result = []
        for word in words1:
            cnt = count(word)
            if all(cnt[i] >= max_req[i] for i in range(26)):
                result.append(word)

        return result
