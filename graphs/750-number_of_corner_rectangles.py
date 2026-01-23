#750. Number of Corner Rectangles
#Medium
#
#Given an m x n integer matrix grid where each entry is only 0 or 1, return the
#number of corner rectangles.
#
#A corner rectangle is 4 distinct 1s on the grid that forms an axis-aligned
#rectangle. Note that only the corners need to have the value 1. Also, all four
#1s used must be distinct.
#
#Example 1:
#Input: grid = [[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]]
#Output: 1
#Explanation: There is only one corner rectangle, with corners grid[1][2],
#grid[1][4], grid[3][2], grid[3][4].
#
#Example 2:
#Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
#Output: 9
#Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and
#one 3x3 rectangle.
#
#Example 3:
#Input: grid = [[1,1,1,1]]
#Output: 0
#Explanation: Rectangles must have 4 distinct corners.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 200
#    grid[i][j] is either 0 or 1.
#    The number of 1s in the grid is in the range [1, 6000].

class Solution:
    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        """
        For each pair of rows, count columns that have 1s in both rows.
        Number of rectangles from k matching columns = k*(k-1)/2
        """
        m, n = len(grid), len(grid[0])
        count = 0

        for r1 in range(m):
            for r2 in range(r1 + 1, m):
                # Count columns with 1s in both rows
                matching = 0
                for c in range(n):
                    if grid[r1][c] == 1 and grid[r2][c] == 1:
                        matching += 1

                # Number of rectangles from k columns = C(k, 2)
                count += matching * (matching - 1) // 2

        return count


class SolutionOptimized:
    """Optimized with column pair counting"""

    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        from collections import Counter

        m, n = len(grid), len(grid[0])
        count = 0
        pair_count = Counter()

        for row in grid:
            # Find all 1s in this row
            ones = [c for c in range(n) if row[c] == 1]

            # For each pair of columns with 1s
            for i in range(len(ones)):
                for j in range(i + 1, len(ones)):
                    pair = (ones[i], ones[j])
                    count += pair_count[pair]
                    pair_count[pair] += 1

        return count


class SolutionPrecompute:
    """Precompute column positions for efficiency"""

    def countCornerRectangles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # For each row, store positions of 1s
        ones = []
        for row in grid:
            ones.append([c for c in range(n) if row[c] == 1])

        count = 0

        for r1 in range(m):
            for r2 in range(r1 + 1, m):
                # Find common columns
                i, j = 0, 0
                matching = 0
                while i < len(ones[r1]) and j < len(ones[r2]):
                    if ones[r1][i] == ones[r2][j]:
                        matching += 1
                        i += 1
                        j += 1
                    elif ones[r1][i] < ones[r2][j]:
                        i += 1
                    else:
                        j += 1

                count += matching * (matching - 1) // 2

        return count
