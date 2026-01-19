#344. Reverse String
#Easy
#
#Write a function that reverses a string. The input string is given as an array
#of characters s.
#
#You must do this by modifying the input array in-place with O(1) extra memory.
#
#Example 1:
#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
#
#Example 2:
#Input: s = ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]
#
#Constraints:
#    1 <= s.length <= 10^5
#    s[i] is a printable ascii character.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Two pointers approach"""
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class SolutionRecursive:
    """Recursive approach"""

    def reverseString(self, s: List[str]) -> None:
        def reverse(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)


class SolutionSlice:
    """Using Python slice (technically O(n) space)"""

    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


class SolutionHalfLoop:
    """Loop through half"""

    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
