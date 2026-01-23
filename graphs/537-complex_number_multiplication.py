#537. Complex Number Multiplication
#Medium
#
#A complex number can be represented as a string on the form "real+imaginaryi" where:
#- real is the real part and is an integer in the range [-100, 100].
#- imaginary is the imaginary part and is an integer in the range [-100, 100].
#- i^2 == -1.
#
#Given two complex numbers num1 and num2 as strings, return a string of the complex
#number that represents their multiplications.
#
#Example 1:
#Input: num1 = "1+1i", num2 = "1+1i"
#Output: "0+2i"
#Explanation: (1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i, and you need to convert it
#to the form of "0+2i".
#
#Example 2:
#Input: num1 = "1+-1i", num2 = "1+-1i"
#Output: "0+-2i"
#
#Constraints:
#    num1 and num2 are valid complex numbers.

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        """
        def parse(s):
            # Split "a+bi" into (a, b)
            real, imag = s[:-1].split('+')
            return int(real), int(imag)

        a, b = parse(num1)
        c, d = parse(num2)

        real = a * c - b * d
        imag = a * d + b * c

        return f"{real}+{imag}i"


class SolutionRegex:
    """Using regex for parsing"""

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        import re

        def parse(s):
            match = re.match(r'(-?\d+)\+(-?\d+)i', s)
            return int(match.group(1)), int(match.group(2))

        a, b = parse(num1)
        c, d = parse(num2)

        real = a * c - b * d
        imag = a * d + b * c

        return f"{real}+{imag}i"


class SolutionComplex:
    """Using Python's complex numbers"""

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def to_complex(s):
            # Replace 'i' with 'j' for Python
            s = s.replace('i', 'j')
            return complex(s)

        result = to_complex(num1) * to_complex(num2)

        return f"{int(result.real)}+{int(result.imag)}i"
