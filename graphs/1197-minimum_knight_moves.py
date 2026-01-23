#1197. Minimum Knight Moves
#Medium
#
#In an infinite chess board with coordinates from -infinity to +infinity, you
#have a knight at square [0, 0].
#
#A knight has 8 possible moves it can make. Each move is two squares in a
#cardinal direction, then one square in an orthogonal direction.
#
#Return the minimum number of steps needed to move the knight to the square [x, y].
#It is guaranteed the answer exists.
#
#Example 1:
#Input: x = 2, y = 1
#Output: 1
#Explanation: [0, 0] → [2, 1]
#
#Example 2:
#Input: x = 5, y = 5
#Output: 4
#Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#
#Constraints:
#    -300 <= x <= 300
#    -300 <= y <= 300

from collections import deque
from functools import lru_cache

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        BFS from origin.
        Due to symmetry, we can work in first quadrant (x, y >= 0).
        """
        # Use absolute values due to symmetry
        x, y = abs(x), abs(y)

        if x == 0 and y == 0:
            return 0

        # Knight moves
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # BFS
        visited = {(0, 0)}
        queue = deque([(0, 0, 0)])

        while queue:
            cx, cy, steps = queue.popleft()

            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy

                if nx == x and ny == y:
                    return steps + 1

                # Bound search area (don't go too far negative)
                if (nx, ny) not in visited and -2 <= nx <= x + 4 and -2 <= ny <= y + 4:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return -1


class SolutionDP:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        DP with memoization.
        Due to symmetry, work in first quadrant.
        """
        x, y = abs(x), abs(y)

        @lru_cache(maxsize=None)
        def dp(cx, cy):
            if cx + cy == 0:
                return 0
            if cx + cy == 2:
                return 2  # Special case: (1,1) or (2,0) or (0,2)

            # Ensure we're in first quadrant and making progress
            return 1 + min(
                dp(abs(cx - 2), abs(cy - 1)),
                dp(abs(cx - 1), abs(cy - 2))
            )

        return dp(x, y)


class SolutionBidirectionalBFS:
    def minKnightMoves(self, x: int, y: int) -> int:
        """Bidirectional BFS for faster search"""
        x, y = abs(x), abs(y)

        if x == 0 and y == 0:
            return 0

        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]

        # Forward from origin
        forward = {(0, 0): 0}
        forward_queue = deque([(0, 0)])

        # Backward from target
        backward = {(x, y): 0}
        backward_queue = deque([(x, y)])

        while forward_queue or backward_queue:
            # Expand forward
            if forward_queue:
                cx, cy = forward_queue.popleft()
                for dx, dy in moves:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in backward:
                        return forward[(cx, cy)] + 1 + backward[(nx, ny)]
                    if (nx, ny) not in forward and -2 <= nx <= x + 4 and -2 <= ny <= y + 4:
                        forward[(nx, ny)] = forward[(cx, cy)] + 1
                        forward_queue.append((nx, ny))

            # Expand backward
            if backward_queue:
                cx, cy = backward_queue.popleft()
                for dx, dy in moves:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in forward:
                        return backward[(cx, cy)] + 1 + forward[(nx, ny)]
                    if (nx, ny) not in backward and -2 <= nx <= x + 4 and -2 <= ny <= y + 4:
                        backward[(nx, ny)] = backward[(cx, cy)] + 1
                        backward_queue.append((nx, ny))

        return -1
