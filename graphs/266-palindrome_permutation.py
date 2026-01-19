#266. Palindrome Permutation
#Easy
#
#Given a string s, return true if a permutation of the string could form a
#palindrome and false otherwise.
#
#Example 1:
#Input: s = "code"
#Output: false
#
#Example 2:
#Input: s = "aab"
#Output: true
#
#Example 3:
#Input: s = "carerac"
#Output: true
#
#Constraints:
#    1 <= s.length <= 5000
#    s consists of only lowercase English letters.

from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        A string can form a palindrome if at most one character has odd count.
        """
        counts = Counter(s)
        odd_count = sum(1 for count in counts.values() if count % 2 == 1)
        return odd_count <= 1


class SolutionSet:
    """Using set to track odd occurrences"""

    def canPermutePalindrome(self, s: str) -> bool:
        odd_chars = set()

        for char in s:
            if char in odd_chars:
                odd_chars.remove(char)
            else:
                odd_chars.add(char)

        return len(odd_chars) <= 1


class SolutionBitMask:
    """Using bit manipulation for lowercase letters"""

    def canPermutePalindrome(self, s: str) -> bool:
        bitmask = 0

        for char in s:
            bit_position = ord(char) - ord('a')
            bitmask ^= (1 << bit_position)

        # Check if at most one bit is set
        # n & (n-1) clears the lowest set bit
        return bitmask & (bitmask - 1) == 0


class SolutionArray:
    """Using array for character counts"""

    def canPermutePalindrome(self, s: str) -> bool:
        counts = [0] * 26

        for char in s:
            counts[ord(char) - ord('a')] += 1

        odd_count = sum(1 for count in counts if count % 2 == 1)
        return odd_count <= 1
