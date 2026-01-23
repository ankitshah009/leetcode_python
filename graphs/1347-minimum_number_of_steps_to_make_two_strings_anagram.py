#1347. Minimum Number of Steps to Make Two Strings Anagram
#Medium
#
#You are given two strings of the same length s and t. In one step you can
#choose any character of t and replace it with another character.
#
#Return the minimum number of steps to make t an anagram of s.
#
#An Anagram of a string is a string that contains the same characters with a
#different (or the same) ordering.
#
#Example 1:
#Input: s = "bab", t = "aba"
#Output: 1
#Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
#
#Example 2:
#Input: s = "leetcode", t = "practice"
#Output: 5
#Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
#
#Example 3:
#Input: s = "anagram", t = "mangaar"
#Output: 0
#Explanation: "anagram" and "mangaar" are anagrams.
#
#Constraints:
#    1 <= s.length <= 5 * 10^4
#    s.length == t.length
#    s and t consist of lowercase English letters only.

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Count character differences.
        Steps needed = characters in s that are extra compared to t.
        """
        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0
        for char, cnt in count_s.items():
            if cnt > count_t[char]:
                steps += cnt - count_t[char]

        return steps


class SolutionArray:
    def minSteps(self, s: str, t: str) -> int:
        """Using array instead of Counter"""
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            count[ord(c) - ord('a')] -= 1

        # Sum of positive differences = characters to replace
        return sum(c for c in count if c > 0)


class SolutionDiff:
    def minSteps(self, s: str, t: str) -> int:
        """Using Counter subtraction"""
        count_s = Counter(s)
        count_t = Counter(t)

        # Difference shows what's extra in s
        diff = count_s - count_t

        return sum(diff.values())
