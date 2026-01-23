#749. Contain Virus
#Hard
#
#A virus is spreading rapidly, and your task is to quarantine the infected area
#by installing walls.
#
#The world is modeled as an m x n binary grid isInfected, where isInfected[i][j]
#== 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells
#contaminated with the virus. A wall (and only one wall) can be installed
#between any two 4-directionally adjacent cells, on the shared boundary.
#
#Every night, the virus spreads to all neighboring cells in all four directions
#unless blocked by a wall. Resources are limited. Each day, you can install
#walls around only one region.
#
#The affected area that threatens the most uninfected cells gets quarantined
#first. Return the number of walls used to quarantine all the infected regions.
#
#Example 1:
#Input: isInfected = [[0,1,0,0,0,0,0,1],
#                     [0,1,0,0,0,0,0,1],
#                     [0,0,0,0,0,0,0,1],
#                     [0,0,0,0,0,0,0,0]]
#Output: 10
#
#Constraints:
#    m == isInfected.length
#    n == isInfected[i].length
#    1 <= m, n <= 50
#    isInfected[i][j] is either 0 or 1.
#    There is always a contiguous viral region throughout the described process.

class Solution:
    def containVirus(self, isInfected: list[list[int]]) -> int:
        """
        Simulation: each day find most threatening region, quarantine it.
        """
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0

        def get_regions():
            """Find all infected regions with their frontiers and wall counts."""
            visited = [[False] * n for _ in range(m)]
            regions = []

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        cells = set()
                        frontier = set()
                        walls = [0]

                        def dfs(r, c):
                            if r < 0 or r >= m or c < 0 or c >= n:
                                return
                            if visited[r][c]:
                                return
                            if isInfected[r][c] == 0:
                                frontier.add((r, c))
                                walls[0] += 1
                                return
                            if isInfected[r][c] != 1:
                                return

                            visited[r][c] = True
                            cells.add((r, c))

                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                dfs(r + dr, c + dc)

                        dfs(i, j)
                        if frontier:
                            regions.append((cells, frontier, walls[0]))

            return regions

        while True:
            regions = get_regions()

            if not regions:
                break

            # Find most threatening region
            regions.sort(key=lambda x: len(x[1]), reverse=True)
            cells, frontier, walls = regions[0]

            # Quarantine this region
            total_walls += walls
            for r, c in cells:
                isInfected[r][c] = 2  # Mark as quarantined

            # Spread other regions
            for i in range(1, len(regions)):
                cells, frontier, _ = regions[i]
                for r, c in frontier:
                    isInfected[r][c] = 1

        return total_walls


class SolutionBFS:
    """BFS version of the simulation"""

    def containVirus(self, isInfected: list[list[int]]) -> int:
        from collections import deque

        m, n = len(isInfected), len(isInfected[0])
        total = 0

        while True:
            visited = [[False] * n for _ in range(m)]
            regions = []

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        cells = []
                        frontier = set()
                        walls = 0

                        queue = deque([(i, j)])
                        visited[i][j] = True

                        while queue:
                            r, c = queue.popleft()
                            cells.append((r, c))

                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 0:
                                        frontier.add((nr, nc))
                                        walls += 1
                                    elif isInfected[nr][nc] == 1 and not visited[nr][nc]:
                                        visited[nr][nc] = True
                                        queue.append((nr, nc))

                        if frontier:
                            regions.append((cells, frontier, walls))

            if not regions:
                break

            regions.sort(key=lambda x: len(x[1]), reverse=True)

            # Quarantine most threatening
            for r, c in regions[0][0]:
                isInfected[r][c] = 2
            total += regions[0][2]

            # Spread others
            for i in range(1, len(regions)):
                for r, c in regions[i][1]:
                    isInfected[r][c] = 1

        return total
