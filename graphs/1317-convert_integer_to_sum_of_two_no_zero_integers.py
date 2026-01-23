#1317. Convert Integer to the Sum of Two No-Zero Integers
#Easy
#
#No-Zero integer is a positive integer that does not contain any 0 in its
#decimal representation.
#
#Given an integer n, return a list of two integers [a, b] where:
#    a and b are No-Zero integers.
#    a + b = n
#
#The test cases are generated so that there is at least one valid solution.
#If there are many valid solutions, you can return any of them.
#
#Example 1:
#Input: n = 2
#Output: [1,1]
#Explanation: Let a = 1, b = 1. Both a and b are no-zero integers, and a + b = 2 = n.
#
#Example 2:
#Input: n = 11
#Output: [2,9]
#Explanation: Let a = 2, b = 9. Both a and b are no-zero integers, and a + b = 11 = n.
#Note that there are other valid answers as [8, 3] that can be accepted.
#
#Constraints:
#    2 <= n <= 10^4

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Try values from 1 to n-1, check both parts for zeros.
        """
        def has_zero(num):
            return '0' in str(num)

        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]

        return []  # Should never reach here given constraints


class SolutionDigitCheck:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """Check for zeros without string conversion"""
        def has_zero(num):
            while num > 0:
                if num % 10 == 0:
                    return True
                num //= 10
            return False

        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]

        return []
