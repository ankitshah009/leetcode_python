#317. Shortest Distance from All Buildings
#Hard
#
#You are given an m x n grid grid of values 0, 1, or 2, where:
#    each 0 marks an empty land that you can pass by freely,
#    each 1 marks a building that you cannot pass through, and
#    each 2 marks an obstacle that you cannot pass through.
#
#You want to build a house on an empty land that reaches all buildings in the
#shortest total travel distance. You can only move up, down, left, and right.
#
#Return the shortest travel distance for such a house. If it is not possible to
#build such a house according to the above rules, return -1.
#
#The total travel distance is the sum of the distances between the houses of
#the friends and the meeting point.
#
#Example 1:
#Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#Output: 7
#Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
#(0,2). The point (1,2) is an ideal empty land to build a house, as the total
#travel distance of 3+3+1=7 is minimal.
#
#Example 2:
#Input: grid = [[1,0]]
#Output: 1
#
#Example 3:
#Input: grid = [[1]]
#Output: -1
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 50
#    grid[i][j] is either 0, 1, or 2.
#    There will be at least one building in the grid.

from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Count buildings
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1

        # dist[i][j] = total distance from all buildings
        # reach[i][j] = number of buildings that can reach this cell
        dist = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(start_r, start_c):
            visited = [[False] * n for _ in range(m)]
            queue = deque([(start_r, start_c, 0)])
            visited[start_r][start_c] = True

            while queue:
                r, c, d = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        dist[nr][nc] += d + 1
                        reach[nr][nc] += 1
                        queue.append((nr, nc, d + 1))

        # BFS from each building
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)

        # Find minimum distance among cells reachable by all buildings
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildings:
                    min_dist = min(min_dist, dist[i][j])

        return min_dist if min_dist != float('inf') else -1
