#935. Knight Dialer
#Medium
#
#The chess knight has a unique movement, it may move two squares vertically and
#one square horizontally, or two squares horizontally and one square vertically.
#
#Given an integer n, return how many distinct phone numbers of length n we can
#dial. A phone number contains only digits 0-9.
#
#The knight may start on any digit, and the answer may be very large, so return
#the answer modulo 10^9 + 7.
#
#Example 1:
#Input: n = 1
#Output: 10
#
#Example 2:
#Input: n = 2
#Output: 20
#
#Example 3:
#Input: n = 3131
#Output: 136006598
#
#Constraints:
#    1 <= n <= 5000

class Solution:
    def knightDialer(self, n: int) -> int:
        """
        DP: track count of numbers ending at each digit.
        """
        MOD = 10 ** 9 + 7

        # Moves from each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        # dp[digit] = count of numbers ending at digit
        dp = [1] * 10

        for _ in range(n - 1):
            new_dp = [0] * 10
            for digit in range(10):
                for prev in moves[digit]:
                    new_dp[digit] = (new_dp[digit] + dp[prev]) % MOD
            dp = new_dp

        return sum(dp) % MOD


class SolutionMemo:
    """Memoization approach"""

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        moves = {
            0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
            5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
        }

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(digit: int, remaining: int) -> int:
            if remaining == 0:
                return 1

            total = 0
            for next_digit in moves[digit]:
                total = (total + dp(next_digit, remaining - 1)) % MOD
            return total

        return sum(dp(d, n - 1) for d in range(10)) % MOD


class SolutionMatrix:
    """Matrix exponentiation for O(log n)"""

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 1:
            return 10

        # Adjacency matrix for knight moves
        M = [
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 0
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],  # 1
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 2
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 3
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],  # 6
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 7
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 8
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # 9
        ]

        def matrix_mult(A, B):
            size = len(A)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        def matrix_pow(M, power):
            size = len(M)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

            while power > 0:
                if power % 2 == 1:
                    result = matrix_mult(result, M)
                M = matrix_mult(M, M)
                power //= 2

            return result

        result_matrix = matrix_pow(M, n - 1)
        return sum(sum(row) for row in result_matrix) % MOD
