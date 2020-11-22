#371. Sum of Two Integers
#Medium
#
#Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
#Example 1:
#
#Input: a = 1, b = 2
#Output: 3
#
#Example 2:
#
#Input: a = -2, b = 3
#Output: 1
#


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
