#1568. Minimum Number of Days to Disconnect Island
#Hard
#
#You are given an m x n binary grid grid where 1 represents land and 0 represents
#water. An island is a maximal 4-directionally (horizontal or vertical) connected
#group of 1's.
#
#The grid is said to be connected if we have exactly one island, otherwise is
#said disconnected.
#
#In one day, we are allowed to change any single land cell (1) into a water cell (0).
#
#Return the minimum number of days to disconnect the grid.
#
#Example 1:
#Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
#Output: 2
#Explanation: We need at least 2 days to get a disconnected grid.
#Change land grid[1][1] and grid[0][2] to water and get 2 disconnected islands.
#
#Example 2:
#Input: grid = [[1,1]]
#Output: 2
#Explanation: Grid of 1's and 0's will become disconnected by removing any 2 land cells.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 30
#    grid[i][j] is either 0 or 1.

from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """
        Key insight: Answer is always 0, 1, or 2.
        - 0: Already disconnected or no islands
        - 1: There exists an articulation point (removing it disconnects)
        - 2: Otherwise (can always disconnect by removing corner of island)

        Check in this order.
        """
        m, n = len(grid), len(grid[0])

        def count_islands():
            visited = [[False] * n for _ in range(m)]
            count = 0

            def dfs(i, j):
                if i < 0 or i >= m or j < 0 or j >= n:
                    return
                if visited[i][j] or grid[i][j] == 0:
                    return
                visited[i][j] = True
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        dfs(i, j)
                        count += 1

            return count

        # Check if already disconnected
        if count_islands() != 1:
            return 0

        # Check if removing any single cell disconnects
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    islands = count_islands()
                    grid[i][j] = 1

                    if islands != 1:
                        return 1

        # Otherwise, answer is 2
        return 2


class SolutionArticulation:
    def minDays(self, grid: List[List[int]]) -> int:
        """
        Using Tarjan's algorithm for articulation points.
        """
        m, n = len(grid), len(grid[0])

        def count_islands():
            visited = set()
            count = 0

            def dfs(i, j):
                if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n:
                    return
                if grid[i][j] == 0:
                    return
                visited.add((i, j))
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    dfs(i+di, j+dj)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j)
                        count += 1
            return count

        if count_islands() != 1:
            return 0

        # Try removing each land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2


class SolutionOptimized:
    def minDays(self, grid: List[List[int]]) -> int:
        """
        Optimized with early termination.
        """
        m, n = len(grid), len(grid[0])

        def get_land_cells():
            return [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        def is_connected(land_cells):
            if not land_cells:
                return False
            if len(land_cells) == 1:
                return True

            visited = set()
            start = land_cells[0]

            def dfs(cell):
                if cell in visited:
                    return
                visited.add(cell)
                i, j = cell
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        dfs((ni, nj))

            dfs(start)
            return len(visited) == len(land_cells)

        land = get_land_cells()

        if not is_connected(land):
            return 0

        if len(land) <= 2:
            return len(land)

        # Check articulation points
        for i, j in land:
            grid[i][j] = 0
            new_land = [(x, y) for x, y in land if (x, y) != (i, j)]
            if not is_connected(new_land):
                return 1
            grid[i][j] = 1

        return 2
