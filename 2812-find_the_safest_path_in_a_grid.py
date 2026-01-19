#2812. Find the Safest Path in a Grid
#Medium
#
#You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
#    A cell containing a thief if grid[r][c] = 1
#    An empty cell if grid[r][c] = 0
#
#You are initially positioned at cell (0, 0). In one move, you can move to any adjacent
#cell in the grid, including cells containing thieves.
#
#The safeness factor of a path on the grid is defined as the minimum manhattan distance
#from any cell in the path to any thief in the grid.
#
#Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).
#
#An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c)
#and (r - 1, c) if it exists.
#
#The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|,
#where |val| denotes the absolute value of val.
#
#Example 1:
#Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
#Output: 0
#Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
#
#Example 2:
#Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
#Output: 2
#Explanation: The path depicted in the picture above has a safeness factor of 2.
#
#Constraints:
#    1 <= grid.length == n <= 400
#    grid[i].length == n
#    grid[i][j] is either 0 or 1.
#    There is at least one thief in the grid.

from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0

        # BFS to calculate minimum distance to any thief for each cell
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    queue.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # Dijkstra-like approach: maximize minimum safeness on path
        # Use max-heap (negate values for max behavior)
        heap = [(-dist[0][0], 0, 0)]
        seen = set()

        while heap:
            safeness, r, c = heapq.heappop(heap)
            safeness = -safeness

            if (r, c) in seen:
                continue
            seen.add((r, c))

            if r == n - 1 and c == n - 1:
                return safeness

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    new_safeness = min(safeness, dist[nr][nc])
                    heapq.heappush(heap, (-new_safeness, nr, nc))

        return 0
