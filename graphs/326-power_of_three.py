#326. Power of Three
#Easy
#
#Given an integer n, return true if it is a power of three. Otherwise, return
#false.
#
#An integer n is a power of three, if there exists an integer x such that
#n == 3^x.
#
#Example 1:
#Input: n = 27
#Output: true
#Explanation: 27 = 3^3
#
#Example 2:
#Input: n = 0
#Output: false
#Explanation: There is no x where 3^x = 0.
#
#Example 3:
#Input: n = -1
#Output: false
#Explanation: There is no x where 3^x = (-1).
#
#Constraints:
#    -2^31 <= n <= 2^31 - 1
#
#Follow up: Could you solve it without loops/recursion?

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Mathematical approach without loops.
        3^19 = 1162261467 is the largest power of 3 that fits in 32-bit signed int.
        If n is a power of 3, then 3^19 % n == 0
        """
        return n > 0 and 1162261467 % n == 0


class SolutionLoop:
    """Iterative division"""

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1


class SolutionLog:
    """Using logarithm"""

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        # log3(n) = log(n) / log(3)
        log_result = math.log10(n) / math.log10(3)

        # Check if it's an integer (handle floating point errors)
        return abs(log_result - round(log_result)) < 1e-10


class SolutionRecursive:
    """Recursive approach"""

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)


class SolutionSet:
    """Precomputed powers of 3"""

    def isPowerOfThree(self, n: int) -> bool:
        powers = {3**i for i in range(20)}  # 3^19 is max in int32
        return n in powers
