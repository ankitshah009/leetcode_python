#799. Champagne Tower
#Medium
#
#We stack glasses in a pyramid, where the first row has 1 glass, the second row
#has 2 glasses, and so on until the 100th row. Each glass holds one cup of
#champagne.
#
#Then, some champagne is poured into the first glass at the top. When the
#topmost glass is full, any excess liquid poured will fall equally to the glass
#immediately to the left and right of it. When those glasses become full, any
#excess champagne will fall equally to the left and right of those glasses, and
#so on. (A glass at the bottom row has its excess champagne fall on the floor.)
#
#Now after pouring some non-negative integer cups of champagne, return how full
#the jth glass in the ith row is (both i and j are 0-indexed.)
#
#Example 1:
#Input: poured = 1, query_row = 1, query_glass = 1
#Output: 0.00000
#Explanation: We poured 1 cup into glass (0, 0) which was already full.
#
#Example 2:
#Input: poured = 2, query_row = 1, query_glass = 1
#Output: 0.50000
#Explanation: Glass (0, 0) overflows by 1 cup, split to (1, 0) and (1, 1).
#
#Example 3:
#Input: poured = 100000009, query_row = 33, query_glass = 17
#Output: 1.00000
#
#Constraints:
#    0 <= poured <= 10^9
#    0 <= query_glass <= query_row < 100

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Simulate the flow row by row.
        Track total liquid that reached each glass (can exceed 1).
        """
        # dp[j] = total liquid at glass j in current row
        dp = [poured]

        for row in range(1, query_row + 1):
            new_dp = [0.0] * (row + 1)

            for j in range(row):
                if dp[j] > 1:
                    overflow = dp[j] - 1
                    new_dp[j] += overflow / 2
                    new_dp[j + 1] += overflow / 2

            dp = new_dp

        return min(1.0, dp[query_glass])


class SolutionFullSimulation:
    """Full 2D simulation"""

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(row + 1):
                if tower[row][glass] > 1:
                    excess = tower[row][glass] - 1
                    tower[row + 1][glass] += excess / 2
                    tower[row + 1][glass + 1] += excess / 2

        return min(1.0, tower[query_row][query_glass])


class SolutionMemo:
    """Memoized recursive solution"""

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def flow(row, glass):
            """Total champagne that flowed into glass (row, glass)"""
            if row == 0 and glass == 0:
                return poured
            if glass < 0 or glass > row:
                return 0

            # From above-left glass
            left = max(0, flow(row - 1, glass - 1) - 1) / 2 if glass > 0 else 0
            # From above-right glass
            right = max(0, flow(row - 1, glass) - 1) / 2 if glass < row else 0

            return left + right

        return min(1.0, flow(query_row, query_glass))
