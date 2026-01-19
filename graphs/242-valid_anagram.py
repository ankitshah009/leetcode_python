#242. Valid Anagram
#Easy
#
#Given two strings s and t, return true if t is an anagram of s, and false
#otherwise.
#
#An Anagram is a word or phrase formed by rearranging the letters of a different
#word or phrase, typically using all the original letters exactly once.
#
#Example 1:
#Input: s = "anagram", t = "nagaram"
#Output: true
#
#Example 2:
#Input: s = "rat", t = "car"
#Output: false
#
#Constraints:
#    1 <= s.length, t.length <= 5 * 10^4
#    s and t consist of lowercase English letters.
#
#Follow up: What if the inputs contain Unicode characters? How would you adapt
#your solution to such a case?

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Using Counter"""
        return Counter(s) == Counter(t)


class SolutionSort:
    """Sort both strings and compare"""

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class SolutionArray:
    """Using array for character counts - O(1) extra space for lowercase letters"""

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for char in s:
            counts[ord(char) - ord('a')] += 1

        for char in t:
            counts[ord(char) - ord('a')] -= 1

        return all(count == 0 for count in counts)


class SolutionDict:
    """Manual dictionary approach"""

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False

        return True


class SolutionUnicode:
    """For Unicode characters - Counter handles this well"""

    def isAnagram(self, s: str, t: str) -> bool:
        # Counter works with any hashable characters including Unicode
        return Counter(s) == Counter(t)
