#934. Shortest Bridge
#Medium
#
#You are given an n x n binary matrix grid where 1 represents land and 0
#represents water.
#
#An island is a 4-directionally connected group of 1's not connected to any
#other 1's. There are exactly two islands in grid.
#
#Return the smallest number of 0's you must flip to connect the two islands.
#
#Example 1:
#Input: grid = [[0,1],[1,0]]
#Output: 1
#
#Example 2:
#Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
#Output: 2
#
#Example 3:
#Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
#Output: 1
#
#Constraints:
#    n == grid.length == grid[i].length
#    2 <= n <= 100
#    grid[i][j] is either 0 or 1.
#    There are exactly two islands in grid.

from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        """
        DFS to find first island, BFS to expand until reaching second island.
        """
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find first island using DFS
        def dfs(r, c, island):
            if r < 0 or r >= n or c < 0 or c >= n:
                return
            if grid[r][c] != 1:
                return

            grid[r][c] = 2  # Mark as visited
            island.append((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, island)

        # Find starting point of first island
        island = []
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, island)
                    found = True
                    break

        # BFS to expand first island
        queue = deque(island)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:  # Found second island
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))

            steps += 1

        return -1


class SolutionIterativeDFS:
    """Using iterative DFS"""

    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find first island
        island = []
        start = None

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        # DFS to mark first island
        stack = [start]
        grid[start[0]][start[1]] = 2

        while stack:
            r, c = stack.pop()
            island.append((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    stack.append((nr, nc))

        # BFS from first island
        queue = deque(island)
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return steps
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))

            steps += 1

        return -1
