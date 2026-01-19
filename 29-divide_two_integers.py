#29. Divide Two Integers
#Medium
#
#Given two integers dividend and divisor, divide two integers without using multiplication,
#division, and mod operator.
#
#The integer division should truncate toward zero, which means losing its fractional part.
#For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
#
#Return the quotient after dividing dividend by divisor.
#
#Note: Assume we are dealing with an environment that could only store integers within the
#32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly
#greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31,
#then return -2^31.
#
#Example 1:
#Input: dividend = 10, divisor = 3
#Output: 3
#Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
#Example 2:
#Input: dividend = 7, divisor = -3
#Output: -2
#Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
#Constraints:
#    -2^31 <= dividend, divisor <= 2^31 - 1
#    divisor != 0

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        return -quotient if negative else quotient
