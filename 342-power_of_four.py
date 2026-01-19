#342. Power of Four
#Easy
#
#Given an integer n, return true if it is a power of four. Otherwise, return false.
#
#An integer n is a power of four, if there exists an integer x such that n == 4^x.
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

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n must be positive, power of 2, and have 1-bit at odd position
        # 0x55555555 = 01010101... in binary (1s at positions 0, 2, 4, ...)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

    def isPowerOfFour_loop(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1
