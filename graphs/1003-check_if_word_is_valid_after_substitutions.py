#1003. Check If Word Is Valid After Substitutions
#Medium
#
#Given a string s, determine if it is valid.
#
#A string s is valid if, starting with an empty string t = "", you can transform
#t into s after performing the following operation any number of times:
#- Insert string "abc" into any position in t.
#
#Return true if s is a valid string, otherwise, return false.
#
#Example 1:
#Input: s = "aabcbc"
#Output: true
#Explanation: "" -> "abc" -> "aabcbc"
#
#Example 2:
#Input: s = "abcabcababcc"
#Output: true
#
#Example 3:
#Input: s = "abccba"
#Output: false
#
#Constraints:
#    1 <= s.length <= 2 * 10^4
#    s consists of letters 'a', 'b', and 'c'.

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack: remove "abc" patterns.
        """
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()

        return len(stack) == 0


class SolutionReplace:
    """Replace until empty"""

    def isValid(self, s: str) -> bool:
        while 'abc' in s:
            s = s.replace('abc', '')
        return s == ''


class SolutionOptimized:
    """Optimized stack check"""

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == 'c':
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
