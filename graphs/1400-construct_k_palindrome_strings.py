#1400. Construct K Palindrome Strings
#Medium
#
#Given a string s and an integer k, return true if you can use all the characters
#in s to construct k palindrome strings or false otherwise.
#
#Example 1:
#Input: s = "annabelle", k = 2
#Output: true
#Explanation: You can construct two palindromes using all characters in s.
#Some possible constructions "anna" + "elble", "## anbna" + "elle", "anellena" + "b"
#
#Example 2:
#Input: s = "leetcode", k = 3
#Output: false
#Explanation: It is impossible to construct 3 palindromes using all the characters of s.
#
#Example 3:
#Input: s = "true", k = 4
#Output: true
#Explanation: The only possible solution is to put each character in a separate string.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of lowercase English letters.
#    1 <= k <= 10^5

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        Key insight: Each palindrome can have at most one character with
        odd frequency (the middle character).

        So we need at least `odd_count` palindromes.
        Also we need at most len(s) palindromes (one char each).

        Answer: odd_count <= k <= len(s)
        """
        n = len(s)

        # Can't make k palindromes from fewer than k characters
        if k > n:
            return False

        # Count characters with odd frequency
        freq = Counter(s)
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)

        # Need at least odd_count palindromes to place all odd-frequency chars
        return odd_count <= k


class SolutionExplicit:
    def canConstruct(self, s: str, k: int) -> bool:
        """More explicit explanation"""
        n = len(s)

        # Base case: can't create more palindromes than characters
        if k > n:
            return False

        # Count frequency of each character
        freq = Counter(s)

        # Count how many characters have odd frequency
        # Each such character must be the center of some palindrome
        odd_count = 0
        for count in freq.values():
            if count % 2 == 1:
                odd_count += 1

        # We need at least odd_count palindromes
        # We can have at most n palindromes (each char alone)
        # So valid if: odd_count <= k <= n
        return odd_count <= k


class SolutionBitwise:
    def canConstruct(self, s: str, k: int) -> bool:
        """Using XOR to count odd frequencies"""
        if k > len(s):
            return False

        # Use bitmask to track parity of each letter
        mask = 0
        for c in s:
            mask ^= (1 << (ord(c) - ord('a')))

        # Count set bits = count of odd frequency letters
        odd_count = bin(mask).count('1')

        return odd_count <= k
