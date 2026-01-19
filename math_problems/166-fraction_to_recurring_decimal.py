#166. Fraction to Recurring Decimal
#Medium
#
#Given two integers representing the numerator and denominator of a fraction,
#return the fraction in string format.
#
#If the fractional part is repeating, enclose the repeating part in parentheses.
#
#If multiple answers are possible, return any of them.
#
#It is guaranteed that the length of the answer string is less than 10^4 for all
#the given inputs.
#
#Example 1:
#Input: numerator = 1, denominator = 2
#Output: "0.5"
#
#Example 2:
#Input: numerator = 2, denominator = 1
#Output: "2"
#
#Example 3:
#Input: numerator = 4, denominator = 333
#Output: "0.(012)"
#
#Constraints:
#    -2^31 <= numerator, denominator <= 2^31 - 1
#    denominator != 0

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)

        result.append(".")

        # Fractional part - track remainders to detect cycle
        remainder_positions = {}

        while remainder != 0:
            if remainder in remainder_positions:
                # Found repeating pattern
                pos = remainder_positions[remainder]
                result.insert(pos, "(")
                result.append(")")
                break

            remainder_positions[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder = remainder % denominator

        return "".join(result)
