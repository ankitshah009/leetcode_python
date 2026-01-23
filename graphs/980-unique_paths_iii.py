#980. Unique Paths III
#Hard
#
#You are given an m x n integer array grid where grid[i][j] could be:
#- 1 representing the starting square.
#- 2 representing the ending square.
#- 0 representing empty squares we can walk over.
#- -1 representing obstacles that we cannot walk over.
#
#Return the number of 4-directional walks from the starting square to the
#ending square, that walk over every non-obstacle square exactly once.
#
#Example 1:
#Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
#Output: 2
#
#Example 2:
#Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
#Output: 4
#
#Example 3:
#Input: grid = [[0,1],[2,0]]
#Output: 0
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 20
#    1 <= m * n <= 20
#    -1 <= grid[i][j] <= 2
#    There is exactly one starting cell and one ending cell.

class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        """
        Backtracking: count paths visiting all empty squares.
        """
        m, n = len(grid), len(grid[0])

        # Find start, end, and count of empty squares
        start = None
        end = None
        empty = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    empty += 1

        # Need to visit empty + 1 (for start) squares before reaching end
        result = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, remaining):
            nonlocal result

            if (r, c) == end:
                if remaining == 0:
                    result += 1
                return

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    # Mark as visited
                    temp = grid[nr][nc]
                    grid[nr][nc] = -1

                    if temp == 2:
                        dfs(nr, nc, remaining)
                    else:
                        dfs(nr, nc, remaining - 1)

                    grid[nr][nc] = temp

        grid[start[0]][start[1]] = -1
        dfs(start[0], start[1], empty + 1)

        return result


class SolutionBitmask:
    """Using bitmask for visited state"""

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Find start, end, target mask
        start = end = None
        target = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    target |= (1 << (i * n + j))
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(r, c, visited):
            if (r, c) == end:
                return 1 if visited == target else 0

            result = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                bit = 1 << (nr * n + nc)

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    if not (visited & bit):
                        result += dfs(nr, nc, visited | bit)

            return result

        start_bit = 1 << (start[0] * n + start[1])
        return dfs(start[0], start[1], start_bit)
