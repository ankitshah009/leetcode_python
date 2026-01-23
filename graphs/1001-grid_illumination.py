#1001. Grid Illumination
#Hard
#
#There is a 2D grid of size n x n where each cell of this grid has a lamp that
#is initially turned off.
#
#You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli]
#indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp
#is listed more than once, it is turned on.
#
#When a lamp is turned on, it illuminates its cell and all other cells in the
#same row, column, or diagonal.
#
#You are also given another 2D array queries, where queries[j] = [rowj, colj].
#For the j-th query, determine whether grid[rowj][colj] is illuminated or not.
#After answering the j-th query, turn off the lamp at grid[rowj][colj] and its
#8 adjacent lamps if they are on.
#
#Return an array of integers ans, where ans[j] should be 1 if the cell is
#illuminated, or 0 if not.
#
#Constraints:
#    1 <= n <= 10^9
#    0 <= lamps.length <= 20000
#    0 <= queries.length <= 20000
#    lamps[i].length == 2
#    0 <= rowi, coli < n
#    queries[j].length == 2
#    0 <= rowj, colj < n

from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        Track lamp counts for rows, columns, and diagonals.
        """
        rows = defaultdict(int)
        cols = defaultdict(int)
        diag1 = defaultdict(int)  # r - c
        diag2 = defaultdict(int)  # r + c
        lamp_set = set()

        # Turn on lamps
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))
                rows[r] += 1
                cols[c] += 1
                diag1[r - c] += 1
                diag2[r + c] += 1

        result = []
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        for r, c in queries:
            # Check if illuminated
            if rows[r] > 0 or cols[c] > 0 or diag1[r - c] > 0 or diag2[r + c] > 0:
                result.append(1)
            else:
                result.append(0)

            # Turn off lamps in 3x3 neighborhood
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if (nr, nc) in lamp_set:
                    lamp_set.remove((nr, nc))
                    rows[nr] -= 1
                    cols[nc] -= 1
                    diag1[nr - nc] -= 1
                    diag2[nr + nc] -= 1

        return result


class SolutionClean:
    """Cleaner implementation"""

    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        from collections import Counter

        lamps_on = set()
        row_count = Counter()
        col_count = Counter()
        diag_count = Counter()
        anti_diag_count = Counter()

        for r, c in lamps:
            if (r, c) not in lamps_on:
                lamps_on.add((r, c))
                row_count[r] += 1
                col_count[c] += 1
                diag_count[r - c] += 1
                anti_diag_count[r + c] += 1

        def is_lit(r, c):
            return row_count[r] or col_count[c] or diag_count[r - c] or anti_diag_count[r + c]

        def turn_off(r, c):
            if (r, c) in lamps_on:
                lamps_on.remove((r, c))
                row_count[r] -= 1
                col_count[c] -= 1
                diag_count[r - c] -= 1
                anti_diag_count[r + c] -= 1

        result = []
        for r, c in queries:
            result.append(1 if is_lit(r, c) else 0)

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    turn_off(r + dr, c + dc)

        return result
