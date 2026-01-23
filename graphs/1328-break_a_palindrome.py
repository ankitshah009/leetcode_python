#1328. Break a Palindrome
#Medium
#
#Given a palindromic string of lowercase English letters palindrome, replace
#exactly one character with any lowercase English letter so that the resulting
#string is not a palindrome and that it is the lexicographically smallest one
#possible.
#
#Return the resulting string. If there is no way to replace a character to make
#it not a palindrome, return an empty string.
#
#A string a is lexicographically smaller than a string b (of the same length)
#if in the first position where a and b differ, a has a character strictly
#smaller than the corresponding character in b.
#
#Example 1:
#Input: palindrome = "abccba"
#Output: "aaccba"
#Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
#Of all the ways, "aaccba" is the lexicographically smallest.
#
#Example 2:
#Input: palindrome = "a"
#Output: ""
#Explanation: There is no way to replace a single character to make "a" not a palindrome.
#
#Constraints:
#    1 <= palindrome.length <= 1000
#    palindrome consists of only lowercase English letters.

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        To get lexicographically smallest:
        1. Find first non-'a' in first half, change it to 'a'
        2. If all 'a's in first half (or single char), change last char to 'b'
        """
        n = len(palindrome)

        # Single character can't be made non-palindrome
        if n == 1:
            return ""

        s = list(palindrome)

        # Check first half (don't include middle for odd length)
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)

        # All characters in first half are 'a'
        # Change last character to 'b'
        s[-1] = 'b'
        return ''.join(s)


class SolutionVerbose:
    def breakPalindrome(self, palindrome: str) -> str:
        """More explicit solution"""
        n = len(palindrome)

        if n == 1:
            return ""

        # Strategy: Make lexicographically smallest by changing leftmost char
        # to something smaller, or if not possible, rightmost to something larger

        s = list(palindrome)

        # Try to change a character in the first half to 'a'
        # (skip middle char in odd-length palindrome as it doesn't matter)
        first_half_end = n // 2

        for i in range(first_half_end):
            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)

        # If first half is all 'a's, change last char to 'b'
        # This makes it lexicographically larger but still smallest possible
        s[-1] = 'b'
        return ''.join(s)
