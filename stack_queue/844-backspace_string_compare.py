#844. Backspace String Compare
#Easy
#
#Given two strings s and t, return true if they are equal when both are typed into empty text
#editors. '#' means a backspace character.
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

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)

        return build_string(s) == build_string(t)

    def backspaceCompare_o1_space(self, s: str, t: str) -> bool:
        # O(1) space solution using two pointers
        def get_next_valid_char_index(string, index):
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
            i = get_next_valid_char_index(s, i)
            j = get_next_valid_char_index(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True
