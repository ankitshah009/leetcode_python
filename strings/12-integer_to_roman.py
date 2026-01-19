#12. Integer to Roman
#Medium
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
#Input: num = 3
#Output: "III"
#Explanation: 3 is represented as 3 ones.
#
#Example 2:
#Input: num = 58
#Output: "LVIII"
#Explanation: L = 50, V = 5, III = 3.
#
#Example 3:
#Input: num = 1994
#Output: "MCMXCIV"
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#Constraints:
#    1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []
        for i, value in enumerate(values):
            while num >= value:
                num -= value
                result.append(symbols[i])

        return ''.join(result)
