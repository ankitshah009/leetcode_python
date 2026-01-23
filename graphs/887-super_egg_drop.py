#887. Super Egg Drop
#Hard
#
#You are given k identical eggs and you have access to a building with n floors
#labeled from 1 to n.
#
#You know that there exists a floor f where 0 <= f <= n such that any egg
#dropped at a floor higher than f will break, and any egg dropped at or below
#floor f will not break.
#
#Each move, you may take an unbroken egg and drop it from any floor x (where
#1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg
#does not break, you may reuse it in future moves.
#
#Return the minimum number of moves that you need to determine with certainty
#what the value of f is.
#
#Example 1:
#Input: k = 1, n = 2
#Output: 2
#
#Example 2:
#Input: k = 2, n = 6
#Output: 3
#
#Example 3:
#Input: k = 3, n = 14
#Output: 4
#
#Constraints:
#    1 <= k <= 100
#    1 <= n <= 10^4

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        DP with optimization: dp[m][k] = max floors checkable with m moves, k eggs.
        dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1
        (if egg breaks + if egg doesn't break + current floor)
        """
        # dp[j] = max floors with current moves and j eggs
        dp = [0] * (k + 1)

        moves = 0
        while dp[k] < n:
            moves += 1
            # Update from right to left to avoid overwriting
            for j in range(k, 0, -1):
                dp[j] = dp[j - 1] + dp[j] + 1

        return moves


class SolutionBinarySearch:
    """Binary search optimization"""

    def superEggDrop(self, k: int, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(eggs, floors):
            if floors == 0:
                return 0
            if eggs == 1:
                return floors

            # Binary search for optimal floor
            lo, hi = 1, floors
            while lo < hi:
                mid = (lo + hi) // 2
                broke = dp(eggs - 1, mid - 1)  # Egg breaks
                survived = dp(eggs, floors - mid)  # Egg survives

                if broke < survived:
                    lo = mid + 1
                else:
                    hi = mid

            # Check both lo and hi
            return 1 + max(dp(eggs - 1, lo - 1), dp(eggs, floors - lo))

        return dp(k, n)


class SolutionMath:
    """Mathematical approach: find minimum m where C(m,1) + C(m,2) + ... + C(m,k) >= n"""

    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i] = max floors checkable with m moves and i eggs
        def max_floors(m, k):
            total = 0
            c = 1  # C(m, i)
            for i in range(1, min(m, k) + 1):
                c = c * (m - i + 1) // i
                total += c
            return total

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if max_floors(mid, k) < n:
                lo = mid + 1
            else:
                hi = mid

        return lo
