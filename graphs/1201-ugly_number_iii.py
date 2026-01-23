#1201. Ugly Number III
#Medium
#
#An ugly number is a positive integer that is divisible by a, b, or c.
#
#Given four integers n, a, b, and c, return the nth ugly number.
#
#Example 1:
#Input: n = 3, a = 2, b = 3, c = 5
#Output: 4
#Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
#
#Example 2:
#Input: n = 4, a = 2, b = 3, c = 4
#Output: 6
#Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
#
#Example 3:
#Input: n = 5, a = 2, b = 11, c = 13
#Output: 10
#Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
#
#Constraints:
#    1 <= n, a, b, c <= 10^9
#    1 <= a * b * c <= 10^18
#    It is guaranteed that the result will be in range [1, 2 * 10^9].

import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        Binary search + inclusion-exclusion principle.

        For a number x, count how many ugly numbers <= x using:
        count = x/a + x/b + x/c - x/lcm(a,b) - x/lcm(b,c) - x/lcm(a,c) + x/lcm(a,b,c)
        """
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        # Precompute LCMs
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)

        def count_ugly(x):
            """Count ugly numbers <= x using inclusion-exclusion"""
            return (x // a + x // b + x // c
                    - x // ab - x // bc - x // ac
                    + x // abc)

        # Binary search for smallest x where count_ugly(x) >= n
        left, right = 1, 2 * 10**9

        while left < right:
            mid = (left + right) // 2
            if count_ugly(mid) < n:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionMathGcd:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """Using math.gcd and math.lcm"""
        ab = math.lcm(a, b)
        bc = math.lcm(b, c)
        ac = math.lcm(a, c)
        abc = math.lcm(a, b, c)

        def count(x):
            return (x // a + x // b + x // c
                    - x // ab - x // bc - x // ac
                    + x // abc)

        lo, hi = 1, 2 * 10**9

        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) < n:
                lo = mid + 1
            else:
                hi = mid

        return lo
