#367. Valid Perfect Square
#Easy
#
#Given a positive integer num, return true if num is a perfect square or false
#otherwise.
#
#A perfect square is an integer that is the square of an integer. In other
#words, it is the product of some integer with itself.
#
#You must not use any built-in library function, such as sqrt.
#
#Example 1:
#Input: num = 16
#Output: true
#Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#
#Example 2:
#Input: num = 14
#Output: false
#Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an
#integer.
#
#Constraints:
#    1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """Binary search approach"""
        if num == 1:
            return True

        left, right = 1, num // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False


class SolutionNewton:
    """Newton's method for square root"""

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        x = num
        while x * x > num:
            x = (x + num // x) // 2

        return x * x == num


class SolutionOddNumbers:
    """
    Mathematical property: Perfect squares are sum of consecutive odd numbers.
    1 = 1
    4 = 1 + 3
    9 = 1 + 3 + 5
    16 = 1 + 3 + 5 + 7
    """

    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        while num > 0:
            num -= odd
            odd += 2

        return num == 0


class SolutionBitwise:
    """Binary search with bitwise operations"""

    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        # Find the number of bits needed
        x = num
        bits = 0
        while x:
            bits += 1
            x >>= 1

        # Start from half the bits (approximate sqrt)
        x = 1 << ((bits + 1) // 2)

        while x * x > num:
            x = (x + num // x) >> 1

        return x * x == num
