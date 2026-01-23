#1281. Subtract the Product and Sum of Digits of an Integer
#Easy
#
#Given an integer number n, return the difference between the product of its
#digits and the sum of its digits.
#
#Example 1:
#Input: n = 234
#Output: 15
#Explanation:
#Product of digits = 2 * 3 * 4 = 24
#Sum of digits = 2 + 3 + 4 = 9
#Result = 24 - 9 = 15
#
#Example 2:
#Input: n = 4421
#Output: 21
#Explanation:
#Product of digits = 4 * 4 * 2 * 1 = 32
#Sum of digits = 4 + 4 + 2 + 1 = 11
#Result = 32 - 11 = 21
#
#Constraints:
#    1 <= n <= 10^5

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """Calculate product and sum of digits"""
        product = 1
        total = 0

        while n > 0:
            digit = n % 10
            product *= digit
            total += digit
            n //= 10

        return product - total


class SolutionString:
    def subtractProductAndSum(self, n: int) -> int:
        """Using string conversion"""
        digits = [int(d) for d in str(n)]
        product = 1
        for d in digits:
            product *= d
        return product - sum(digits)


class SolutionFunctional:
    def subtractProductAndSum(self, n: int) -> int:
        """Functional approach"""
        from functools import reduce
        from operator import mul

        digits = [int(d) for d in str(n)]
        return reduce(mul, digits) - sum(digits)
