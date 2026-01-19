#343. Integer Break
#Medium
#
#Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize
#the product of those integers.
#
#Return the maximum product you can get.
#
#Example 1:
#Input: n = 2
#Output: 1
#Explanation: 2 = 1 + 1, 1 * 1 = 1.
#
#Example 2:
#Input: n = 10
#Output: 36
#Explanation: 10 = 3 + 3 + 4, 3 * 3 * 4 = 36.
#
#Constraints:
#    2 <= n <= 58

class Solution:
    def integerBreak(self, n: int) -> int:
        # Math insight: 3s are optimal for maximizing product
        # For n <= 3, we need at least 2 parts
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Use as many 3s as possible
        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            # Use one less 3 and use a 4 (3+1 -> 2+2 is better: 4 > 3)
            return 3 ** (n // 3 - 1) * 4
        else:  # n % 3 == 2
            return 3 ** (n // 3) * 2
