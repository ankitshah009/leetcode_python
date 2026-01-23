#592. Fraction Addition and Subtraction
#Medium
#
#Given a string expression representing an expression of fraction addition and
#subtraction, return the calculation result in string format.
#
#The final result should be an irreducible fraction.
#
#Example 1:
#Input: expression = "-1/2+1/2"
#Output: "0/1"
#
#Example 2:
#Input: expression = "-1/2+1/2+1/3"
#Output: "1/3"
#
#Example 3:
#Input: expression = "1/3-1/2"
#Output: "-1/6"
#
#Constraints:
#    The input string only contains '0' to '9', '/', '+' and '-'.
#    Each fraction in the input has integer numerator and denominator.

import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        """Parse fractions and compute result"""
        # Find all fractions (including sign)
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        numerator = 0
        denominator = 1

        for frac in fractions:
            parts = frac.split('/')
            num, den = int(parts[0]), int(parts[1])

            # Add fraction: a/b + c/d = (ad + bc) / bd
            numerator = numerator * den + num * denominator
            denominator = denominator * den

            # Reduce
            g = gcd(abs(numerator), denominator)
            numerator //= g
            denominator //= g

        return f"{numerator}/{denominator}"


class SolutionManualParse:
    """Manual parsing without regex"""

    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1

        i = 0
        n = len(expression)

        while i < n:
            # Get sign
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1

            # Get numerator
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            num *= sign

            # Skip '/'
            i += 1

            # Get denominator
            den = 0
            while i < n and expression[i].isdigit():
                den = den * 10 + int(expression[i])
                i += 1

            # Add to result
            numerator = numerator * den + num * denominator
            denominator = denominator * den

            g = gcd(abs(numerator), denominator)
            numerator //= g
            denominator //= g

        return f"{numerator}/{denominator}"
