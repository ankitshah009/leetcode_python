#878. Nth Magical Number
#Hard
#
#A positive integer is magical if it is divisible by either a or b.
#
#Given the three integers n, a, and b, return the nth magical number. Since the
#answer may be very large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 1, a = 2, b = 3
#Output: 2
#
#Example 2:
#Input: n = 4, a = 2, b = 3
#Output: 6
#
#Example 3:
#Input: n = 5, a = 2, b = 4
#Output: 10
#
#Example 4:
#Input: n = 3, a = 6, b = 4
#Output: 8
#
#Constraints:
#    1 <= n <= 10^9
#    2 <= a, b <= 4 * 10^4

import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """
        Binary search: count magical numbers <= x.
        Count = x//a + x//b - x//lcm(a,b)
        """
        MOD = 10**9 + 7

        lcm = a * b // math.gcd(a, b)

        def count(x):
            """Count of magical numbers <= x"""
            return x // a + x // b - x // lcm

        # Binary search for smallest x where count(x) >= n
        left, right = 1, n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD


class SolutionMath:
    """Mathematical approach"""

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        # Ensure a <= b
        if a > b:
            a, b = b, a

        lcm = a * b // math.gcd(a, b)

        # In one LCM period, there are lcm//a + lcm//b - 1 magical numbers
        period_count = lcm // a + lcm // b - 1

        # How many complete periods?
        full_periods = n // period_count
        remainder = n % period_count

        if remainder == 0:
            return (full_periods * lcm) % MOD

        # Find the remainder-th magical number in one period
        left, right = 1, lcm

        while left < right:
            mid = (left + right) // 2
            cnt = mid // a + mid // b - mid // lcm
            if cnt < remainder:
                left = mid + 1
            else:
                right = mid

        return (full_periods * lcm + left) % MOD
