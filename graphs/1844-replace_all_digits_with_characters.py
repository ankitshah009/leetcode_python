#1844. Replace All Digits with Characters
#Easy
#
#You are given a 0-indexed string s that has lowercase English letters in its
#even indices and digits in its odd indices.
#
#There is a function shift(c, x), where c is a character and x is a digit, that
#returns the xth character after c.
#
#For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
#
#For every odd index i, you want to replace the digit s[i] with
#shift(s[i-1], s[i]).
#
#Return s after replacing all digits. It is guaranteed that
#shift(s[i-1], s[i]) will never exceed 'z'.
#
#Example 1:
#Input: s = "a1c1e1"
#Output: "abcdef"
#
#Example 2:
#Input: s = "a1b2c3d4e"
#Output: "abbdceli"
#
#Constraints:
#    1 <= s.length <= 100
#    s consists only of lowercase English letters and digits.
#    shift(s[i-1], s[i]) <= 'z' for all odd indices i.

class Solution:
    def replaceDigits(self, s: str) -> str:
        """
        Replace each digit with shifted character.
        """
        result = list(s)

        for i in range(1, len(s), 2):
            result[i] = chr(ord(s[i - 1]) + int(s[i]))

        return ''.join(result)


class SolutionList:
    def replaceDigits(self, s: str) -> str:
        """
        Build result list.
        """
        result = []

        for i, c in enumerate(s):
            if i % 2 == 0:
                result.append(c)
            else:
                result.append(chr(ord(s[i - 1]) + int(c)))

        return ''.join(result)


class SolutionComprehension:
    def replaceDigits(self, s: str) -> str:
        """
        Using list comprehension.
        """
        return ''.join(
            s[i] if i % 2 == 0 else chr(ord(s[i - 1]) + int(s[i]))
            for i in range(len(s))
        )
