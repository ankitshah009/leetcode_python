#1162. As Far from Land as Possible
#Medium
#
#Given an n x n grid containing only values 0 and 1, where 0 represents water
#and 1 represents land, find a water cell such that its distance to the nearest
#land cell is maximized, and return the distance. If no land or water exists
#in the grid, return -1.
#
#The distance used in this problem is the Manhattan distance: the distance
#between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
#Example 1:
#Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
#Output: 2
#Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
#
#Example 2:
#Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
#Output: 4
#Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
#
#Constraints:
#    n == grid.length
#    n == grid[i].length
#    1 <= n <= 100
#    grid[i][j] is 0 or 1

from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS from all land cells.
        Last cell visited is the answer.
        """
        n = len(grid)
        queue = deque()

        # Add all land cells to queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # If no land or no water
        if len(queue) == 0 or len(queue) == n * n:
            return -1

        # BFS from all land cells simultaneously
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = -1

        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1  # Mark as visited
                        queue.append((nx, ny))

        return distance


class SolutionDP:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        DP: Two passes to compute distance from nearest land.
        """
        n = len(grid)
        INF = float('inf')

        # Initialize distances
        dist = [[INF] * n for _ in range(n)]

        # Set land cells to 0
        has_land = has_water = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    has_land = True
                else:
                    has_water = True

        if not has_land or not has_water:
            return -1

        # First pass: top-left to bottom-right
        for i in range(n):
            for j in range(n):
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)

        # Second pass: bottom-right to top-left
        result = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < n - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
                result = max(result, dist[i][j])

        return result
