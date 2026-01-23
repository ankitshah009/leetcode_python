#1659. Maximize Grid Happiness
#Hard
#
#You are given four integers, m, n, introvertsCount, and extrovertsCount. You
#have an m x n grid, and there are two types of people: introverts and extroverts.
#There are introvertsCount introverts and extrovertsCount extroverts.
#
#You should decide how many people you want to live in the grid and assign each
#of them one grid cell. Note that you do not have to have all the people living
#in the grid.
#
#The happiness of each person is calculated as follows:
#- Introverts start with 120 happiness and lose 30 happiness for each neighbor.
#- Extroverts start with 40 happiness and gain 20 happiness for each neighbor.
#- Neighbors live in the directly adjacent cells north, east, south, and west.
#
#The grid happiness is the sum of each person's happiness. Return the maximum
#possible grid happiness.
#
#Example 1:
#Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
#Output: 240
#
#Example 2:
#Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
#Output: 260
#
#Example 3:
#Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
#Output: 240
#
#Constraints:
#    1 <= m, n <= 5
#    0 <= introvertsCount, extrovertsCount <= min(m * n, 6)

from functools import lru_cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int,
                           extrovertsCount: int) -> int:
        """
        DP with bitmask for previous row state.
        State: (cell_idx, introverts_left, extroverts_left, prev_row_state)
        prev_row_state: base-3 number where 0=empty, 1=introvert, 2=extrovert
        """
        # Precompute cost changes
        # When placing type1 next to type2
        # Returns (delta for type1, delta for type2)
        def neighbor_cost(type1: int, type2: int) -> int:
            if type1 == 0 or type2 == 0:
                return 0

            cost = 0
            # Effect on type1
            if type1 == 1:  # Introvert
                cost -= 30
            else:  # Extrovert
                cost += 20

            # Effect on type2
            if type2 == 1:  # Introvert
                cost -= 30
            else:  # Extrovert
                cost += 20

            return cost

        @lru_cache(maxsize=None)
        def dp(pos: int, intro: int, extro: int, prev_row: tuple) -> int:
            if pos == m * n:
                return 0

            row, col = divmod(pos, n)

            # Convert prev_row tuple to list for manipulation
            new_row = list(prev_row[1:]) + [0]

            best = dp(pos + 1, intro, extro, tuple(new_row))  # Skip cell

            # Try placing introvert
            if intro > 0:
                new_row[-1] = 1
                happiness = 120

                # Check neighbor above (prev_row[col])
                if row > 0:
                    happiness += neighbor_cost(1, prev_row[col])

                # Check neighbor to the left
                if col > 0 and len(prev_row) >= n:
                    left_type = new_row[-2] if len(new_row) >= 2 else 0
                    happiness += neighbor_cost(1, left_type)

                best = max(best, happiness + dp(pos + 1, intro - 1, extro, tuple(new_row)))
                new_row[-1] = 0

            # Try placing extrovert
            if extro > 0:
                new_row[-1] = 2
                happiness = 40

                # Check neighbor above
                if row > 0:
                    happiness += neighbor_cost(2, prev_row[col])

                # Check neighbor to the left
                if col > 0 and len(new_row) >= 2:
                    left_type = new_row[-2]
                    happiness += neighbor_cost(2, left_type)

                best = max(best, happiness + dp(pos + 1, intro, extro - 1, tuple(new_row)))

            return best

        initial_row = tuple([0] * n)
        return dp(0, introvertsCount, extrovertsCount, initial_row)


class SolutionOptimized:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int,
                           extrovertsCount: int) -> int:
        """
        Optimized with base-3 encoding.
        """
        if introvertsCount == 0 and extrovertsCount == 0:
            return 0

        # Precompute powers of 3
        pow3 = [3 ** i for i in range(n)]

        def get_cell(mask: int, pos: int) -> int:
            return (mask // pow3[pos]) % 3

        def set_cell(mask: int, pos: int, val: int) -> int:
            old_val = get_cell(mask, pos)
            return mask - old_val * pow3[pos] + val * pow3[pos]

        # Cost when placing person of type t
        BASE = {0: 0, 1: 120, 2: 40}
        # Cost change when two neighbors interact
        NEIGHBOR = [[0, 0, 0], [0, -60, -10], [0, -10, 40]]

        @lru_cache(maxsize=None)
        def dp(pos: int, intro: int, extro: int, mask: int) -> int:
            if pos == m * n:
                return 0

            row, col = divmod(pos, n)

            # Shift mask for new row
            above = get_cell(mask, col)
            left = get_cell(mask, (col - 1) % n) if col > 0 else 0

            # Option 1: Leave empty
            new_mask = set_cell(mask, col, 0)
            best = dp(pos + 1, intro, extro, new_mask)

            # Option 2: Place introvert
            if intro > 0:
                new_mask = set_cell(mask, col, 1)
                gain = BASE[1]
                if row > 0:
                    gain += NEIGHBOR[1][above]
                if col > 0:
                    gain += NEIGHBOR[1][left]
                best = max(best, gain + dp(pos + 1, intro - 1, extro, new_mask))

            # Option 3: Place extrovert
            if extro > 0:
                new_mask = set_cell(mask, col, 2)
                gain = BASE[2]
                if row > 0:
                    gain += NEIGHBOR[2][above]
                if col > 0:
                    gain += NEIGHBOR[2][left]
                best = max(best, gain + dp(pos + 1, intro, extro - 1, new_mask))

            return best

        return dp(0, introvertsCount, extrovertsCount, 0)
