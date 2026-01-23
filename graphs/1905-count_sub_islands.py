#1905. Count Sub Islands
#Medium
#
#You are given two m x n binary matrices grid1 and grid2 containing only 0's
#(representing water) and 1's (representing land). An island is a group of 1's
#connected 4-directionally (horizontal or vertical). Any cells outside of the
#grid are considered water cells.
#
#An island in grid2 is considered a sub-island if there is an island in grid1
#that contains all the cells that make up this island in grid2.
#
#Return the number of islands in grid2 that are considered sub-islands.
#
#Example 1:
#Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
#       grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
#Output: 3
#
#Example 2:
#Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
#       grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
#Output: 2
#
#Constraints:
#    m == grid1.length == grid2.length
#    n == grid1[i].length == grid2[i].length
#    1 <= m, n <= 500
#    grid1[i][j] and grid2[i][j] are either 0 or 1.

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        DFS on grid2, check if all cells are land in grid1.
        """
        m, n = len(grid1), len(grid1[0])

        def dfs(i: int, j: int) -> bool:
            """Return True if this island in grid2 is a sub-island of grid1."""
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True

            # Mark as visited
            grid2[i][j] = 0

            # Check if this cell is land in grid1
            is_sub = grid1[i][j] == 1

            # Explore all neighbors (must check all, even if not sub)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not dfs(i + di, j + dj):
                    is_sub = False

            return is_sub

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1

        return count


class SolutionBFS:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        BFS approach.
        """
        from collections import deque

        m, n = len(grid1), len(grid1[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    # BFS to explore island
                    queue = deque([(i, j)])
                    grid2[i][j] = 0
                    is_sub = True

                    while queue:
                        x, y = queue.popleft()

                        if grid1[x][y] == 0:
                            is_sub = False

                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                                grid2[nx][ny] = 0
                                queue.append((nx, ny))

                    if is_sub:
                        count += 1

        return count
