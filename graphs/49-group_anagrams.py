#49. Group Anagrams
#Medium
#
#Given an array of strings strs, group the anagrams together. You can return the
#answer in any order.
#
#An anagram is a word or phrase formed by rearranging the letters of a different
#word or phrase, typically using all the original letters exactly once.
#
#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
#Example 2:
#Input: strs = [""]
#Output: [[""]]
#
#Example 3:
#Input: strs = ["a"]
#Output: [["a"]]
#
#Constraints:
#    1 <= strs.length <= 10^4
#    0 <= strs[i].length <= 100
#    strs[i] consists of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use sorted string as key.
        """
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())


class SolutionCharCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use character count tuple as key - O(n*k) where k is max string length.
        """
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())


class SolutionPrimeProduct:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use prime number product as key.
        Each letter maps to a prime, anagrams have same product.
        Note: May overflow for very long strings.
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        groups = defaultdict(list)

        for s in strs:
            product = 1
            for char in s:
                product *= primes[ord(char) - ord('a')]

            groups[product].append(s)

        return list(groups.values())


class SolutionCounter:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Using frozenset of Counter items as key.
        """
        from collections import Counter

        groups = defaultdict(list)

        for s in strs:
            key = frozenset(Counter(s).items())
            groups[key].append(s)

        return list(groups.values())
