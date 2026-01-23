#12. Integer to Roman
#Medium
#
#Seven different symbols represent Roman numerals with the following values:
#Symbol  Value
#I       1
#V       5
#X       10
#L       50
#C       100
#D       500
#M       1000
#
#Roman numerals are formed by appending the conversions of decimal place values
#from highest to lowest.
#
#Example 1:
#Input: num = 3749
#Output: "MMMDCCXLIX"
#
#Example 2:
#Input: num = 58
#Output: "LVIII"
#
#Example 3:
#Input: num = 1994
#Output: "MCMXCIV"
#
#Constraints:
#    1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Greedy approach using value-symbol pairs.
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []

        for i, value in enumerate(values):
            count = num // value
            if count:
                result.append(symbols[i] * count)
                num %= value

        return ''.join(result)


class SolutionDigitByDigit:
    def intToRoman(self, num: int) -> str:
        """
        Process each digit position separately.
        """
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (thousands[num // 1000] +
                hundreds[(num % 1000) // 100] +
                tens[(num % 100) // 10] +
                ones[num % 10])


class SolutionIterative:
    def intToRoman(self, num: int) -> str:
        """
        Iterative approach with dictionary.
        """
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = []

        for value, symbol in mapping:
            while num >= value:
                result.append(symbol)
                num -= value

        return ''.join(result)
