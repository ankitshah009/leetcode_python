#1102. Path With Maximum Minimum Value
#Medium
#
#Given an m x n integer matrix grid, return the maximum score of a path
#starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal
#directions.
#
#The score of a path is the minimum value in that path.
#
#Example 1:
#Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
#Output: 4
#Explanation: The path with the maximum score is highlighted in yellow.
#
#Example 2:
#Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
#Output: 2
#
#Example 3:
#Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],
#               [4,6,5,4,3]]
#Output: 3
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 100
#    0 <= grid[i][j] <= 10^9

from typing import List
import heapq

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        Modified Dijkstra: Max heap prioritizing by minimum value on path.
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Max heap: (-min_value, row, col)
        heap = [(-grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while heap:
            neg_min_val, r, c = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return -neg_min_val

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_min = max(neg_min_val, -grid[nr][nc])  # max of negatives = min of positives
                    heapq.heappush(heap, (new_min, nr, nc))

        return -1


class SolutionBinarySearch:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        Binary search on answer + BFS/DFS to check if path exists.
        """
        from collections import deque

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def can_reach(min_val):
            if grid[0][0] < min_val or grid[m-1][n-1] < min_val:
                return False

            visited = [[False] * n for _ in range(m)]
            queue = deque([(0, 0)])
            visited[0][0] = True

            while queue:
                r, c = queue.popleft()
                if r == m - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] >= min_val:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            return False

        # Binary search
        left, right = 0, min(grid[0][0], grid[m-1][n-1])
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result


class SolutionUnionFind:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        Union-Find: Add cells in decreasing order of value.
        Return when start and end are connected.
        """
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def idx(r, c):
            return r * n + c

        # Sort cells by value (descending)
        cells = [(grid[r][c], r, c) for r in range(m) for c in range(n)]
        cells.sort(reverse=True)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        added = [[False] * n for _ in range(m)]

        for val, r, c in cells:
            added[r][c] = True

            # Connect with already added neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and added[nr][nc]:
                    union(idx(r, c), idx(nr, nc))

            # Check if start and end are connected
            if find(idx(0, 0)) == find(idx(m - 1, n - 1)):
                return val

        return 0
