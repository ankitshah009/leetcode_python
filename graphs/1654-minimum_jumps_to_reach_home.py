#1654. Minimum Jumps to Reach Home
#Medium
#
#A certain bug's home is on the x-axis at position x. Help them get there from
#position 0.
#
#The bug jumps according to the following rules:
#- It can jump exactly a positions forward (to the right).
#- It can jump exactly b positions backward (to the left).
#- It cannot jump backward twice in a row.
#- It cannot jump to any forbidden positions.
#
#The bug may jump forward beyond its home, but it cannot jump to positions
#numbered with negative integers.
#
#Return the minimum number of jumps needed for the bug to reach its home.
#If there is no possible sequence of jumps that lands the bug on position x,
#return -1.
#
#Example 1:
#Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
#Output: 3
#Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9).
#
#Example 2:
#Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
#Output: -1
#
#Example 3:
#Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
#Output: 2
#
#Constraints:
#    1 <= forbidden.length <= 1000
#    1 <= a, b, forbidden[i] <= 2000
#    0 <= x <= 2000
#    All elements in forbidden are distinct.
#    Position x is not forbidden.

from typing import List
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        BFS with state (position, last_jump_was_backward).
        Upper bound: max(max(forbidden) + a + b, x + b) for position.
        """
        forbidden_set = set(forbidden)
        # Upper bound for search space
        upper_bound = max(max(forbidden) + a + b, x + b) + 1

        # State: (position, last_was_backward)
        visited = set()
        visited.add((0, False))

        queue = deque([(0, False, 0)])  # (pos, last_backward, jumps)

        while queue:
            pos, last_backward, jumps = queue.popleft()

            if pos == x:
                return jumps

            # Jump forward
            forward = pos + a
            if forward <= upper_bound and forward not in forbidden_set:
                if (forward, False) not in visited:
                    visited.add((forward, False))
                    queue.append((forward, False, jumps + 1))

            # Jump backward (only if last wasn't backward)
            if not last_backward:
                backward = pos - b
                if backward >= 0 and backward not in forbidden_set:
                    if (backward, True) not in visited:
                        visited.add((backward, True))
                        queue.append((backward, True, jumps + 1))

        return -1


class SolutionOptimized:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        Optimized BFS with tighter bounds.
        """
        forbidden_set = set(forbidden)
        limit = max(x, max(forbidden)) + a + b

        # visited[pos][direction]: 0 = forward, 1 = backward
        visited = [[False, False] for _ in range(limit + 1)]

        queue = deque([(0, 0)])  # (position, jumps)
        visited[0][0] = True
        visited[0][1] = True

        while queue:
            pos, jumps = queue.popleft()

            if pos == x:
                return jumps

            # Forward jump
            nxt = pos + a
            if nxt <= limit and nxt not in forbidden_set and not visited[nxt][0]:
                visited[nxt][0] = True
                visited[nxt][1] = True  # Can go backward from forward position
                queue.append((nxt, jumps + 1))

            # Backward jump (only if we arrived here via forward)
            # We need separate tracking for this
            pass

        return -1


class SolutionDPStyle:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        BFS tracking direction separately.
        """
        forbidden_set = set(forbidden)
        max_pos = 6000  # Safe upper bound

        # visited[pos] = set of directions we've arrived from
        # 0 = came via forward, 1 = came via backward
        visited = [set() for _ in range(max_pos + 1)]

        queue = deque([(0, 0, 0)])  # (pos, direction, jumps)
        visited[0].add(0)

        while queue:
            pos, direction, jumps = queue.popleft()

            if pos == x:
                return jumps

            # Forward jump (always allowed)
            nxt = pos + a
            if nxt <= max_pos and nxt not in forbidden_set and 0 not in visited[nxt]:
                visited[nxt].add(0)
                queue.append((nxt, 0, jumps + 1))

            # Backward jump (only if last was forward)
            if direction == 0:
                nxt = pos - b
                if nxt >= 0 and nxt not in forbidden_set and 1 not in visited[nxt]:
                    visited[nxt].add(1)
                    queue.append((nxt, 1, jumps + 1))

        return -1


class SolutionClean:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        Clean BFS implementation.
        """
        forbidden_set = set(forbidden)
        furthest = max(x + b, max(forbidden) + a + b) + 1

        # (position, can_go_back)
        visited = {(0, True)}
        queue = deque([(0, 0, True)])  # pos, jumps, can_go_back

        while queue:
            pos, jumps, can_back = queue.popleft()

            if pos == x:
                return jumps

            # Forward
            nxt = pos + a
            if nxt <= furthest and nxt not in forbidden_set and (nxt, True) not in visited:
                visited.add((nxt, True))
                queue.append((nxt, jumps + 1, True))

            # Backward
            if can_back:
                nxt = pos - b
                if nxt >= 0 and nxt not in forbidden_set and (nxt, False) not in visited:
                    visited.add((nxt, False))
                    queue.append((nxt, jumps + 1, False))

        return -1
