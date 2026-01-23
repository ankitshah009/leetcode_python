#1837. Sum of Digits in Base K
#Easy
#
#Given an integer n (in base 10) and a base k, return the sum of the digits of
#n after converting n from base 10 to base k.
#
#After converting, each digit should be interpreted as a base 10 number, and
#the sum should be returned in base 10.
#
#Example 1:
#Input: n = 34, k = 6
#Output: 9
#Explanation: 34 (base 10) = 54 (base 6). 5 + 4 = 9.
#
#Example 2:
#Input: n = 10, k = 10
#Output: 1
#Explanation: n is already in base 10. 1 + 0 = 1.
#
#Constraints:
#    1 <= n <= 100
#    2 <= k <= 10

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """
        Convert to base k by repeatedly taking mod and dividing.
        """
        digit_sum = 0

        while n > 0:
            digit_sum += n % k
            n //= k

        return digit_sum


class SolutionList:
    def sumBase(self, n: int, k: int) -> int:
        """
        Build list of digits then sum.
        """
        digits = []

        while n > 0:
            digits.append(n % k)
            n //= k

        return sum(digits)


class SolutionRecursive:
    def sumBase(self, n: int, k: int) -> int:
        """
        Recursive approach.
        """
        if n == 0:
            return 0
        return n % k + self.sumBase(n // k, k)


class SolutionBuiltin:
    def sumBase(self, n: int, k: int) -> int:
        """
        Using numpy base conversion (if available).
        """
        import numpy as np
        return sum(int(d) for d in np.base_repr(n, k))
