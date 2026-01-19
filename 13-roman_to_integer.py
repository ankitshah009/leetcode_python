#13. Roman to Integer
#Easy
#
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#
#Example 1:
#Input: s = "III"
#Output: 3
#Explanation: III = 3.
#
#Example 2:
#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.
#
#Example 3:
#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#Constraints:
#    1 <= s.length <= 15
#    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]

        return result
