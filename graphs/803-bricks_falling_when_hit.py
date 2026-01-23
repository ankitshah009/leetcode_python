#803. Bricks Falling When Hit
#Hard
#
#You are given an m x n grid, where each cell is 0 (empty) or 1 (brick).
#A brick is stable if:
#- It is directly connected to the top of the grid, or
#- At least one other brick in its four adjacent cells is stable.
#
#You are given an array hits, which is a sequence of erasures we want to apply.
#Each time we want to erase the brick at hits[i] = (rowi, coli). The brick on
#that location (if exists) will disappear. Some other bricks may no longer be
#stable because of that erasure and will fall. Once a brick falls, it is
#immediately erased from the grid.
#
#Return an array result, where each result[i] is the number of bricks that will
#fall after the ith erasure is applied.
#
#Example 1:
#Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
#Output: [2]
#
#Example 2:
#Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
#Output: [0,0]
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 200
#    grid[i][j] is 0 or 1.
#    1 <= hits.length <= 4 * 10^4
#    hits[i].length == 2
#    0 <= xi <= m - 1
#    0 <= yi <= n - 1
#    All (xi, yi) are unique.

class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        """
        Reverse time: start with all bricks removed, add them back.
        Use Union-Find to track connected components to ceiling.
        """
        m, n = len(grid), len(grid[0])

        # Union-Find with size tracking
        parent = list(range(m * n + 1))  # Extra node for ceiling
        size = [1] * (m * n + 1)
        CEILING = m * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            # Always attach to ceiling if one is ceiling
            if px == CEILING:
                px, py = py, px
            parent[px] = py
            size[py] += size[px]

        def index(r, c):
            return r * n + c

        def ceiling_size():
            return size[find(CEILING)]

        # Mark hit locations
        grid_copy = [row[:] for row in grid]
        for r, c in hits:
            grid_copy[r][c] = 0

        # Build initial structure (after all hits)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for c in range(n):
            if grid_copy[0][c] == 1:
                union(index(0, c), CEILING)

        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid_copy[nr][nc] == 1:
                            union(index(r, c), index(nr, nc))

        # Process hits in reverse
        result = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                result.append(0)
                continue

            prev_ceiling = ceiling_size()

            # Add brick back
            grid_copy[r][c] = 1

            if r == 0:
                union(index(r, c), CEILING)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid_copy[nr][nc] == 1:
                    union(index(r, c), index(nr, nc))

            new_ceiling = ceiling_size()
            # Bricks that fell = new attached - 1 (for the brick we added)
            result.append(max(0, new_ceiling - prev_ceiling - 1))

        return result[::-1]
