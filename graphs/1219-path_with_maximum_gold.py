#1219. Path with Maximum Gold
#Medium
#
#In a gold mine grid of size m x n, each cell in this mine has an integer
#representing the amount of gold in that cell, 0 if it is empty.
#
#Return the maximum amount of gold you can collect under the conditions:
#    Every time you are located in a cell you will collect all the gold in that cell.
#    From your position, you can walk one step to the left, right, up, or down.
#    You can't visit the same cell more than once.
#    Never visit a cell with 0 gold.
#    You can start and stop collecting gold from any position in the grid that
#    has some gold.
#
#Example 1:
#Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
#Output: 24
#Explanation:
#[[0,6,0],
# [5,8,7],
# [0,9,0]]
#Path to get the maximum gold, 9 -> 8 -> 7.
#
#Example 2:
#Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
#Output: 28
#Explanation:
#[[1,0,7],
# [2,0,6],
# [3,4,5],
# [0,3,0],
# [9,0,20]]
#Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 15
#    0 <= grid[i][j] <= 100
#    There are at most 25 cells containing gold.

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Backtracking: Try starting from each gold cell.
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            gold = grid[r][c]
            grid[r][c] = 0  # Mark as visited

            max_gold = 0
            for dr, dc in directions:
                max_gold = max(max_gold, dfs(r + dr, c + dc))

            grid[r][c] = gold  # Restore
            return gold + max_gold

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    result = max(result, dfs(i, j))

        return result


class SolutionBitmask:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Bitmask DP for small number of gold cells.
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find all gold cells
        gold_cells = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    gold_cells.append((i, j))

        if not gold_cells:
            return 0

        num_gold = len(gold_cells)
        cell_to_idx = {cell: idx for idx, cell in enumerate(gold_cells)}

        # Build adjacency for gold cells
        adjacent = [[] for _ in range(num_gold)]
        for idx, (r, c) in enumerate(gold_cells):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in cell_to_idx:
                    adjacent[idx].append(cell_to_idx[(nr, nc)])

        # DFS with bitmask
        def dfs(curr, visited):
            r, c = gold_cells[curr]
            gold = grid[r][c]
            max_additional = 0

            for next_idx in adjacent[curr]:
                if not (visited & (1 << next_idx)):
                    max_additional = max(max_additional,
                                        dfs(next_idx, visited | (1 << next_idx)))

            return gold + max_additional

        result = 0
        for start in range(num_gold):
            result = max(result, dfs(start, 1 << start))

        return result
