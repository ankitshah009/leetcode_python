#807. Max Increase to Keep City Skyline
#Medium
#
#There is a city composed of n x n blocks, where each block contains a single
#building shaped like a vertical square prism. You are given a 0-indexed n x n
#integer matrix grid where grid[r][c] represents the height of the building
#located in the block at row r and column c.
#
#A city's skyline is the outer contour formed by all the building when viewing
#the side of the city from a distance. The skyline from each cardinal direction
#north, east, south, and west may be different.
#
#We are allowed to increase the height of any number of buildings by any amount
#(the amount can be different per building). The height of a 0-height building
#can also be increased. However, increasing the height of a building should not
#affect the city's skyline from any cardinal direction.
#
#Return the maximum total sum that the height of the buildings can be increased
#by without changing the city's skyline from any cardinal direction.
#
#Example 1:
#Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
#Output: 35
#
#Example 2:
#Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
#Output: 0
#
#Constraints:
#    n == grid.length
#    n == grid[r].length
#    2 <= n <= 50
#    0 <= grid[r][c] <= 100

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        """
        Each building can increase to min(row_max, col_max).
        """
        n = len(grid)

        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]

        total_increase = 0
        for r in range(n):
            for c in range(n):
                max_height = min(row_max[r], col_max[c])
                total_increase += max_height - grid[r][c]

        return total_increase


class SolutionZip:
    """Using zip for column max"""

    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        return sum(
            min(row_max[r], col_max[c]) - grid[r][c]
            for r in range(len(grid))
            for c in range(len(grid[0]))
        )


class SolutionOneLine:
    """Compact one-liner"""

    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        rows, cols = [max(r) for r in grid], [max(c) for c in zip(*grid)]
        return sum(min(rows[i], cols[j]) - v for i, r in enumerate(grid) for j, v in enumerate(r))
