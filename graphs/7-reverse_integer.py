#7. Reverse Integer
#Medium
#
#Given a signed 32-bit integer x, return x with its digits reversed. If
#reversing x causes the value to go outside the signed 32-bit integer range
#[-2^31, 2^31 - 1], then return 0.
#
#Assume the environment does not allow you to store 64-bit integers (signed or
#unsigned).
#
#Example 1:
#Input: x = 123
#Output: 321
#
#Example 2:
#Input: x = -123
#Output: -321
#
#Example 3:
#Input: x = 120
#Output: 21
#
#Constraints:
#    -2^31 <= x <= 2^31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digit by digit with overflow check.
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1 if x >= 0 else -1
        x = abs(x)
        result = 0

        while x:
            digit = x % 10
            x //= 10

            # Check overflow before adding digit
            if result > INT_MAX // 10:
                return 0
            if result == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0

            result = result * 10 + digit

        return sign * result


class SolutionString:
    def reverse(self, x: int) -> int:
        """
        String reversal approach.
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1 if x >= 0 else -1
        reversed_str = str(abs(x))[::-1]
        result = sign * int(reversed_str)

        if result < INT_MIN or result > INT_MAX:
            return 0

        return result


class SolutionMath:
    def reverse(self, x: int) -> int:
        """
        Mathematical approach with Python's big integers.
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        result = sign * reversed_num

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
