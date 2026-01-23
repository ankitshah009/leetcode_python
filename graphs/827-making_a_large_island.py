#827. Making A Large Island
#Hard
#
#You are given an n x n binary matrix grid. You are allowed to change at most
#one 0 to be 1.
#
#Return the size of the largest island in grid after applying this operation.
#
#An island is a 4-directionally connected group of 1s.
#
#Example 1:
#Input: grid = [[1,0],[0,1]]
#Output: 3
#Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#
#Example 2:
#Input: grid = [[1,1],[1,0]]
#Output: 4
#Explanation: Change the 0 to 1 and make the island bigger, area = 4.
#
#Example 3:
#Input: grid = [[1,1],[1,1]]
#Output: 4
#Explanation: Can't change any 0 to 1, only one island with area = 4.
#
#Constraints:
#    n == grid.length
#    n == grid[i].length
#    1 <= n <= 500
#    grid[i][j] is either 0 or 1.

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        """
        1. Label each island with unique ID and compute sizes
        2. For each 0, compute sum of adjacent island sizes
        """
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS to label islands
        def dfs(r, c, label):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = label
            size = 1

            for dr, dc in directions:
                size += dfs(r + dr, c + dc, label)

            return size

        # Label islands starting from 2
        island_size = {0: 0}  # Size of each island
        label = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, label)
                    island_size[label] = size
                    label += 1

        # Check each 0 cell
        max_island = max(island_size.values()) if island_size else 0

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    # Get unique adjacent islands
                    adjacent = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            adjacent.add(grid[nr][nc])

                    # Sum sizes of adjacent islands + 1
                    total = 1 + sum(island_size.get(lbl, 0) for lbl in adjacent)
                    max_island = max(max_island, total)

        return max_island


class SolutionUnionFind:
    """Union-Find approach"""

    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)

        parent = list(range(n * n))
        size = [1] * (n * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if size[px] < size[py]:
                    px, py = py, px
                parent[py] = px
                size[px] += size[py]

        def index(r, c):
            return r * n + c

        # Build initial islands
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            union(index(r, c), index(nr, nc))

        # Find max island
        max_size = 0
        for i in range(n * n):
            if grid[i // n][i % n] == 1:
                max_size = max(max_size, size[find(i)])

        # Try flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    adjacent = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            adjacent.add(find(index(nr, nc)))

                    total = 1 + sum(size[p] for p in adjacent)
                    max_size = max(max_size, total)

        return max_size if max_size > 0 else 1
