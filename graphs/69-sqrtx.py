#69. Sqrt(x)
#Easy
#
#Given a non-negative integer x, return the square root of x rounded down to the
#nearest integer. The returned integer should be non-negative as well.
#
#You must not use any built-in exponent function or operator.
#
#Example 1:
#Input: x = 4
#Output: 2
#Explanation: The square root of 4 is 2, so we return 2.
#
#Example 2:
#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since we round it down to
#the nearest integer, 2 is returned.
#
#Constraints:
#    0 <= x <= 2^31 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Binary search approach.
        """
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


class SolutionNewton:
    def mySqrt(self, x: int) -> int:
        """
        Newton's method (Heron's method).
        """
        if x < 2:
            return x

        guess = x

        while guess * guess > x:
            guess = (guess + x // guess) // 2

        return guess


class SolutionBitManipulation:
    def mySqrt(self, x: int) -> int:
        """
        Bit manipulation - find each bit of the result.
        """
        if x < 2:
            return x

        # Start from the highest bit
        result = 0
        bit = 1 << 15  # sqrt(2^31) < 2^16

        while bit > 0:
            result |= bit
            if result * result > x:
                result ^= bit
            bit >>= 1

        return result


class SolutionExponential:
    def mySqrt(self, x: int) -> int:
        """
        Using logarithm identity (if math functions allowed).
        sqrt(x) = e^(0.5 * ln(x))
        """
        if x < 2:
            return x

        import math
        left = int(math.exp(0.5 * math.log(x)))
        right = left + 1

        return left if right * right > x else right


class SolutionLinear:
    def mySqrt(self, x: int) -> int:
        """
        Linear search - O(sqrt(x)) - for comparison.
        """
        if x < 2:
            return x

        result = 1
        while result * result <= x:
            result += 1

        return result - 1
