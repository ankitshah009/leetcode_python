#711. Number of Distinct Islands II
#Hard
#
#You are given an m x n binary matrix grid. An island is a group of 1's
#(representing land) connected 4-directionally (horizontal or vertical.)
#You may assume all four edges of the grid are surrounded by water.
#
#An island is considered to be the same as another if they have the same shape,
#or have the same shape after rotation (90, 180, or 270 degrees only) or
#reflection (left/right direction or up/down direction).
#
#Return the number of distinct islands.
#
#Example 1:
#Input: grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
#Output: 1
#Explanation: The two islands are considered the same because if we make a
#180 degree clockwise rotation on the first island, then two islands will
#have the same shapes.
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 50
#    grid[i][j] is either 0 or 1.

class Solution:
    def numDistinctIslands2(self, grid: list[list[int]]) -> int:
        """
        For each island, generate all 8 transformations (4 rotations + 4 reflections),
        normalize each, and use canonical form as key.
        """
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, shape):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] == 0 or (r, c) in visited:
                return

            visited.add((r, c))
            shape.append((r, c))

            dfs(r + 1, c, shape)
            dfs(r - 1, c, shape)
            dfs(r, c + 1, shape)
            dfs(r, c - 1, shape)

        def normalize(shape):
            # Translate to origin
            min_r = min(r for r, c in shape)
            min_c = min(c for r, c in shape)
            return tuple(sorted((r - min_r, c - min_c) for r, c in shape))

        def get_transformations(shape):
            # All 8 transformations: 4 rotations x 2 (original + reflection)
            transforms = []

            for coords in [shape]:
                # Original and rotations
                curr = list(coords)
                for _ in range(4):
                    transforms.append(normalize(curr))
                    curr = [(c, -r) for r, c in curr]  # 90 degree rotation

                # Reflection and rotations
                curr = [(-r, c) for r, c in coords]
                for _ in range(4):
                    transforms.append(normalize(curr))
                    curr = [(c, -r) for r, c in curr]

            return min(transforms)  # Canonical form

        distinct = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    shape = []
                    dfs(i, j, shape)
                    canonical = get_transformations(shape)
                    distinct.add(canonical)

        return len(distinct)
