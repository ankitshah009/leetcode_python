#1210. Minimum Moves to Reach Target with Rotations
#Hard
#
#In an n*n grid, there is a snake that spans 2 cells and starts moving from
#the top left corner at (0, 0) and (0, 1). The grid has empty cells represented
#by zeros and blocked cells represented by ones. The snake wants to reach the
#lower right corner at (n-1, n-2) and (n-1, n-1).
#
#In one move the snake can:
#    Move one cell to the right if there are no blocked cells there. This move
#    keeps the horizontal/vertical position of the snake as it is.
#    Move one cell down if there are no blocked cells there. This move keeps
#    the horizontal/vertical position of the snake as it is.
#    Rotate clockwise if it's in a horizontal position and the two cells under
#    it are both empty. In that case the snake moves from (r, c) and (r, c+1)
#    to (r, c) and (r+1, c).
#    Rotate counterclockwise if it's in a vertical position and the two cells
#    to its right are both empty. In that case the snake moves from (r, c) and
#    (r+1, c) to (r, c) and (r, c+1).
#
#Return the minimum number of moves to reach the target. If there is no way to
#reach the target, return -1.
#
#Example 1:
#Input: grid = [[0,0,0,0,0,1],
#               [1,1,0,0,1,0],
#               [0,0,0,0,1,1],
#               [0,0,1,0,1,0],
#               [0,1,1,0,0,0],
#               [0,1,1,0,0,0]]
#Output: 11
#
#Example 2:
#Input: grid = [[0,0,1,1,1,1],
#               [0,0,0,0,1,1],
#               [1,1,0,0,0,1],
#               [1,1,1,0,0,1],
#               [1,1,1,0,0,1],
#               [1,1,1,0,0,0]]
#Output: 9
#
#Constraints:
#    2 <= n <= 100
#    0 <= grid[i][j] <= 1
#    The snake starts at empty cells.

from typing import List
from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        BFS with state = (row, col, direction)
        direction: 0 = horizontal, 1 = vertical
        (row, col) represents the left/top cell of snake
        """
        n = len(grid)

        # Target state: horizontal at (n-1, n-2)
        target = (n - 1, n - 2, 0)

        # BFS
        queue = deque([(0, 0, 0, 0)])  # (row, col, direction, moves)
        visited = {(0, 0, 0)}

        while queue:
            r, c, direction, moves = queue.popleft()

            if (r, c, direction) == target:
                return moves

            if direction == 0:  # Horizontal
                # Move right: need (r, c+2) empty
                if c + 2 < n and grid[r][c + 2] == 0:
                    state = (r, c + 1, 0)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r, c + 1, 0, moves + 1))

                # Move down: need (r+1, c) and (r+1, c+1) empty
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r + 1, c, 0)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r + 1, c, 0, moves + 1))

                    # Rotate clockwise: also need (r+1, c) and (r+1, c+1) empty
                    state = (r, c, 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r, c, 1, moves + 1))

            else:  # Vertical
                # Move right: need (r, c+1) and (r+1, c+1) empty
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r, c + 1, 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r, c + 1, 1, moves + 1))

                    # Rotate counterclockwise: also need right cells empty
                    state = (r, c, 0)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r, c, 0, moves + 1))

                # Move down: need (r+2, c) empty
                if r + 2 < n and grid[r + 2][c] == 0:
                    state = (r + 1, c, 1)
                    if state not in visited:
                        visited.add(state)
                        queue.append((r + 1, c, 1, moves + 1))

        return -1


class SolutionDP:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """DP approach with BFS-like iteration"""
        n = len(grid)
        INF = float('inf')

        # dp[r][c][d] = min moves to reach state (r, c, d)
        dp = [[[INF] * 2 for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = 0

        changed = True
        while changed:
            changed = False

            for r in range(n):
                for c in range(n):
                    for d in range(2):
                        if dp[r][c][d] == INF:
                            continue

                        moves = dp[r][c][d]

                        if d == 0:  # Horizontal
                            # Move right
                            if c + 2 < n and grid[r][c + 2] == 0:
                                if dp[r][c + 1][0] > moves + 1:
                                    dp[r][c + 1][0] = moves + 1
                                    changed = True

                            # Move down
                            if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                                if dp[r + 1][c][0] > moves + 1:
                                    dp[r + 1][c][0] = moves + 1
                                    changed = True

                                # Rotate
                                if dp[r][c][1] > moves + 1:
                                    dp[r][c][1] = moves + 1
                                    changed = True

                        else:  # Vertical
                            # Move right
                            if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                                if dp[r][c + 1][1] > moves + 1:
                                    dp[r][c + 1][1] = moves + 1
                                    changed = True

                                # Rotate
                                if dp[r][c][0] > moves + 1:
                                    dp[r][c][0] = moves + 1
                                    changed = True

                            # Move down
                            if r + 2 < n and grid[r + 2][c] == 0:
                                if dp[r + 1][c][1] > moves + 1:
                                    dp[r + 1][c][1] = moves + 1
                                    changed = True

        result = dp[n - 1][n - 2][0]
        return result if result != INF else -1
