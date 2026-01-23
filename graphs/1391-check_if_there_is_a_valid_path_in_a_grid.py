#1391. Check if There is a Valid Path in a Grid
#Medium
#
#You are given an m x n grid. Each cell of grid represents a street. The street
#of grid[i][j] can be:
#    1 which means a street connecting the left cell and the right cell.
#    2 which means a street connecting the upper cell and the lower cell.
#    3 which means a street connecting the left cell and the lower cell.
#    4 which means a street connecting the right cell and the lower cell.
#    5 which means a street connecting the left cell and the upper cell.
#    6 which means a street connecting the right cell and the upper cell.
#
#You will initially start at the street of the upper-left cell (0, 0). A valid
#path in the grid is a path that starts from the upper left cell (0, 0) and ends
#at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.
#
#Notice that you are not allowed to change any street.
#
#Return true if there is a valid path in the grid or false otherwise.
#
#Example 1:
#Input: grid = [[2,4,3],[6,5,2]]
#Output: true
#
#Example 2:
#Input: grid = [[1,2,1],[1,2,1]]
#Output: false
#
#Example 3:
#Input: grid = [[1,1,2]]
#Output: false
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 300
#    1 <= grid[i][j] <= 6

from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """
        BFS/DFS with street connection rules.
        Each street type connects to specific directions.
        Check both: can we leave current cell AND can we enter next cell.
        """
        m, n = len(grid), len(grid[0])

        # Define which directions each street type connects
        # directions: 0=up, 1=right, 2=down, 3=left
        street_connections = {
            1: {1, 3},      # left-right
            2: {0, 2},      # up-down
            3: {2, 3},      # left-down
            4: {1, 2},      # right-down
            5: {0, 3},      # left-up
            6: {0, 1}       # right-up
        }

        # Direction deltas: up, right, down, left
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        # Opposite directions
        opposite = {0: 2, 1: 3, 2: 0, 3: 1}

        visited = [[False] * n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()

            if r == m - 1 and c == n - 1:
                return True

            street = grid[r][c]

            for direction in street_connections[street]:
                nr, nc = r + dr[direction], c + dc[direction]

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    next_street = grid[nr][nc]
                    # Check if next cell can be entered from this direction
                    if opposite[direction] in street_connections[next_street]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False


class SolutionDFS:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """DFS approach"""
        m, n = len(grid), len(grid[0])

        # Street type -> set of (dr, dc) it connects to
        connections = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(0, 1), (1, 0)],    # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)]    # right, up
        }

        visited = set()

        def dfs(r: int, c: int) -> bool:
            if r == m - 1 and c == n - 1:
                return True

            visited.add((r, c))
            street = grid[r][c]

            for dr, dc in connections[street]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if next cell connects back
                    if (-dr, -dc) in connections[grid[nr][nc]]:
                        if dfs(nr, nc):
                            return True

            return False

        return dfs(0, 0)


class SolutionUnionFind:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """Union-Find approach"""
        m, n = len(grid), len(grid[0])

        parent = list(range(m * n))
        rank = [0] * (m * n)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # Connect adjacent compatible cells
        connections = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        for r in range(m):
            for c in range(n):
                street = grid[r][c]
                for dr, dc in connections[street]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (-dr, -dc) in connections[grid[nr][nc]]:
                            union(r * n + c, nr * n + nc)

        return find(0) == find(m * n - 1)
