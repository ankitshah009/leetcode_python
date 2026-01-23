#959. Regions Cut By Slashes
#Medium
#
#An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of
#a '/', '\\', or blank space ' '. These characters divide the square into
#contiguous regions.
#
#Return the number of regions.
#
#Note: Backslash characters are escaped, so '\\' is the visual representation
#of a single backslash.
#
#Example 1:
#Input: grid = [" /","/ "]
#Output: 2
#
#Example 2:
#Input: grid = [" /","  "]
#Output: 1
#
#Example 3:
#Input: grid = ["/\\","\\/"]
#Output: 5
#
#Constraints:
#    n == grid.length == grid[i].length
#    1 <= n <= 30
#    grid[i][j] is either '/', '\\', or ' '.

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        """
        Scale up 3x: each cell becomes 3x3 grid.
        Count connected components of 0s.
        """
        n = len(grid)
        scaled = [[0] * (3 * n) for _ in range(3 * n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    scaled[3*i][3*j+2] = 1
                    scaled[3*i+1][3*j+1] = 1
                    scaled[3*i+2][3*j] = 1
                elif grid[i][j] == '\\':
                    scaled[3*i][3*j] = 1
                    scaled[3*i+1][3*j+1] = 1
                    scaled[3*i+2][3*j+2] = 1

        # Count connected components of 0s
        def dfs(r, c):
            if r < 0 or r >= 3*n or c < 0 or c >= 3*n:
                return
            if scaled[r][c] == 1:
                return
            scaled[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        regions = 0
        for i in range(3*n):
            for j in range(3*n):
                if scaled[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions


class SolutionUnionFind:
    """Union-Find with 4 triangles per cell"""

    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        # Each cell divided into 4 triangles: 0=top, 1=right, 2=bottom, 3=left
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def index(r, c, k):
            return 4 * (r * n + c) + k

        for i in range(n):
            for j in range(n):
                # Connect within cell based on character
                if grid[i][j] != '/':
                    union(index(i, j, 0), index(i, j, 1))
                    union(index(i, j, 2), index(i, j, 3))
                if grid[i][j] != '\\':
                    union(index(i, j, 0), index(i, j, 3))
                    union(index(i, j, 1), index(i, j, 2))

                # Connect to right neighbor
                if j + 1 < n:
                    union(index(i, j, 1), index(i, j+1, 3))

                # Connect to bottom neighbor
                if i + 1 < n:
                    union(index(i, j, 2), index(i+1, j, 0))

        return sum(find(i) == i for i in range(4 * n * n))
