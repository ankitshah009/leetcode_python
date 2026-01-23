#509. Fibonacci Number
#Easy
#
#The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci
#sequence, such that each number is the sum of the two preceding ones, starting
#from 0 and 1.
#
#F(0) = 0, F(1) = 1
#F(n) = F(n - 1) + F(n - 2), for n > 1.
#
#Given n, calculate F(n).
#
#Example 1:
#Input: n = 2
#Output: 1
#
#Example 2:
#Input: n = 3
#Output: 2
#
#Example 3:
#Input: n = 4
#Output: 3
#
#Constraints:
#    0 <= n <= 30

class Solution:
    def fib(self, n: int) -> int:
        """Iterative O(n) time, O(1) space"""
        if n <= 1:
            return n

        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr


class SolutionDP:
    """Dynamic programming with memoization"""

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


class SolutionRecursive:
    """Recursive with memoization"""

    def fib(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def helper(k):
            if k <= 1:
                return k
            return helper(k-1) + helper(k-2)

        return helper(n)


class SolutionMatrix:
    """Matrix exponentiation O(log n)"""

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        def multiply(A, B):
            return [
                [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
            ]

        def matrix_pow(M, p):
            result = [[1, 0], [0, 1]]  # Identity matrix
            while p:
                if p & 1:
                    result = multiply(result, M)
                M = multiply(M, M)
                p >>= 1
            return result

        M = [[1, 1], [1, 0]]
        return matrix_pow(M, n)[0][1]
