#957. Prison Cells After N Days
#Medium
#
#There are 8 prison cells in a row and each cell is either occupied or vacant.
#
#Each day, whether the cell is occupied or vacant changes according to:
#- If a cell has two adjacent neighbors that are both occupied or both vacant,
#  then the cell becomes occupied.
#- Otherwise, it becomes vacant.
#
#Note that the first and last cells don't have two adjacent neighbors.
#
#Return the state of the prison after n days.
#
#Example 1:
#Input: cells = [0,1,0,1,1,0,0,1], n = 7
#Output: [0,0,1,1,0,0,0,0]
#
#Example 2:
#Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
#Output: [0,0,1,1,1,1,1,0]
#
#Constraints:
#    cells.length == 8
#    cells[i] is either 0 or 1.
#    1 <= n <= 10^9

class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        """
        Find cycle and compute final state.
        """
        def next_day(state: tuple) -> tuple:
            new = [0] * 8
            for i in range(1, 7):
                new[i] = 1 if state[i - 1] == state[i + 1] else 0
            return tuple(new)

        seen = {}
        state = tuple(cells)

        for day in range(n):
            if state in seen:
                # Found cycle
                cycle_length = day - seen[state]
                remaining = (n - day) % cycle_length
                for _ in range(remaining):
                    state = next_day(state)
                return list(state)

            seen[state] = day
            state = next_day(state)

        return list(state)


class SolutionBitmask:
    """Using bitmask for state"""

    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        def cells_to_int(cells):
            return sum(c << i for i, c in enumerate(cells))

        def int_to_cells(x):
            return [(x >> i) & 1 for i in range(8)]

        def next_state(x):
            # New state: bit i is 1 if bits i-1 and i+1 are equal
            # For cells 1-6 only (0 and 7 always become 0)
            result = 0
            for i in range(1, 7):
                left = (x >> (i - 1)) & 1
                right = (x >> (i + 1)) & 1
                if left == right:
                    result |= (1 << i)
            return result

        state = cells_to_int(cells)
        seen = {}

        for day in range(n):
            if state in seen:
                cycle = day - seen[state]
                remaining = (n - day) % cycle
                for _ in range(remaining):
                    state = next_state(state)
                return int_to_cells(state)

            seen[state] = day
            state = next_state(state)

        return int_to_cells(state)


class SolutionFastCycle:
    """Cycle is always 14 after first day"""

    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        def next_day(cells):
            return [0] + [1 if cells[i-1] == cells[i+1] else 0 for i in range(1, 7)] + [0]

        # After first day, first and last are always 0
        # Cycle length is always 14
        cells = next_day(cells)
        n -= 1

        n %= 14
        for _ in range(n):
            cells = next_day(cells)

        return cells
