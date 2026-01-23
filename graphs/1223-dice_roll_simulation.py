#1223. Dice Roll Simulation
#Hard
#
#A die simulator generates a random number from 1 to 6 for each roll. You
#introduced a constraint to the generator such that it cannot roll the number
#i more than rollMax[i] (1-indexed) consecutive times.
#
#Given an array of integers rollMax and an integer n, return the number of
#distinct sequences that can be obtained with exact n rolls. Since the answer
#may be too large, return it modulo 10^9 + 7.
#
#Two sequences are considered different if at least one element differs from each other.
#
#Example 1:
#Input: n = 2, rollMax = [1,1,2,2,2,3]
#Output: 34
#Explanation: There will be 2 rolls of die, if there are no constraints on the
#die, there are 6 * 6 = 36 possible combinations. In this case, looking at
#rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore
#sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
#
#Example 2:
#Input: n = 2, rollMax = [1,1,1,1,1,1]
#Output: 30
#
#Example 3:
#Input: n = 3, rollMax = [1,1,1,2,2,3]
#Output: 181
#
#Constraints:
#    1 <= n <= 5000
#    rollMax.length == 6
#    1 <= rollMax[i] <= 15

from typing import List
from functools import lru_cache

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        DP: dp[i][j][k] = number of sequences of length i,
                          ending with die face j,
                          with k consecutive j's at the end.
        """
        MOD = 10**9 + 7

        # dp[j][k] = sequences ending with face j, k consecutive
        # Start with 0 rolls
        max_consec = max(rollMax)
        dp = [[0] * (max_consec + 1) for _ in range(6)]

        # Base case: first roll
        for j in range(6):
            dp[j][1] = 1

        for roll in range(2, n + 1):
            new_dp = [[0] * (max_consec + 1) for _ in range(6)]

            for j in range(6):  # Current face
                # Sum of all sequences not ending with j
                total_others = sum(sum(dp[other]) for other in range(6) if other != j)
                new_dp[j][1] = total_others % MOD

                # Extend consecutive j's
                for k in range(2, rollMax[j] + 1):
                    new_dp[j][k] = dp[j][k - 1]

            dp = new_dp

        return sum(sum(row) for row in dp) % MOD


class SolutionMemo:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """Top-down DP with memoization"""
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(remaining, last_face, consecutive):
            if remaining == 0:
                return 1

            total = 0
            for face in range(6):
                if face == last_face:
                    if consecutive < rollMax[face]:
                        total += dp(remaining - 1, face, consecutive + 1)
                else:
                    total += dp(remaining - 1, face, 1)

            return total % MOD

        return dp(n, -1, 0)


class SolutionOptimized:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        Optimized: Track total count and subtract invalid sequences.
        """
        MOD = 10**9 + 7

        # dp[j][k] = sequences ending with j, k consecutive
        # Also track total sequences
        max_k = max(rollMax)

        # dp[face][consecutive_count]
        dp = [[0] * (max_k + 1) for _ in range(6)]
        total = 0

        # First roll
        for j in range(6):
            dp[j][1] = 1
        total = 6

        for _ in range(n - 1):
            new_dp = [[0] * (max_k + 1) for _ in range(6)]
            new_total = 0

            for j in range(6):
                # New sequences starting with face j (after different face)
                others = total - sum(dp[j])
                new_dp[j][1] = others % MOD

                # Extend consecutive
                for k in range(2, rollMax[j] + 1):
                    new_dp[j][k] = dp[j][k - 1]

                new_total += sum(new_dp[j])

            dp = new_dp
            total = new_total % MOD

        return total
