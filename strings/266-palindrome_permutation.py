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
        # A string can form a palindrome if at most one character has odd count
        count = Counter(s)
        odd_count = sum(1 for freq in count.values() if freq % 2 == 1)
        return odd_count <= 1

    # Using set (toggle approach)
    def canPermutePalindromeSet(self, s: str) -> bool:
        chars = set()
        for char in s:
            if char in chars:
                chars.remove(char)
            else:
                chars.add(char)
        return len(chars) <= 1

    # Bit manipulation approach
    def canPermutePalindromeBit(self, s: str) -> bool:
        # Use a 26-bit integer to track odd/even counts
        bit_vector = 0
        for char in s:
            bit_vector ^= (1 << (ord(char) - ord('a')))

        # Check if at most one bit is set
        # n & (n-1) removes the lowest set bit
        return bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0
