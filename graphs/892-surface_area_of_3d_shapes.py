#892. Surface Area of 3D Shapes
#Easy
#
#You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each
#value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
#
#After placing these cubes, you have decided to glue any directly adjacent cubes
#to each other, forming several irregular 3D shapes.
#
#Return the total surface area of the resulting shapes.
#
#Example 1:
#Input: grid = [[1,2],[3,4]]
#Output: 34
#
#Example 2:
#Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
#Output: 32
#
#Example 3:
#Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
#Output: 46
#
#Constraints:
#    n == grid.length == grid[i].length
#    1 <= n <= 50
#    0 <= grid[i][j] <= 50

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        """
        For each tower, surface area = 2 (top and bottom) + 4 * height (sides)
        Subtract hidden faces between adjacent towers.
        """
        n = len(grid)
        total = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    # Top and bottom
                    total += 2

                    # Four sides (subtract overlapping with neighbors)
                    # Up
                    up = grid[i - 1][j] if i > 0 else 0
                    total += max(grid[i][j] - up, 0)

                    # Down
                    down = grid[i + 1][j] if i < n - 1 else 0
                    total += max(grid[i][j] - down, 0)

                    # Left
                    left = grid[i][j - 1] if j > 0 else 0
                    total += max(grid[i][j] - left, 0)

                    # Right
                    right = grid[i][j + 1] if j < n - 1 else 0
                    total += max(grid[i][j] - right, 0)

        return total


class SolutionSubtract:
    """Calculate total then subtract hidden faces"""

    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total = 0
        hidden = 0

        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v > 0:
                    total += 2 + 4 * v

                    # Hidden faces with right neighbor
                    if j < n - 1:
                        hidden += 2 * min(v, grid[i][j + 1])

                    # Hidden faces with bottom neighbor
                    if i < n - 1:
                        hidden += 2 * min(v, grid[i + 1][j])

        return total - hidden
