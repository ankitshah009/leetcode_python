#1137. N-th Tribonacci Number
#Easy
#
#The Tribonacci sequence Tn is defined as follows:
#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
#Given n, return the value of Tn.
#
#Example 1:
#Input: n = 4
#Output: 4
#Explanation: T_3 = 0 + 1 + 1 = 2, T_4 = 1 + 1 + 2 = 4
#
#Example 2:
#Input: n = 25
#Output: 1389537
#
#Constraints:
#    0 <= n <= 37
#    The answer is guaranteed to fit within a 32-bit integer.

class Solution:
    def tribonacci(self, n: int) -> int:
        """Iterative O(1) space"""
        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


class SolutionDP:
    def tribonacci(self, n: int) -> int:
        """DP array"""
        if n == 0:
            return 0
        if n <= 2:
            return 1

        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]


class SolutionMatrix:
    def tribonacci(self, n: int) -> int:
        """Matrix exponentiation O(log n)"""
        if n == 0:
            return 0
        if n <= 2:
            return 1

        def multiply(A, B):
            return [
                [sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
                for i in range(3)
            ]

        def matrix_power(M, p):
            result = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
            while p:
                if p & 1:
                    result = multiply(result, M)
                M = multiply(M, M)
                p >>= 1
            return result

        M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        result = matrix_power(M, n - 2)
        return result[0][0] + result[0][1]
