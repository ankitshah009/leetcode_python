#1444. Number of Ways of Cutting a Pizza
#Hard
#
#Given a rectangular pizza represented as a rows x cols matrix containing the
#following characters: 'A' (an apple) and '.' (empty cell) and given the integer
#k. You have to cut the pizza into k pieces using k-1 cuts.
#
#For each cut you choose the direction: vertical or horizontal, then you choose
#a cut position at the cell boundary and cut the pizza into two pieces. If you
#cut the pizza vertically, give the left part of the pizza to a person. If you
#cut the pizza horizontally, give the upper part of the pizza to a person. Give
#the last piece of pizza to the last person.
#
#Return the number of ways of cutting the pizza such that each piece contains
#at least one apple. Since the answer can be a huge number, return this modulo
#10^9 + 7.
#
#Example 1:
#Input: pizza = ["A..","AAA","..."], k = 3
#Output: 3
#Explanation: The figure above shows the three ways to cut the pizza. Note that
#pieces must contain at least one apple.
#
#Example 2:
#Input: pizza = ["A..","AA.","..."], k = 3
#Output: 1
#
#Example 3:
#Input: pizza = ["A..","A..","..."], k = 1
#Output: 1
#
#Constraints:
#    1 <= rows, cols <= 50
#    rows == pizza.length
#    cols == pizza[i].length
#    1 <= k <= 10
#    pizza consists of characters 'A' and '.' only.

from typing import List
from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        """
        DP with memoization.
        State: (row, col, cuts_remaining) - current top-left corner and cuts left.
        Precompute 2D suffix sum for apple counts.
        """
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])

        # Precompute suffix sum: apples[r][c] = apples in pizza[r:][c:]
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (1 if pizza[r][c] == 'A' else 0) + \
                               apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]

        @lru_cache(maxsize=None)
        def dp(r: int, c: int, cuts: int) -> int:
            """Ways to cut pizza[r:][c:] into 'cuts' pieces"""
            # No apples in remaining pizza
            if apples[r][c] == 0:
                return 0

            # Last piece - just need at least one apple
            if cuts == 1:
                return 1 if apples[r][c] > 0 else 0

            total = 0

            # Horizontal cuts: give upper part (rows r to nr-1)
            for nr in range(r + 1, rows):
                # Upper part: apples[r][c] - apples[nr][c]
                if apples[r][c] - apples[nr][c] > 0:
                    total = (total + dp(nr, c, cuts - 1)) % MOD

            # Vertical cuts: give left part (cols c to nc-1)
            for nc in range(c + 1, cols):
                # Left part: apples[r][c] - apples[r][nc]
                if apples[r][c] - apples[r][nc] > 0:
                    total = (total + dp(r, nc, cuts - 1)) % MOD

            return total

        return dp(0, 0, k)


class SolutionIterative:
    def ways(self, pizza: List[str], k: int) -> int:
        """Iterative DP"""
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])

        # Suffix sum of apples
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (1 if pizza[r][c] == 'A' else 0) + \
                               apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]

        # dp[r][c][cuts] = ways to cut pizza[r:][c:] into cuts pieces
        dp = [[[0] * (k + 1) for _ in range(cols)] for _ in range(rows)]

        # Base case: 1 piece
        for r in range(rows):
            for c in range(cols):
                dp[r][c][1] = 1 if apples[r][c] > 0 else 0

        # Fill for increasing number of cuts
        for cuts in range(2, k + 1):
            for r in range(rows):
                for c in range(cols):
                    if apples[r][c] == 0:
                        continue

                    total = 0

                    # Horizontal cuts
                    for nr in range(r + 1, rows):
                        if apples[r][c] - apples[nr][c] > 0:
                            total = (total + dp[nr][c][cuts - 1]) % MOD

                    # Vertical cuts
                    for nc in range(c + 1, cols):
                        if apples[r][c] - apples[r][nc] > 0:
                            total = (total + dp[r][nc][cuts - 1]) % MOD

                    dp[r][c][cuts] = total

        return dp[0][0][k]
