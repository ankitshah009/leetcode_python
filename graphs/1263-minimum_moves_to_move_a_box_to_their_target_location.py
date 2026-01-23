#1263. Minimum Moves to Move a Box to Their Target Location
#Hard
#
#A storekeeper is a game in which the player pushes boxes around in a warehouse
#trying to get them to target locations.
#
#The game is represented by an m x n grid of characters grid where each element
#is a wall, floor, or box.
#
#Your task is to move the box 'B' to the target position 'T' under the following rules:
#    The character 'S' represents the player. The player can move up, down, left,
#    right in grid if it is a floor (empty cell).
#    The character '.' represents the floor which means a free cell to walk.
#    The character '#' represents the wall which means an obstacle.
#    There is only one box 'B' and one target cell 'T' in the grid.
#    The box can be moved to an adjacent free cell by standing next to the box
#    and then moving in the direction of the box. This is a push.
#    The player cannot walk through the box.
#
#Return the minimum number of pushes to move the box to the target. If there is
#no way to reach the target, return -1.
#
#Example 1:
#Input: grid = [["#","#","#","#","#","#"],
#               ["#","T","#","#","#","#"],
#               ["#",".",".","B",".","#"],
#               ["#",".","#","#",".","#"],
#               ["#",".",".",".","S","#"],
#               ["#","#","#","#","#","#"]]
#Output: 3
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 20
#    grid contains only characters '.', '#', 'S', 'T', and 'B'.
#    There is only one 'S', 'B', and 'T' in the grid.

from typing import List
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        BFS with state = (box_position, player_position).
        Use 0-1 BFS: Moving player costs 0, pushing box costs 1.
        """
        m, n = len(grid), len(grid[0])

        # Find initial positions
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_valid(r, c, box_pos):
            return 0 <= r < m and 0 <= c < n and grid[r][c] != '#' and (r, c) != box_pos

        def can_reach(start, end, box_pos):
            """Check if player can reach 'end' from 'start' without moving box"""
            if start == end:
                return True

            visited = {start}
            queue = deque([start])

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc, box_pos) and (nr, nc) not in visited:
                        if (nr, nc) == end:
                            return True
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return False

        # BFS on (box_pos, player_pos, pushes)
        # Actually, we only need (box_pos, player_pos) since we want min pushes
        # Use deque and add push moves to end, non-push moves to front (0-1 BFS)

        # Simpler: BFS where each state is (box_pos, player_pos) and we count pushes
        visited = set()
        queue = deque([(box, player, 0)])  # (box_pos, player_pos, pushes)
        visited.add((box, player))

        while queue:
            (bx, by), (px, py), pushes = queue.popleft()

            if (bx, by) == target:
                return pushes

            # Try to push box in each direction
            for dr, dc in directions:
                # New box position
                new_bx, new_by = bx + dr, by + dc

                # Player needs to be on opposite side of box
                player_needed = (bx - dr, by - dc)

                # Check if push is valid
                if (0 <= new_bx < m and 0 <= new_by < n and
                    grid[new_bx][new_by] != '#' and
                    is_valid(player_needed[0], player_needed[1], (bx, by)) and
                    can_reach((px, py), player_needed, (bx, by))):

                    new_state = ((new_bx, new_by), (bx, by))  # Player moves to old box position
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(((new_bx, new_by), (bx, by), pushes + 1))

        return -1
