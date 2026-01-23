#633. Sum of Square Numbers
#Medium
#
#Given a non-negative integer c, decide whether there are two integers a and b
#such that a^2 + b^2 = c.
#
#Example 1:
#Input: c = 5
#Output: true
#Explanation: 1 * 1 + 2 * 2 = 5
#
#Example 2:
#Input: c = 3
#Output: false
#
#Constraints:
#    0 <= c <= 2^31 - 1

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """Two pointers approach"""
        left, right = 0, int(math.sqrt(c))

        while left <= right:
            total = left * left + right * right

            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1

        return False


class SolutionSet:
    """Using set for lookup"""

    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        a = 0

        while a * a <= c:
            squares.add(a * a)
            a += 1

        for sq in squares:
            if c - sq in squares:
                return True

        return False


class SolutionSqrt:
    """Check if c - a^2 is perfect square"""

    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b_sq = c - a * a
            b = int(math.sqrt(b_sq))
            if b * b == b_sq:
                return True
            a += 1
        return False


class SolutionFermat:
    """
    Fermat's theorem on sums of two squares.
    A number can be represented as sum of two squares iff
    all prime factors of the form (4k+3) occur to an even power.
    """

    def judgeSquareSum(self, c: int) -> bool:
        def is_sum_of_squares(n):
            i = 2
            while i * i <= n:
                count = 0
                if n % i == 0:
                    while n % i == 0:
                        count += 1
                        n //= i
                    if i % 4 == 3 and count % 2 != 0:
                        return False
                i += 1
            return n % 4 != 3

        return is_sum_of_squares(c)
