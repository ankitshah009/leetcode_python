#438. Find All Anagrams in a String
#Medium
#
#Given two strings s and p, return an array of all the start indices of p's
#anagrams in s. You may return the answer in any order.
#
#An Anagram is a word or phrase formed by rearranging the letters of a
#different word or phrase, typically using all the original letters exactly
#once.
#
#Example 1:
#Input: s = "cbaebabacd", p = "abc"
#Output: [0,6]
#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#Example 2:
#Input: s = "abab", p = "ab"
#Output: [0,1,2]
#Explanation:
#The substring with start index = 0 is "ab", which is an anagram of "ab".
#The substring with start index = 1 is "ba", which is an anagram of "ab".
#The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#Constraints:
#    1 <= s.length, p.length <= 3 * 10^4
#    s and p consist of lowercase English letters.

from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Sliding window with character count comparison"""
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter(s[:len(p)])
        result = []

        if window_count == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            # Add new character
            window_count[s[i]] += 1

            # Remove old character
            old_char = s[i - len(p)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            if window_count == p_count:
                result.append(i - len(p) + 1)

        return result


class SolutionMatches:
    """Track number of matching characters"""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        result = []
        matches = 0

        for i in range(len(s)):
            # Add character to window
            if s[i] in p_count:
                p_count[s[i]] -= 1
                if p_count[s[i]] == 0:
                    matches += 1

            # Remove character from window
            if i >= len(p):
                old_char = s[i - len(p)]
                if old_char in p_count:
                    if p_count[old_char] == 0:
                        matches -= 1
                    p_count[old_char] += 1

            if matches == len(p_count):
                result.append(i - len(p) + 1)

        return result


class SolutionArray:
    """Using array instead of Counter"""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        for c in p:
            p_count[ord(c) - ord('a')] += 1

        result = []

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_count == p_count:
                result.append(i - len(p) + 1)

        return result
