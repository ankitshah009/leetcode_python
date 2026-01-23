#778. Swim in Rising Water
#Hard
#
#You are given an n x n integer matrix grid where each value grid[i][j]
#represents the elevation at that point (i, j).
#
#The rain starts to fall. At time t, the depth of the water everywhere is t.
#You can swim from a square to another 4-directionally adjacent square if and
#only if the elevation of both squares individually are at most t. You can swim
#infinite distances in zero time. Of course, you must stay within the boundaries
#of the grid during your swim.
#
#Return the least time until you can reach the bottom right square (n - 1, n - 1)
#starting from the top left square (0, 0).
#
#Example 1:
#Input: grid = [[0,2],[1,3]]
#Output: 3
#Explanation: At time 0, you are in grid location (0, 0). You cannot go anywhere
#else because 4-directionally adjacent neighbors have a higher elevation.
#At time 3, you can swim to (1, 0) then (1, 1).
#
#Example 2:
#Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
#Output: 16
#
#Constraints:
#    n == grid.length
#    n == grid[i].length
#    1 <= n <= 50
#    0 <= grid[i][j] < n^2
#    Each value grid[i][j] is unique.

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Dijkstra-like: min time to reach each cell = max elevation on path.
        """
        n = len(grid)

        # Min-heap: (max_elevation_on_path, row, col)
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while heap:
            max_elev, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return max_elev

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (max(max_elev, grid[nr][nc]), nr, nc))

        return -1


class SolutionBinarySearch:
    """Binary search on answer + BFS/DFS to check"""

    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def can_reach(t):
            if grid[0][0] > t:
                return False

            visited = [[False] * n for _ in range(n)]
            stack = [(0, 0)]
            visited[0][0] = True

            while stack:
                r, c = stack.pop()
                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < n and
                        not visited[nr][nc] and grid[nr][nc] <= t):
                        visited[nr][nc] = True
                        stack.append((nr, nc))

            return False

        left, right = max(grid[0][0], grid[n-1][n-1]), n * n - 1

        while left < right:
            mid = (left + right) // 2
            if can_reach(mid):
                right = mid
            else:
                left = mid + 1

        return left


class SolutionUnionFind:
    """Union-Find: add cells in order of elevation"""

    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        parent = list(range(n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def idx(r, c):
            return r * n + c

        # Sort cells by elevation
        cells = sorted((grid[r][c], r, c) for r in range(n) for c in range(n))

        for elev, r, c in cells:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= elev:
                    union(idx(r, c), idx(nr, nc))

            if find(0) == find(n * n - 1):
                return elev

        return -1
