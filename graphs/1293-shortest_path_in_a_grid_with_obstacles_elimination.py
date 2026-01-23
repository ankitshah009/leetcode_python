#1293. Shortest Path in a Grid with Obstacles Elimination
#Hard
#
#You are given an m x n integer matrix grid where each cell is either 0 (empty)
#or 1 (obstacle). You can move up, down, left, or right from and to an empty cell
#in one step.
#
#Return the minimum number of steps to walk from the upper left corner (0, 0) to
#the lower right corner (m - 1, n - 1) given that you can eliminate at most k
#obstacles. If it is not possible to find such walk return -1.
#
#Example 1:
#Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
#Output: 6
#Explanation:
#The shortest path without eliminating any obstacle is 10.
#The shortest path with one obstacle elimination at position (3,2) is 6.
#
#Example 2:
#Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
#Output: -1
#Explanation: We need to eliminate at least two obstacles to find such a walk.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 40
#    1 <= k <= m * n
#    grid[i][j] is either 0 or 1.
#    grid[0][0] == grid[m - 1][n - 1] == 0

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        BFS with state (row, col, remaining_eliminations).
        """
        m, n = len(grid), len(grid[0])

        # If we have enough k, can just go straight
        if k >= m + n - 3:
            return m + n - 2

        # BFS: (row, col, remaining_k)
        queue = deque([(0, 0, k, 0)])  # row, col, remaining_k, steps
        visited = {(0, 0, k)}

        while queue:
            row, col, remaining, steps = queue.popleft()

            if row == m - 1 and col == n - 1:
                return steps

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_k = remaining - grid[nr][nc]

                    if new_k >= 0 and (nr, nc, new_k) not in visited:
                        visited.add((nr, nc, new_k))
                        queue.append((nr, nc, new_k, steps + 1))

        return -1


class SolutionAStar:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """A* search with Manhattan distance heuristic"""
        import heapq

        m, n = len(grid), len(grid[0])

        if k >= m + n - 3:
            return m + n - 2

        def heuristic(r, c):
            return (m - 1 - r) + (n - 1 - c)

        # (estimated_cost, steps, row, col, remaining_k)
        heap = [(heuristic(0, 0), 0, 0, 0, k)]
        visited = {}  # (r, c) -> max remaining_k when visited

        while heap:
            _, steps, row, col, remaining = heapq.heappop(heap)

            if row == m - 1 and col == n - 1:
                return steps

            # Skip if we've been here with more k
            if (row, col) in visited and visited[(row, col)] >= remaining:
                continue
            visited[(row, col)] = remaining

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_k = remaining - grid[nr][nc]
                    if new_k >= 0:
                        new_steps = steps + 1
                        heapq.heappush(heap, (new_steps + heuristic(nr, nc), new_steps, nr, nc, new_k))

        return -1
