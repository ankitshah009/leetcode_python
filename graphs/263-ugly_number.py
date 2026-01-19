#263. Ugly Number
#Easy
#
#An ugly number is a positive integer whose prime factors are limited to 2, 3,
#and 5.
#
#Given an integer n, return true if n is an ugly number.
#
#Example 1:
#Input: n = 6
#Output: true
#Explanation: 6 = 2 × 3
#
#Example 2:
#Input: n = 1
#Output: true
#Explanation: 1 has no prime factors, therefore all of its prime factors are
#limited to 2, 3, and 5.
#
#Example 3:
#Input: n = 14
#Output: false
#Explanation: 14 is not ugly since it includes the prime factor 7.
#
#Constraints:
#    -2^31 <= n <= 2^31 - 1

class Solution:
    def isUgly(self, n: int) -> bool:
        """Divide out all factors of 2, 3, 5"""
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1


class SolutionRecursive:
    """Recursive approach"""

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)

        return False


class SolutionOneLiner:
    """One-liner using reduce"""

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        from functools import reduce
        return reduce(lambda x, f: self.divide_out(x, f), [2, 3, 5], n) == 1

    def divide_out(self, n, factor):
        while n % factor == 0:
            n //= factor
        return n
