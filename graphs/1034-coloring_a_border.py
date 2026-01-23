#1034. Coloring A Border
#Medium
#
#You are given an m x n integer matrix grid, and three integers row, col,
#and color. Each value in the grid represents the color of the grid square
#at that location.
#
#Two squares belong to the same connected component if they have the same
#color and are next to each other in one of the 4 directions.
#
#The border of a connected component is all the squares in the connected
#component that are either on the boundary of the grid, or adjacent to a
#square that is not in the component.
#
#You should color the border of the connected component that contains the
#square grid[row][col] with the given color.
#
#Return the final grid.
#
#Example 1:
#Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
#Output: [[3,3],[3,2]]
#
#Example 2:
#Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
#Output: [[1,3,3],[2,3,3]]
#
#Example 3:
#Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
#Output: [[2,2,2],[2,1,2],[2,2,2]]
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 50
#    1 <= grid[i][j], color <= 1000
#    0 <= row < m
#    0 <= col < n

from typing import List
from collections import deque

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        """
        DFS to find connected component, identify border cells.
        A cell is border if it's on grid boundary or adjacent to different color.
        """
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        visited = set()
        borders = []

        def dfs(r, c):
            if (r, c) in visited:
                return True
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if grid[r][c] != original_color:
                return False

            visited.add((r, c))

            # Check all 4 neighbors
            is_border = False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not dfs(nr, nc):
                    is_border = True

            if is_border:
                borders.append((r, c))

            return True

        dfs(row, col)

        # Color the borders
        for r, c in borders:
            grid[r][c] = color

        return grid


class SolutionBFS:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        """BFS approach"""
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        visited = set()
        borders = []
        queue = deque([(row, col)])
        visited.add((row, col))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            is_border = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    is_border = True
                elif grid[nr][nc] != original:
                    is_border = True
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

            if is_border:
                borders.append((r, c))

        for r, c in borders:
            grid[r][c] = color

        return grid
