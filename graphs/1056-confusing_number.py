#1056. Confusing Number
#Easy
#
#A confusing number is a number that when rotated 180 degrees becomes a
#different number with each digit valid.
#
#We can rotate digits of a number by 180 degrees to form new digits:
#    0 rotates to 0
#    1 rotates to 1
#    6 rotates to 9
#    8 rotates to 8
#    9 rotates to 6
#
#When rotated, 2, 3, 4, 5 and 7 become invalid.
#
#Note that after rotating a number, we can ignore leading zeros. For example,
#after rotating 8000, we have 0008 which is considered as just 8.
#
#Given an integer n, return true if it is a confusing number, or false otherwise.
#
#Example 1:
#Input: n = 6
#Output: true
#Explanation: We get 9 after rotating 6, 9 is a valid number and 9 != 6.
#
#Example 2:
#Input: n = 89
#Output: true
#Explanation: We get 68 after rotating 89.
#
#Example 3:
#Input: n = 11
#Output: false
#Explanation: We get 11 after rotating 11.
#
#Constraints:
#    0 <= n <= 10^9

class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        Check if all digits are valid and rotated number is different.
        """
        rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        invalid = {'2', '3', '4', '5', '7'}

        s = str(n)

        # Check for invalid digits
        if any(d in invalid for d in s):
            return False

        # Build rotated number
        rotated = ''.join(rotate_map[d] for d in reversed(s))

        return rotated != s


class SolutionMath:
    def confusingNumber(self, n: int) -> bool:
        """Mathematical approach without string conversion"""
        rotate_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        valid_digits = {0, 1, 6, 8, 9}

        original = n
        rotated = 0

        while n > 0:
            digit = n % 10
            if digit not in valid_digits:
                return False
            rotated = rotated * 10 + rotate_map[digit]
            n //= 10

        return rotated != original


class SolutionCompact:
    def confusingNumber(self, n: int) -> bool:
        """Compact one-liner style"""
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        original = n
        rotated = 0

        while n:
            d = n % 10
            if d not in mapping:
                return False
            rotated = rotated * 10 + mapping[d]
            n //= 10

        return rotated != original
