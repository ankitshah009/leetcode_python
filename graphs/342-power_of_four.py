#342. Power of Four
#Easy
#
#Given an integer n, return true if it is a power of four. Otherwise, return
#false.
#
#An integer n is a power of four, if there exists an integer x such that
#n == 4^x.
#
#Example 1:
#Input: n = 16
#Output: true
#
#Example 2:
#Input: n = 5
#Output: false
#
#Example 3:
#Input: n = 1
#Output: true
#
#Constraints:
#    -2^31 <= n <= 2^31 - 1
#
#Follow up: Could you solve it without loops/recursion?

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Bit manipulation approach.
        Power of 4 must be:
        1. Positive
        2. Power of 2 (only one bit set)
        3. The bit must be at an even position (0, 2, 4, ...)

        0x55555555 = 0101 0101 ... (mask for even positions)
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


class SolutionMod:
    """Using modulo property"""

    def isPowerOfFour(self, n: int) -> bool:
        # Power of 4 - 1 is divisible by 3
        # 4^x - 1 = (4-1)(4^(x-1) + 4^(x-2) + ... + 1) = 3 * something
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0


class SolutionLog:
    """Using logarithm"""

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        log_result = math.log(n) / math.log(4)
        return abs(log_result - round(log_result)) < 1e-10


class SolutionLoop:
    """Iterative division"""

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1


class SolutionRecursive:
    """Recursive approach"""

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)


class SolutionSet:
    """Precomputed powers of 4"""

    def isPowerOfFour(self, n: int) -> bool:
        powers = {4**i for i in range(16)}  # 4^15 is within int32
        return n in powers
