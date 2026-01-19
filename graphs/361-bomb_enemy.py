#361. Bomb Enemy
#Medium
#
#Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E'
#or empty '0', return the maximum enemies you can kill using one bomb. You can
#only place the bomb in an empty cell.
#
#The bomb kills all the enemies in the same row and column from the planted
#point until it hits the wall since it is too strong to be destroyed.
#
#Example 1:
#Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
#Output: 3
#
#Example 2:
#Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
#Output: 1
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 500
#    grid[i][j] is either 'W', 'E', or '0'.

from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
        O(mn) solution with row caching.
        Only recalculate row count when hitting a wall or at start.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_kills = 0
        row_kills = 0
        col_kills = [0] * n

        for i in range(m):
            for j in range(n):
                # Recalculate row kills if at start of row or after wall
                if j == 0 or grid[i][j - 1] == 'W':
                    row_kills = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            row_kills += 1

                # Recalculate col kills if at start of col or after wall
                if i == 0 or grid[i - 1][j] == 'W':
                    col_kills[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            col_kills[j] += 1

                # Update max if current cell is empty
                if grid[i][j] == '0':
                    max_kills = max(max_kills, row_kills + col_kills[j])

        return max_kills


class SolutionBruteForce:
    """O(mn(m+n)) brute force - for reference"""

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_kills = 0

        def count_kills(row, col):
            kills = 0
            # Count in all 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                while 0 <= r < m and 0 <= c < n and grid[r][c] != 'W':
                    if grid[r][c] == 'E':
                        kills += 1
                    r += dr
                    c += dc
            return kills

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    max_kills = max(max_kills, count_kills(i, j))

        return max_kills


class SolutionPrecompute:
    """Precompute kills in all 4 directions"""

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        # Precompute enemies killed from each direction
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'W':
                    left[i][j] = (1 if grid[i][j] == 'E' else 0) + (left[i][j-1] if j > 0 else 0)

            for j in range(n - 1, -1, -1):
                if grid[i][j] != 'W':
                    right[i][j] = (1 if grid[i][j] == 'E' else 0) + (right[i][j+1] if j < n-1 else 0)

        for j in range(n):
            for i in range(m):
                if grid[i][j] != 'W':
                    up[i][j] = (1 if grid[i][j] == 'E' else 0) + (up[i-1][j] if i > 0 else 0)

            for i in range(m - 1, -1, -1):
                if grid[i][j] != 'W':
                    down[i][j] = (1 if grid[i][j] == 'E' else 0) + (down[i+1][j] if i < m-1 else 0)

        max_kills = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    kills = left[i][j] + right[i][j] + up[i][j] + down[i][j]
                    max_kills = max(max_kills, kills)

        return max_kills
