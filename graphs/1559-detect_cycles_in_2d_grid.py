#1559. Detect Cycles in 2D Grid
#Medium
#
#Given a 2D array of characters grid of size m x n, you need to find if there
#exists any cycle consisting of the same value in grid.
#
#A cycle is a path of length 4 or more in the grid that starts and ends at the
#same cell. From a given cell, you can move to one of the cells adjacent to it
#- in one of the four directions (up, down, left, or right), if it has the same
#value of the current cell.
#
#Also, you cannot move to the cell that you visited in your last move. For
#example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we
#visited (1, 1) which was the last visited cell.
#
#Return true if any cycle of the same value exists in grid, otherwise, return false.
#
#Example 1:
#Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
#Output: true
#Explanation: There are two valid cycles:
#The cycle (0,0) -> (0,1) -> (0,2) -> (0,3) -> (1,3) -> (2,3) -> (3,3) -> (3,2) -> (3,1) -> (3,0) -> (2,0) -> (1,0) -> (0,0)
#
#Example 2:
#Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
#Output: true
#
#Example 3:
#Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
#Output: false
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 500
#    grid consists only of lowercase English letters.

from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        DFS with parent tracking. A cycle exists if we visit a cell
        we've already visited (that isn't our immediate parent).
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, pi: int, pj: int) -> bool:
            visited[i][j] = True
            char = grid[i][j]

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj

                # Check bounds and same character
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == char:
                    # Skip parent
                    if ni == pi and nj == pj:
                        continue

                    # Found cycle - visiting already visited cell
                    if visited[ni][nj]:
                        return True

                    if dfs(ni, nj, i, j):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False


class SolutionUnionFind:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        Union-Find approach. For each cell, union with right and down neighbors
        if they have the same value. If we try to union cells already in the
        same set, we found a cycle.
        """
        m, n = len(grid), len(grid[0])

        # Union-Find
        parent = list(range(m * n))
        rank = [0] * (m * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # Already in same set - cycle detected

            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        for i in range(m):
            for j in range(n):
                curr = i * n + j

                # Check right neighbor
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    if not union(curr, curr + 1):
                        return True

                # Check down neighbor
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    if not union(curr, curr + n):
                        return True

        return False


class SolutionBFS:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        BFS with parent tracking.
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def bfs(si: int, sj: int) -> bool:
            queue = deque([(si, sj, -1, -1)])  # (row, col, parent_row, parent_col)
            visited[si][sj] = True
            char = grid[si][sj]

            while queue:
                i, j, pi, pj = queue.popleft()

                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == char:
                        if ni == pi and nj == pj:
                            continue

                        if visited[ni][nj]:
                            return True

                        visited[ni][nj] = True
                        queue.append((ni, nj, i, j))

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(i, j):
                        return True

        return False


class SolutionIterativeDFS:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        Iterative DFS to avoid recursion limit issues.
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        for si in range(m):
            for sj in range(n):
                if visited[si][sj]:
                    continue

                # DFS from this cell
                stack = [(si, sj, -1, -1)]
                visited[si][sj] = True
                char = grid[si][sj]

                while stack:
                    i, j, pi, pj = stack.pop()

                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + di, j + dj

                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == char:
                            if ni == pi and nj == pj:
                                continue

                            if visited[ni][nj]:
                                return True

                            visited[ni][nj] = True
                            stack.append((ni, nj, i, j))

        return False
