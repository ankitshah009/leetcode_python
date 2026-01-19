#844. Backspace String Compare
#Easy
#
#Given two strings s and t, return true if they are equal when both are typed
#into empty text editors. '#' means a backspace character.
#
#Note that after backspacing an empty text, the text will continue empty.
#
#Example 1:
#Input: s = "ab#c", t = "ad#c"
#Output: true
#Explanation: Both s and t become "ac".
#
#Example 2:
#Input: s = "ab##", t = "c#d#"
#Output: true
#Explanation: Both s and t become "".
#
#Example 3:
#Input: s = "a#c", t = "b"
#Output: false
#Explanation: s becomes "c" while t becomes "b".
#
#Constraints:
#    1 <= s.length, t.length <= 200
#    s and t only contain lowercase letters and '#' characters.
#
#Follow up: Can you solve it in O(n) time and O(1) space?

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """O(1) space using two pointers from the end"""

        def next_valid_char(string, index):
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = next_valid_char(s, i)
            j = next_valid_char(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True


class SolutionStack:
    """Using stack - O(n) time and space"""

    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return build(s) == build(t)


class SolutionGenerator:
    """Using generator for O(1) space"""

    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            skip = 0
            for c in reversed(string):
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield c

        from itertools import zip_longest
        return all(a == b for a, b in zip_longest(process(s), process(t)))
