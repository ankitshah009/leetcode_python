#680. Valid Palindrome II
#Easy
#
#Given a string s, return true if the s can be palindrome after deleting at most
#one character from it.
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
        """
        Two pointers: when mismatch found, try skipping either character.
        """
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
                # Try skipping left or right character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1

        return True


class SolutionRecursive:
    """Recursive approach with deletion count"""

    def validPalindrome(self, s: str) -> bool:
        def check(left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    return (check(left + 1, right, True) or
                            check(left, right - 1, True))
                left += 1
                right -= 1
            return True

        return check(0, len(s) - 1, False)


class SolutionSlicing:
    """Using string slicing"""

    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Check both possibilities
                skip_left = s[left + 1:right + 1]
                skip_right = s[left:right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            left += 1
            right -= 1

        return True
