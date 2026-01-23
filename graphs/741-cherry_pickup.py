#741. Cherry Pickup
#Hard
#
#You are given an n x n grid representing a field of cherries, each cell is one
#of three possible integers.
#
#- 0 means the cell is empty, so you can pass through,
#- 1 means the cell contains a cherry that you can pick up and pass through, or
#- -1 means the cell contains a thorn that blocks your way.
#
#Return the maximum number of cherries you can collect by following the rules:
#- Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right
#  or down through valid path cells.
#- After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up.
#- When passing through a path cell containing a cherry, you pick it up, and
#  the cell becomes an empty cell 0.
#- If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries
#  can be collected.
#
#Example 1:
#Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
#Output: 5
#Explanation: The player started at (0, 0) and went down, down, right, right
#to reach (2, 2). 4 cherries were picked up during this single trip, and the
#matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
#Then, the player went left, up, up, left to return home, picking up one more
#cherry. The total number of cherries picked up is 5.
#
#Example 2:
#Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
#Output: 0
#
#Constraints:
#    n == grid.length
#    n == grid[i].length
#    1 <= n <= 50
#    grid[i][j] is -1, 0, or 1.
#    grid[0][0] != -1
#    grid[n - 1][n - 1] != -1

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        """
        Two simultaneous walks: dp[r1][c1][r2] where c2 = r1+c1-r2.
        """
        n = len(grid)

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2

            # Out of bounds or blocked
            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')

            # Reached destination
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            # Cherries at current positions
            cherries = grid[r1][c1]
            if r1 != r2:  # Different cells
                cherries += grid[r2][c2]

            # Try all 4 combinations of moves
            result = max(
                dp(r1 + 1, c1, r2 + 1),  # Both down
                dp(r1 + 1, c1, r2),       # First down, second right
                dp(r1, c1 + 1, r2 + 1),   # First right, second down
                dp(r1, c1 + 1, r2)        # Both right
            )

            return cherries + result

        return max(0, dp(0, 0, 0))


class SolutionBottomUp:
    """Bottom-up DP"""

    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        INF = float('inf')

        # dp[c1][c2] = max cherries when person 1 is at (step-c1, c1)
        # and person 2 is at (step-c2, c2)
        dp = [[-INF] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for step in range(1, 2 * n - 1):
            new_dp = [[-INF] * n for _ in range(n)]

            for c1 in range(max(0, step - n + 1), min(n, step + 1)):
                for c2 in range(max(0, step - n + 1), min(n, step + 1)):
                    r1, r2 = step - c1, step - c2

                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    cherries = grid[r1][c1]
                    if c1 != c2:
                        cherries += grid[r2][c2]

                    # Try all previous states
                    for pc1 in (c1 - 1, c1):
                        for pc2 in (c2 - 1, c2):
                            if pc1 >= 0 and pc2 >= 0:
                                new_dp[c1][c2] = max(
                                    new_dp[c1][c2],
                                    dp[pc1][pc2] + cherries
                                )

            dp = new_dp

        return max(0, dp[n - 1][n - 1])
