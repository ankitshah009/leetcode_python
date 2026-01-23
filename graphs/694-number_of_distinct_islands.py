#694. Number of Distinct Islands
#Medium
#
#You are given an m x n binary matrix grid. An island is a group of 1's
#(representing land) connected 4-directionally (horizontal or vertical.)
#You may assume all four edges of the grid are surrounded by water.
#
#An island is considered to be the same as another if and only if one island
#can be translated (and not rotated or reflected) to equal the other.
#
#Return the number of distinct islands.
#
#Example 1:
#Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
#Output: 1
#
#Example 2:
#Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
#Output: 3
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 50
#    grid[i][j] is either 0 or 1.

class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        """
        DFS to find islands, normalize by translating to origin.
        Store shapes in a set.
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()
        shapes = set()

        def dfs(r, c, origin_r, origin_c, shape):
            if (r < 0 or r >= m or c < 0 or c >= n or
                grid[r][c] == 0 or (r, c) in visited):
                return

            visited.add((r, c))
            # Store relative position to origin
            shape.append((r - origin_r, c - origin_c))

            dfs(r + 1, c, origin_r, origin_c, shape)
            dfs(r - 1, c, origin_r, origin_c, shape)
            dfs(r, c + 1, origin_r, origin_c, shape)
            dfs(r, c - 1, origin_r, origin_c, shape)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []
                    dfs(i, j, i, j, shape)
                    shapes.add(tuple(shape))

        return len(shapes)


class SolutionPathSignature:
    """Use path signature instead of coordinates"""

    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()
        shapes = set()

        def dfs(r, c, direction):
            if (r < 0 or r >= m or c < 0 or c >= n or
                grid[r][c] == 0 or (r, c) in visited):
                return ""

            visited.add((r, c))

            # Record the path
            path = direction
            path += dfs(r + 1, c, "D")  # Down
            path += dfs(r - 1, c, "U")  # Up
            path += dfs(r, c + 1, "R")  # Right
            path += dfs(r, c - 1, "L")  # Left
            path += "B"  # Backtrack marker

            return path

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = dfs(i, j, "S")  # Start
                    shapes.add(shape)

        return len(shapes)


class SolutionBFS:
    """BFS approach with coordinate normalization"""

    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        from collections import deque

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()
        shapes = set()

        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            visited.add((start_r, start_c))
            shape = []

            while queue:
                r, c = queue.popleft()
                shape.append((r - start_r, c - start_c))

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return tuple(sorted(shape))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = bfs(i, j)
                    shapes.add(shape)

        return len(shapes)
