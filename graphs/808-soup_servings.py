#808. Soup Servings
#Medium
#
#There are two types of soup: type A and type B. Initially, we have n ml of each
#type of soup. There are four kinds of operations:
#1. Serve 100 ml of soup A and 0 ml of soup B,
#2. Serve 75 ml of soup A and 25 ml of soup B,
#3. Serve 50 ml of soup A and 50 ml of soup B,
#4. Serve 25 ml of soup A and 75 ml of soup B.
#
#When we serve some soup, we give it to someone, and we no longer have it.
#Each turn, we will choose from the four operations with an equal probability
#0.25. If the remaining volume of soup is not enough to complete the operation,
#we will serve as much as possible. We stop once we no longer have some quantity
#of both types of soup.
#
#Note that we do not have an operation where all 100 ml's of soup B are used first.
#
#Return the probability that soup A will be empty first, plus half the
#probability that A and B become empty at the same time.
#
#Example 1:
#Input: n = 50
#Output: 0.62500
#
#Example 2:
#Input: n = 100
#Output: 0.71875
#
#Constraints:
#    0 <= n <= 10^9

class Solution:
    def soupServings(self, n: int) -> float:
        """
        Use units of 25ml. Operations become: (4,0), (3,1), (2,2), (1,3)
        A is used more on average (2.5 vs 1.5 units per turn).
        For large n, probability approaches 1.
        """
        # For large n, probability is very close to 1
        if n >= 4800:
            return 1.0

        # Convert to units of 25ml (ceiling)
        n = (n + 24) // 25

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(a, b):
            """Probability that A empties first + 0.5 * P(both empty)"""
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(n, n)


class SolutionIterative:
    """Bottom-up DP"""

    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0

        n = (n + 24) // 25

        # dp[a][b] = probability
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]

        # Base cases handled in recurrence
        for a in range(n + 1):
            for b in range(n + 1):
                if a == 0 and b == 0:
                    dp[0][0] = 0.5
                elif a == 0:
                    dp[0][b] = 1.0
                elif b == 0:
                    dp[a][0] = 0.0
                else:
                    prob = 0
                    for da, db in [(4, 0), (3, 1), (2, 2), (1, 3)]:
                        na, nb = max(0, a - da), max(0, b - db)
                        prob += dp[na][nb]
                    dp[a][b] = prob * 0.25

        return dp[n][n]
