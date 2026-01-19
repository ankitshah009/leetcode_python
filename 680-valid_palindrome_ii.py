#680. Valid Palindrome II
#Easy
#
#Given a string s, return true if the s can be palindrome after deleting at most one character
#from it.
#
#Example 1:
#Input: s = "aba"
#Output: true
#
#Example 2:
#Input: s = "abca"
#Output: true
#Explanation: You could delete the character 'c'.
#
#Example 3:
#Input: s = "abc"
#Output: false
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of lowercase English letters.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try skipping either left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1

        return True
