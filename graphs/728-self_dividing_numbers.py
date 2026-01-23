#728. Self Dividing Numbers
#Easy
#
#A self-dividing number is a number that is divisible by every digit it contains.
#
#For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
#and 128 % 8 == 0.
#
#A self-dividing number is not allowed to contain the digit zero.
#
#Given two integers left and right, return a list of all the self-dividing
#numbers in the range [left, right].
#
#Example 1:
#Input: left = 1, right = 22
#Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
#
#Example 2:
#Input: left = 47, right = 85
#Output: [48,55,66,77]
#
#Constraints:
#    1 <= left <= right <= 10^4

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        """
        Check each number in range for self-dividing property.
        """
        def is_self_dividing(n):
            original = n
            while n > 0:
                digit = n % 10
                if digit == 0 or original % digit != 0:
                    return False
                n //= 10
            return True

        return [n for n in range(left, right + 1) if is_self_dividing(n)]


class SolutionString:
    """Using string conversion"""

    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(n):
            for c in str(n):
                d = int(c)
                if d == 0 or n % d != 0:
                    return False
            return True

        return [n for n in range(left, right + 1) if is_self_dividing(n)]


class SolutionCompact:
    """One-liner approach"""

    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        return [
            n for n in range(left, right + 1)
            if '0' not in str(n) and all(n % int(d) == 0 for d in str(n))
        ]


class SolutionDivmod:
    """Using divmod for digit extraction"""

    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []

        for num in range(left, right + 1):
            n = num
            valid = True

            while n > 0 and valid:
                n, digit = divmod(n, 10)
                if digit == 0 or num % digit != 0:
                    valid = False

            if valid:
                result.append(num)

        return result
