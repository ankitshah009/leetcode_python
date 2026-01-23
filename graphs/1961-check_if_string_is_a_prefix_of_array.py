#1961. Check If String Is a Prefix of Array
#Easy
#
#Given a string s and an array of strings words, determine whether s is a prefix
#string of words.
#
#A string s is a prefix string of words if s can be made by concatenating the
#first k strings in words for some positive k no larger than words.length.
#
#Return true if s is a prefix string of words, or false otherwise.
#
#Example 1:
#Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
#Output: true
#Explanation: s can be made by concatenating "i", "love", and "leetcode".
#
#Example 2:
#Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
#Output: false
#
#Constraints:
#    1 <= words.length <= 100
#    1 <= words[i].length <= 20
#    1 <= s.length <= 1000
#    words[i] and s consist of only lowercase English letters.

from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        Concatenate words until we match or exceed s length.
        """
        current = ""

        for word in words:
            current += word

            if current == s:
                return True

            if len(current) > len(s):
                return False

        return False


class SolutionStartsWith:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        Check prefix at each step.
        """
        idx = 0

        for word in words:
            if not s.startswith(word, idx):
                return False

            idx += len(word)

            if idx == len(s):
                return True

        return False


class SolutionOneLoop:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        Build and compare character by character.
        """
        s_idx = 0
        n = len(s)

        for word in words:
            for c in word:
                if s_idx >= n or s[s_idx] != c:
                    return False
                s_idx += 1

            if s_idx == n:
                return True

        return False
