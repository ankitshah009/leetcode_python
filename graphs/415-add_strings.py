#415. Add Strings
#Easy
#
#Given two non-negative integers, num1 and num2 represented as string, return
#the sum of num1 and num2 as a string.
#
#You must solve the problem without using any built-in library for handling
#large integers (such as BigInteger). You must also not convert the inputs to
#integers directly.
#
#Example 1:
#Input: num1 = "11", num2 = "456"
#Output: "467"
#
#Example 2:
#Input: num1 = "456", num2 = "77"
#Output: "533"
#
#Example 3:
#Input: num1 = "0", num2 = "0"
#Output: "0"
#
#Constraints:
#    1 <= num1.length, num2.length <= 10^4
#    num1 and num2 consist of only digits.
#    num1 and num2 don't have any leading zeros except for the zero itself.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """Two pointer from right to left"""
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        return ''.join(result[::-1])


class SolutionOrd:
    """Using ord() instead of int()"""

    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = d1 + d2 + carry
            carry = total // 10
            result.append(chr(total % 10 + ord('0')))

            i -= 1
            j -= 1

        return ''.join(result[::-1])


class SolutionPadded:
    """Pad shorter number with zeros"""

    def addStrings(self, num1: str, num2: str) -> str:
        # Pad to same length
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            total = int(num1[i]) + int(num2[i]) + carry
            carry = total // 10
            result.append(str(total % 10))

        if carry:
            result.append('1')

        return ''.join(result[::-1])
