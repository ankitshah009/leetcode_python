#1411. Number of Ways to Paint N × 3 Grid
#Hard
#
#You have a grid of size n x 3 and you want to paint each cell of the grid with
#exactly one of the three colors: Red, Yellow, or Green while making sure that
#no two adjacent cells have the same color (i.e., no two cells that share
#vertical or horizontal sides have the same color).
#
#Given n the number of rows of the grid, return the number of ways you can paint
#this grid. As the answer may grow large, the answer must be computed modulo
#10^9 + 7.
#
#Example 1:
#Input: n = 1
#Output: 12
#Explanation: There are 12 possible way to paint the grid as shown.
#
#Example 2:
#Input: n = 5000
#Output: 30228214
#
#Constraints:
#    n == grid.length
#    1 <= n <= 5000

class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Each row can be colored in patterns of 2 types:
        - Type A: ABC pattern (all different) - 6 patterns
        - Type B: ABA pattern (ends same) - 6 patterns

        Transitions:
        - From ABC to next row: 3 ABC + 2 ABA patterns work
        - From ABA to next row: 2 ABC + 2 ABA patterns work

        So: a_new = 3*a + 2*b
            b_new = 2*a + 2*b
        """
        MOD = 10**9 + 7

        # Type A (ABC): 6 patterns
        # Type B (ABA): 6 patterns
        a, b = 6, 6

        for _ in range(n - 1):
            a, b = (3 * a + 2 * b) % MOD, (2 * a + 2 * b) % MOD

        return (a + b) % MOD


class SolutionExplicit:
    def numOfWays(self, n: int) -> int:
        """More explicit enumeration of patterns"""
        MOD = 10**9 + 7

        # Generate all valid row patterns
        colors = [0, 1, 2]  # R, Y, G
        patterns = []

        for c1 in colors:
            for c2 in colors:
                for c3 in colors:
                    if c1 != c2 and c2 != c3:
                        patterns.append((c1, c2, c3))

        # Check if two patterns can be adjacent (vertically)
        def compatible(p1, p2):
            return all(p1[i] != p2[i] for i in range(3))

        # Build adjacency
        m = len(patterns)  # Should be 12
        adj = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                if compatible(patterns[i], patterns[j]):
                    adj[i][j] = 1

        # DP: dp[i] = number of ways to color up to current row ending with pattern i
        dp = [1] * m

        for _ in range(n - 1):
            new_dp = [0] * m
            for j in range(m):
                for i in range(m):
                    if adj[i][j]:
                        new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp

        return sum(dp) % MOD


class SolutionMatrix:
    def numOfWays(self, n: int) -> int:
        """Matrix exponentiation for O(log n) solution"""
        MOD = 10**9 + 7

        def mat_mult(A, B):
            return [
                [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
                 (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
                 (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
            ]

        def mat_pow(M, p):
            result = [[1, 0], [0, 1]]  # Identity
            while p > 0:
                if p % 2 == 1:
                    result = mat_mult(result, M)
                M = mat_mult(M, M)
                p //= 2
            return result

        # Transition matrix: [[3, 2], [2, 2]]
        M = [[3, 2], [2, 2]]
        result = mat_pow(M, n - 1)

        # Initial: a=6, b=6
        a = (result[0][0] * 6 + result[0][1] * 6) % MOD
        b = (result[1][0] * 6 + result[1][1] * 6) % MOD

        return (a + b) % MOD
