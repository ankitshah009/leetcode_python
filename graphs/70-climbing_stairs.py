#70. Climbing Stairs
#Easy
#
#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you
#climb to the top?
#
#Example 1:
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#
#Example 2:
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
#
#Constraints:
#    1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        DP with O(1) space - Fibonacci sequence.
        """
        if n <= 2:
            return n

        prev1, prev2 = 2, 1

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1


class SolutionDP:
    def climbStairs(self, n: int) -> int:
        """
        DP with array.
        """
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class SolutionMemoization:
    def climbStairs(self, n: int) -> int:
        """
        Top-down DP with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            if i <= 2:
                return i
            return dp(i - 1) + dp(i - 2)

        return dp(n)


class SolutionMatrix:
    def climbStairs(self, n: int) -> int:
        """
        Matrix exponentiation - O(log n).
        """
        def multiply(A, B):
            return [
                [A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]]
            ]

        def power(M, p):
            if p == 1:
                return M
            if p % 2 == 0:
                half = power(M, p // 2)
                return multiply(half, half)
            else:
                return multiply(M, power(M, p - 1))

        if n <= 2:
            return n

        M = [[1, 1], [1, 0]]
        result = power(M, n)
        return result[0][0]


class SolutionFormula:
    def climbStairs(self, n: int) -> int:
        """
        Binet's formula for Fibonacci.
        """
        sqrt5 = 5 ** 0.5
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2

        # F(n+1) = (phi^(n+1) - psi^(n+1)) / sqrt(5)
        return round((phi ** (n + 1) - psi ** (n + 1)) / sqrt5)
