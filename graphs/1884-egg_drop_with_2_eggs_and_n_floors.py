#1884. Egg Drop With 2 Eggs and N Floors
#Medium
#
#You are given two identical eggs and you have access to a building with n
#floors labeled from 1 to n.
#
#You know that there exists a floor f where 0 <= f <= n such that any egg
#dropped at a floor higher than f will break, and any egg dropped at or below
#floor f will not break.
#
#In each move, you can take an unbroken egg and drop it from any floor x
#(where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if
#the egg does not break, you may reuse it in future moves.
#
#Return the minimum number of moves that you need to determine with certainty
#what the value of f is.
#
#Example 1:
#Input: n = 2
#Output: 2
#
#Example 2:
#Input: n = 100
#Output: 14
#
#Constraints:
#    1 <= n <= 1000

class Solution:
    def twoEggDrop(self, n: int) -> int:
        """
        Math: with k moves and 2 eggs, we can cover at most k + (k-1) + ... + 1
        = k*(k+1)/2 floors.

        Find minimum k where k*(k+1)/2 >= n.
        """
        k = 1
        while k * (k + 1) // 2 < n:
            k += 1
        return k


class SolutionDP:
    def twoEggDrop(self, n: int) -> int:
        """
        DP approach: dp[e][f] = min moves with e eggs and f floors.
        """
        # dp[f] = min moves with 2 eggs for f floors
        dp = list(range(n + 1))  # With 1 egg, need f moves for f floors

        # With 2 eggs
        for f in range(1, n + 1):
            for x in range(1, f + 1):
                # Drop from floor x:
                # - Breaks: 1 egg, x-1 floors below = x-1 moves
                # - Doesn't break: 2 eggs, f-x floors above = dp[f-x] moves
                moves = 1 + max(x - 1, dp[f - x])
                dp[f] = min(dp[f], moves)

        return dp[n]


class SolutionFormula:
    def twoEggDrop(self, n: int) -> int:
        """
        Direct formula using quadratic equation.
        k*(k+1)/2 >= n
        k^2 + k - 2n >= 0
        k = (-1 + sqrt(1 + 8n)) / 2
        """
        import math
        return math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)


class SolutionRecursive:
    def twoEggDrop(self, n: int) -> int:
        """
        Recursive with memoization.
        """
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(eggs: int, floors: int) -> int:
            if floors <= 1:
                return floors
            if eggs == 1:
                return floors

            min_moves = floors  # Worst case with 1 egg

            for x in range(1, floors + 1):
                # Drop from floor x
                breaks = dp(eggs - 1, x - 1)  # Check floors below
                survives = dp(eggs, floors - x)  # Check floors above
                moves = 1 + max(breaks, survives)
                min_moves = min(min_moves, moves)

            return min_moves

        return dp(2, n)
