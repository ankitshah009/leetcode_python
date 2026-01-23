#1878. Get Biggest Three Rhombus Sums in a Grid
#Medium
#
#You are given an m x n integer matrix grid.
#
#A rhombus sum is the sum of the elements that form the border of a regular
#rhombus shape in grid. The rhombus must have the shape of a square rotated 45
#degrees with each of the corners centered in a grid cell.
#
#Return the biggest three distinct rhombus sums in the grid in descending
#order. If there are less than three distinct values, return all of them.
#
#Example 1:
#Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,60,2],[1,1,3,1,1]]
#Output: [228,216,211]
#
#Example 2:
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [20,9,8]
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 50
#    1 <= grid[i][j] <= 10^5

from typing import List
import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        """
        Enumerate all possible rhombus centers and sizes.
        """
        m, n = len(grid), len(grid[0])
        sums = set()

        # Single cells are rhombus of size 0
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])

        # For each center and size
        for i in range(m):
            for j in range(n):
                for size in range(1, min(i, m - 1 - i, j, n - 1 - j) + 1):
                    # Rhombus with center (i, j) and half-diagonal = size
                    total = 0

                    # Four edges of rhombus
                    for k in range(size):
                        # Top-right edge
                        total += grid[i - size + k][j + k]
                        # Right-bottom edge
                        total += grid[i + k][j + size - k]
                        # Bottom-left edge
                        total += grid[i + size - k][j - k]
                        # Left-top edge
                        total += grid[i - k][j - size + k]

                    sums.add(total)

        # Get top 3
        result = sorted(sums, reverse=True)
        return result[:3]


class SolutionPrefixSum:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        """
        Using diagonal prefix sums for O(1) rhombus sum queries.
        """
        m, n = len(grid), len(grid[0])

        # Diagonal prefix sums
        # diag1[i][j] = sum along i+j constant diagonal ending at (i,j)
        # diag2[i][j] = sum along i-j constant diagonal ending at (i,j)
        diag1 = [[0] * n for _ in range(m)]
        diag2 = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diag1[i][j] = grid[i][j]
                diag2[i][j] = grid[i][j]
                if i > 0 and j > 0:
                    diag1[i][j] += diag1[i-1][j-1]
                if i > 0 and j < n - 1:
                    diag2[i][j] += diag2[i-1][j+1]

        def get_diag1_sum(r1, c1, r2, c2):
            """Sum from (r1,c1) to (r2,c2) along i+j=const diagonal."""
            result = diag1[r2][c2]
            if r1 > 0 and c1 > 0:
                result -= diag1[r1-1][c1-1]
            return result

        def get_diag2_sum(r1, c1, r2, c2):
            """Sum from (r1,c1) to (r2,c2) along i-j=const diagonal."""
            result = diag2[r2][c2]
            if r1 > 0 and c1 < n - 1:
                result -= diag2[r1-1][c1+1]
            return result

        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])

                for s in range(1, min(i, m-1-i, j, n-1-j) + 1):
                    # Corners: top(i-s,j), right(i,j+s), bottom(i+s,j), left(i,j-s)
                    total = (get_diag1_sum(i-s, j, i, j+s) +
                             get_diag2_sum(i, j+s, i+s, j) +
                             get_diag1_sum(i, j-s, i+s, j) +
                             get_diag2_sum(i-s, j, i, j-s))
                    # Subtract corners counted twice
                    total -= (grid[i-s][j] + grid[i][j+s] +
                              grid[i+s][j] + grid[i][j-s])
                    sums.add(total)

        return sorted(sums, reverse=True)[:3]
