#1368. Minimum Cost to Make at Least One Valid Path in a Grid
#Hard
#
#Given an m x n grid. Each cell of the grid has a sign pointing to the next
#cell you should visit if you are currently in this cell. The sign of grid[i][j]
#can be:
#    1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
#    2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
#    3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
#    4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
#
#Notice that there could be some signs on the cells of the grid that point
#outside the grid.
#
#You will initially start at the upper left cell (0, 0). A valid path in the
#grid is a path that starts from the upper left cell (0, 0) and ends at the
#bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
#path does not have to be the shortest.
#
#You can modify the sign on a cell with cost = 1. You can modify the sign on a
#cell one time only.
#
#Return the minimum cost to make the grid have at least one valid path.
#
#Example 1:
#Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
#Output: 3
#
#Example 2:
#Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
#Output: 0
#
#Example 3:
#Input: grid = [[1,2],[4,3]]
#Output: 1
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 100
#    1 <= grid[i][j] <= 4

from typing import List
from collections import deque
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        0-1 BFS: Following arrow costs 0, changing direction costs 1.
        Use deque: add cost-0 edges to front, cost-1 to back.
        """
        m, n = len(grid), len(grid[0])

        # Direction mapping: 1=right, 2=left, 3=down, 4=up
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        # Deque for 0-1 BFS
        dq = deque([(0, 0, 0)])  # (row, col, cost)

        while dq:
            r, c, cost = dq.popleft()

            if cost > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            # Try all 4 directions
            for direction, (dr, dc) in dirs.items():
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    # Cost is 0 if following arrow, 1 otherwise
                    new_cost = cost if grid[r][c] == direction else cost + 1

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        if grid[r][c] == direction:
                            dq.appendleft((nr, nc, new_cost))
                        else:
                            dq.append((nr, nc, new_cost))

        return dist[m - 1][n - 1]


class SolutionDijkstra:
    def minCost(self, grid: List[List[int]]) -> int:
        """Dijkstra's algorithm"""
        m, n = len(grid), len(grid[0])
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (cost, row, col)

        while heap:
            cost, r, c = heapq.heappop(heap)

            if cost > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            for direction, (dr, dc) in dirs.items():
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost if grid[r][c] == direction else cost + 1

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(heap, (new_cost, nr, nc))

        return dist[m - 1][n - 1]
