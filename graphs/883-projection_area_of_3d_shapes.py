#883. Projection Area of 3D Shapes
#Easy
#
#You are given an n x n grid where we place some 1 x 1 x 1 cubes that are
#axis-aligned with the x, y, and z axes.
#
#Each value v = grid[i][j] represents a tower of v cubes placed on top of the
#cell (i, j).
#
#We view the projection of these cubes onto the xy, yz, and zx planes.
#
#A projection is like a shadow, that maps our 3-dimensional figure to a
#2-dimensional plane. We are viewing the "shadow" when looking at the cubes
#from the top, the front, and the side.
#
#Return the total area of all three projections.
#
#Example 1:
#Input: grid = [[1,2],[3,4]]
#Output: 17
#Explanation: xy projection = 4, yz projection = max(1,3) + max(2,4) = 3+4 = 7
#zx projection = max(1,2) + max(3,4) = 2+4 = 6. Total = 4+7+6 = 17.
#
#Example 2:
#Input: grid = [[2]]
#Output: 5
#
#Example 3:
#Input: grid = [[1,0],[0,2]]
#Output: 8
#
#Constraints:
#    n == grid.length == grid[i].length
#    1 <= n <= 50
#    0 <= grid[i][j] <= 50

class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        """
        xy projection = count of non-zero cells
        yz projection = sum of max in each row
        zx projection = sum of max in each column
        """
        n = len(grid)

        # xy: top view (count non-zero)
        xy = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)

        # yz: front view (max in each row)
        yz = sum(max(row) for row in grid)

        # zx: side view (max in each column)
        zx = sum(max(grid[i][j] for i in range(n)) for j in range(n))

        return xy + yz + zx


class SolutionSinglePass:
    """Single pass through grid"""

    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        xy = 0
        row_max = [0] * n
        col_max = [0] * n

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])

        return xy + sum(row_max) + sum(col_max)


class SolutionZip:
    """Using zip for columns"""

    def projectionArea(self, grid: list[list[int]]) -> int:
        xy = sum(v > 0 for row in grid for v in row)
        yz = sum(max(row) for row in grid)
        zx = sum(max(col) for col in zip(*grid))

        return xy + yz + zx
