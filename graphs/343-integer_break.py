#343. Integer Break
#Medium
#
#Given an integer n, break it into the sum of k positive integers, where k >= 2,
#and maximize the product of those integers.
#
#Return the maximum product you can get.
#
#Example 1:
#Input: n = 2
#Output: 1
#Explanation: 2 = 1 + 1, 1 × 1 = 1.
#
#Example 2:
#Input: n = 10
#Output: 36
#Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#
#Constraints:
#    2 <= n <= 58

class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Mathematical insight:
        - Use as many 3s as possible, but avoid leaving remainder 1
        - If remainder is 1, use one less 3 and make a 4 (2+2)
        - If remainder is 2, just multiply by 2
        """
        if n == 2:
            return 1
        if n == 3:
            return 2

        quotient, remainder = divmod(n, 3)

        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:  # remainder == 2
            return 3 ** quotient * 2


class SolutionDP:
    """Dynamic programming approach"""

    def integerBreak(self, n: int) -> int:
        # dp[i] = max product for integer i
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                # Either use j as is, or break j further
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[n]


class SolutionMemo:
    """Memoization approach"""

    def integerBreak(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(num, must_break):
            if num == 0:
                return 1

            max_product = 0
            start = 1 if must_break else num  # If don't need to break, can use num itself

            for i in range(1, num):
                max_product = max(max_product, i * dp(num - i, False))

            if not must_break:
                max_product = max(max_product, num)

            return max_product

        return dp(n, True)


class SolutionGreedy:
    """Greedy: prefer 3s, then 2s"""

    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        result = 1
        while n > 4:
            result *= 3
            n -= 3

        return result * n
