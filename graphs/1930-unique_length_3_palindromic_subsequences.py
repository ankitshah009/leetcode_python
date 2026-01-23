#1930. Unique Length-3 Palindromic Subsequences
#Medium
#
#Given a string s, return the number of unique palindromes of length three that
#are a subsequence of s.
#
#Note that even if there are multiple ways to obtain the same subsequence, it
#is still only counted once.
#
#A palindrome is a string that reads the same forwards and backwards.
#
#A subsequence of a string is a new string generated from the original string
#with some characters (can be none) deleted without changing the relative order
#of the remaining characters.
#
#Example 1:
#Input: s = "aabca"
#Output: 3
#
#Example 2:
#Input: s = "adc"
#Output: 0
#
#Example 3:
#Input: s = "bbcbaba"
#Output: 4
#
#Constraints:
#    3 <= s.length <= 10^5
#    s consists of only lowercase English letters.

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        For each letter, find first and last occurrence.
        Count unique letters between them.
        """
        count = 0

        for c in set(s):
            first = s.find(c)
            last = s.rfind(c)

            if last > first + 1:
                # Count unique characters between first and last
                unique = len(set(s[first + 1:last]))
                count += unique

        return count


class SolutionPrecompute:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Precompute first and last indices.
        """
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        count = 0

        for c in first:
            if last[c] > first[c] + 1:
                between = set(s[first[c] + 1:last[c]])
                count += len(between)

        return count


class SolutionOptimized:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Using prefix arrays for each character.
        """
        n = len(s)

        # First and last occurrence of each character
        first = [-1] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        count = 0

        for c in range(26):
            if first[c] != -1 and last[c] > first[c] + 1:
                # Count unique chars between first[c] and last[c]
                unique = set(s[first[c] + 1:last[c]])
                count += len(unique)

        return count
