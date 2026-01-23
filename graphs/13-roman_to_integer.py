#13. Roman to Integer
#Easy
#
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D, M.
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#
#I can be placed before V (5) and X (10) to make 4 and 9.
#X can be placed before L (50) and C (100) to make 40 and 90.
#C can be placed before D (500) and M (1000) to make 400 and 900.
#
#Given a roman numeral, convert it to an integer.
#
#Example 1:
#Input: s = "III"
#Output: 3
#
#Example 2:
#Input: s = "LVIII"
#Output: 58
#
#Example 3:
#Input: s = "MCMXCIV"
#Output: 1994
#
#Constraints:
#    1 <= s.length <= 15
#    s contains only characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#    It is guaranteed that s is a valid roman numeral in range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Scan from right to left, subtract if smaller value precedes larger.
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        prev = 0

        for char in reversed(s):
            curr = values[char]
            if curr < prev:
                result -= curr
            else:
                result += curr
            prev = curr

        return result


class SolutionLeftToRight:
    def romanToInt(self, s: str) -> int:
        """
        Scan left to right, check if next value is larger.
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]

        return result


class SolutionReplace:
    def romanToInt(self, s: str) -> int:
        """
        Replace subtractive combinations first, then sum.
        """
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Replace subtractive notations
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        return sum(values[char] for char in s)
