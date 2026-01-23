#1910. Remove All Occurrences of a Substring
#Medium
#
#Given two strings s and part, perform the following operation on s until all
#occurrences of the substring part are removed:
#- Find the leftmost occurrence of the substring part and remove it from s.
#
#Return s after removing all occurrences of part.
#
#A substring is a contiguous sequence of characters in a string.
#
#Example 1:
#Input: s = "daabcbaabcbc", part = "abc"
#Output: "dab"
#
#Example 2:
#Input: s = "axxxxyyyyb", part = "xy"
#Output: "ab"
#
#Constraints:
#    1 <= s.length <= 1000
#    1 <= part.length <= 1000
#    s and part consists of lowercase English letters.

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Repeatedly remove leftmost occurrence.
        """
        while part in s:
            s = s.replace(part, '', 1)
        return s


class SolutionStack:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Use stack to check suffix after each character.
        """
        stack = []
        part_len = len(part)

        for c in s:
            stack.append(c)

            # Check if stack ends with part
            if len(stack) >= part_len:
                if ''.join(stack[-part_len:]) == part:
                    # Remove part from stack
                    for _ in range(part_len):
                        stack.pop()

        return ''.join(stack)


class SolutionFind:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Using find method.
        """
        idx = s.find(part)
        while idx != -1:
            s = s[:idx] + s[idx + len(part):]
            idx = s.find(part)
        return s
