#372. Super Pow
#Medium
#
#Your task is to calculate a^b mod 1337 where a is a positive integer and b is
#an extremely large positive integer given in the form of an array.
#
#Example 1:
#Input: a = 2, b = [3]
#Output: 8
#
#Example 2:
#Input: a = 2, b = [1,0]
#Output: 1024
#
#Example 3:
#Input: a = 1, b = [4,3,3,8,5,2]
#Output: 1
#
#Constraints:
#    1 <= a <= 2^31 - 1
#    1 <= b.length <= 2000
#    0 <= b[i] <= 9

from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """
        Use the property: a^(10x+y) = (a^x)^10 * a^y
        Process digits from left to right.
        """
        MOD = 1337

        def power(base, exp):
            """Calculate base^exp mod MOD"""
            base %= MOD
            result = 1
            for _ in range(exp):
                result = (result * base) % MOD
            return result

        result = 1
        for digit in b:
            result = power(result, 10) * power(a, digit) % MOD

        return result


class SolutionFastPow:
    """Using fast exponentiation"""

    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def fast_pow(base, exp):
            base %= MOD
            result = 1
            while exp > 0:
                if exp & 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp >>= 1
            return result

        result = 1
        for digit in b:
            result = fast_pow(result, 10) * fast_pow(a, digit) % MOD

        return result


class SolutionRecursive:
    """Recursive approach"""

    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def power(x, n):
            if n == 0:
                return 1
            x %= MOD
            if n % 2 == 0:
                return power(x * x, n // 2) % MOD
            return x * power(x, n - 1) % MOD

        if not b:
            return 1

        last_digit = b.pop()
        return power(self.superPow(a, b), 10) * power(a, last_digit) % MOD
