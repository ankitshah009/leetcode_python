#790. Domino and Tromino Tiling
#Medium
#
#You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may
#rotate these shapes.
#
#Given an integer n, return the number of ways to tile an 2 x n board. Since
#the answer may be very large, return it modulo 10^9 + 7.
#
#In a tiling, every square must be covered by a tile. Two tilings are different
#if and only if there are two 4-directionally adjacent cells on the board such
#that exactly one of the tilings has both squares occupied by a tile.
#
#Example 1:
#Input: n = 3
#Output: 5
#
#Example 2:
#Input: n = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 1000

class Solution:
    def numTilings(self, n: int) -> int:
        """
        DP with states: full, top gap, bottom gap.
        Recurrence: f(n) = f(n-1) + f(n-2) + 2*t(n-1)
                    t(n) = f(n-2) + t(n-1)
        Simplified: f(n) = 2*f(n-1) + f(n-3)
        """
        MOD = 10**9 + 7

        if n <= 2:
            return n

        # dp[i] = ways to fully tile 2xi board
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]


class SolutionMatrix:
    """Matrix exponentiation for O(log n)"""

    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        def multiply(A, B):
            return [
                [(A[0][0]*B[0][0] + A[0][1]*B[1][0] + A[0][2]*B[2][0]) % MOD,
                 (A[0][0]*B[0][1] + A[0][1]*B[1][1] + A[0][2]*B[2][1]) % MOD,
                 (A[0][0]*B[0][2] + A[0][1]*B[1][2] + A[0][2]*B[2][2]) % MOD],
                [(A[1][0]*B[0][0] + A[1][1]*B[1][0] + A[1][2]*B[2][0]) % MOD,
                 (A[1][0]*B[0][1] + A[1][1]*B[1][1] + A[1][2]*B[2][1]) % MOD,
                 (A[1][0]*B[0][2] + A[1][1]*B[1][2] + A[1][2]*B[2][2]) % MOD],
                [(A[2][0]*B[0][0] + A[2][1]*B[1][0] + A[2][2]*B[2][0]) % MOD,
                 (A[2][0]*B[0][1] + A[2][1]*B[1][1] + A[2][2]*B[2][1]) % MOD,
                 (A[2][0]*B[0][2] + A[2][1]*B[1][2] + A[2][2]*B[2][2]) % MOD]
            ]

        def power(M, n):
            result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            while n:
                if n & 1:
                    result = multiply(result, M)
                M = multiply(M, M)
                n >>= 1
            return result

        if n <= 2:
            return n

        M = [[2, 0, 1], [1, 0, 0], [0, 1, 0]]
        result = power(M, n - 2)

        return (result[0][0] * 2 + result[0][1] * 1 + result[0][2] * 1) % MOD


class SolutionFullState:
    """Full state DP"""

    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # f[i] = full, t[i] = one cell sticking out
        f = [0] * (n + 1)
        t = [0] * (n + 1)

        f[0] = 1
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = (f[i - 1] + f[i - 2] + 2 * t[i - 1]) % MOD
            t[i] = (f[i - 2] + t[i - 1]) % MOD

        return f[n]
