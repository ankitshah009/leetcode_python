#231. Power of Two
#Easy
#
#Given an integer n, return true if it is a power of two. Otherwise, return false.
#
#An integer n is a power of two, if there exists an integer x such that n == 2^x.
#
#Example 1:
#Input: n = 1
#Output: true
#Explanation: 2^0 = 1
#
#Example 2:
#Input: n = 16
#Output: true
#Explanation: 2^4 = 16
#
#Example 3:
#Input: n = 3
#Output: false
#
#Constraints:
#    -2^31 <= n <= 2^31 - 1
#
#Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Bit manipulation: n & (n-1) removes the lowest set bit.
        Power of two has exactly one bit set, so n & (n-1) == 0.
        """
        return n > 0 and (n & (n - 1)) == 0


class SolutionCountBits:
    """Count number of set bits"""

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1


class SolutionLoop:
    """Iterative division"""

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2

        return True


class SolutionMath:
    """Using math log"""

    def isPowerOfTwo(self, n: int) -> bool:
        import math

        if n <= 0:
            return False

        log_val = math.log2(n)
        return log_val == int(log_val)


class SolutionMaxPower:
    """Using max power of 2 in 32-bit range"""

    def isPowerOfTwo(self, n: int) -> bool:
        # 2^30 is the largest power of 2 in 32-bit signed integer range
        return n > 0 and (1 << 30) % n == 0


class SolutionLowestBit:
    """Check if lowest set bit equals n"""

    def isPowerOfTwo(self, n: int) -> bool:
        # n & (-n) isolates the lowest set bit
        return n > 0 and (n & (-n)) == n
