#1260. Shift 2D Grid
#Easy
#
#Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
#In one shift operation:
#    Element at grid[i][j] moves to grid[i][j + 1].
#    Element at grid[i][n - 1] moves to grid[i + 1][0].
#    Element at grid[m - 1][n - 1] moves to grid[0][0].
#
#Return the 2D grid after applying shift operation k times.
#
#Example 1:
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
#Output: [[9,1,2],[3,4,5],[6,7,8]]
#
#Example 2:
#Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
#Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#
#Example 3:
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
#Output: [[1,2,3],[4,5,6],[7,8,9]]
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m <= 50
#    1 <= n <= 50
#    -1000 <= grid[i][j] <= 1000
#    0 <= k <= 100

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Flatten grid, rotate, rebuild.
        """
        m, n = len(grid), len(grid[0])
        total = m * n

        # Flatten
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # Rotate right by k
        k = k % total
        flat = flat[-k:] + flat[:-k]

        # Rebuild grid
        result = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(flat[i * n + j])
            result.append(row)

        return result


class SolutionIndex:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """Direct index calculation"""
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Current position in flattened array
                old_idx = i * n + j
                # New position after shift
                new_idx = (old_idx + k) % total
                # Convert back to 2D
                new_i, new_j = new_idx // n, new_idx % n
                result[new_i][new_j] = grid[i][j]

        return result
