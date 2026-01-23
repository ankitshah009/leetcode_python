#1139. Largest 1-Bordered Square
#Medium
#
#Given a 2D grid of 0s and 1s, return the number of elements in the largest
#square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
#exist in the grid.
#
#Example 1:
#Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
#Output: 9
#
#Example 2:
#Input: grid = [[1,1,0,0]]
#Output: 1
#
#Constraints:
#    1 <= grid.length <= 100
#    1 <= grid[0].length <= 100
#    grid[i][j] is 0 or 1

from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        Precompute consecutive 1s going right and down from each cell.
        For each cell, check if it can be top-left of a k x k bordered square.
        """
        m, n = len(grid), len(grid[0])

        # right[i][j] = consecutive 1s starting at (i,j) going right
        # down[i][j] = consecutive 1s starting at (i,j) going down
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = (right[i][j + 1] if j + 1 < n else 0) + 1
                    down[i][j] = (down[i + 1][j] if i + 1 < m else 0) + 1

        # Find largest bordered square
        max_side = 0

        for i in range(m):
            for j in range(n):
                # Maximum possible side starting at (i, j)
                max_k = min(right[i][j], down[i][j])

                for k in range(max_k, max_side, -1):
                    # Check bottom-left and top-right corners
                    # Bottom-left: (i+k-1, j) should have k going right
                    # Top-right: (i, j+k-1) should have k going down
                    if right[i + k - 1][j] >= k and down[i][j + k - 1] >= k:
                        max_side = k
                        break

        return max_side * max_side


class SolutionBruteForce:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """Check each possible square directly"""
        m, n = len(grid), len(grid[0])

        def is_bordered(r, c, k):
            # Check all 4 sides
            for i in range(k):
                if grid[r][c + i] == 0:  # Top
                    return False
                if grid[r + k - 1][c + i] == 0:  # Bottom
                    return False
                if grid[r + i][c] == 0:  # Left
                    return False
                if grid[r + i][c + k - 1] == 0:  # Right
                    return False
            return True

        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_bordered(i, j, k):
                        return k * k

        return 0
