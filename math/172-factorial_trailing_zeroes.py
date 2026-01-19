#172. Factorial Trailing Zeroes
#Medium
#
#Given an integer n, return the number of trailing zeroes in n!.
#
#Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
#
#Example 1:
#Input: n = 3
#Output: 0
#Explanation: 3! = 6, no trailing zero.
#
#Example 2:
#Input: n = 5
#Output: 1
#Explanation: 5! = 120, one trailing zero.
#
#Example 3:
#Input: n = 0
#Output: 0
#
#Constraints:
#    0 <= n <= 10^4
#
#Follow up: Could you write a solution that works in logarithmic time complexity?

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Trailing zeros come from factors of 10, which = 2 * 5.
        Since there are always more factors of 2 than 5, we just count factors of 5.
        We also need to count 25, 125, etc. (powers of 5).
        """
        count = 0
        power_of_5 = 5

        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5

        return count


class SolutionSimple:
    """Simpler version dividing n"""

    def trailingZeroes(self, n: int) -> int:
        count = 0

        while n >= 5:
            n //= 5
            count += n

        return count


class SolutionRecursive:
    """Recursive approach"""

    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)
