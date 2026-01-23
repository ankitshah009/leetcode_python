#738. Monotone Increasing Digits
#Medium
#
#An integer has monotone increasing digits if and only if each pair of adjacent
#digits x and y satisfy x <= y.
#
#Given an integer n, return the largest number that is less than or equal to n
#with monotone increasing digits.
#
#Example 1:
#Input: n = 10
#Output: 9
#
#Example 2:
#Input: n = 1234
#Output: 1234
#
#Example 3:
#Input: n = 332
#Output: 299
#
#Constraints:
#    0 <= n <= 10^9

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
        Find first decrease point, set to d-1, and all following to 9.
        """
        digits = list(str(n))

        # Find the first position where digit decreases
        mark = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                mark = i
                digits[i - 1] = str(int(digits[i - 1]) - 1)

        # Set all digits after mark to 9
        for i in range(mark, len(digits)):
            digits[i] = '9'

        return int(''.join(digits))


class SolutionDetailed:
    """More explicit approach"""

    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        length = len(s)

        # Find rightmost peak where s[i-1] > s[i]
        i = 1
        while i < length and s[i - 1] <= s[i]:
            i += 1

        if i == length:
            return n  # Already monotone increasing

        # Go back to handle equal digits
        while i > 1 and s[i - 1] == s[i - 2]:
            i -= 1

        # Decrement and fill with 9s
        while i > 0 and i < length and s[i - 1] > s[i]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            i -= 1

        # Fill rest with 9s
        for j in range(i + 1, length):
            s[j] = '9'

        return int(''.join(s))


class SolutionGreedy:
    """Greedy from left to right"""

    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))

        # Find first violation from right
        cliff = len(digits)

        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                cliff = i
                digits[i - 1] = chr(ord(digits[i - 1]) - 1)

        # Set everything after cliff to 9
        for i in range(cliff, len(digits)):
            digits[i] = '9'

        return int(''.join(digits))
