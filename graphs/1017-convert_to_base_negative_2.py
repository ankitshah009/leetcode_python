#1017. Convert to Base -2
#Medium
#
#Given an integer n, return a binary string representing its representation in
#base -2.
#
#Note that the returned string should not have leading zeros unless the string
#is "0".
#
#Example 1:
#Input: n = 2
#Output: "110"
#Explanation: (-2)^2 + (-2)^1 = 4 + (-2) = 2
#
#Example 2:
#Input: n = 3
#Output: "111"
#Explanation: (-2)^2 + (-2)^1 + (-2)^0 = 4 + (-2) + 1 = 3
#
#Example 3:
#Input: n = 4
#Output: "100"
#
#Constraints:
#    0 <= n <= 10^9

class Solution:
    def baseNeg2(self, n: int) -> str:
        """
        Division with remainder, handling negative base.
        """
        if n == 0:
            return "0"

        result = []

        while n != 0:
            remainder = n % (-2)
            n //= -2

            # In Python, remainder can be negative for negative divisor
            if remainder < 0:
                remainder += 2
                n += 1

            result.append(str(remainder))

        return ''.join(reversed(result))


class SolutionAlt:
    """Alternative using bit manipulation"""

    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        result = []

        while n != 0:
            result.append(str(n & 1))
            n = -(n >> 1)

        return ''.join(reversed(result))


class SolutionExplicit:
    """More explicit calculation"""

    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        bits = []
        base = -2

        while n != 0:
            # Get remainder (always 0 or 1)
            if n % 2 == 0:
                bits.append('0')
                n //= base
            else:
                bits.append('1')
                n = (n - 1) // base

        return ''.join(reversed(bits))
