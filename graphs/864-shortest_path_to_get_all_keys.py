#864. Shortest Path to Get All Keys
#Hard
#
#You are given an m x n grid where:
#- '.' is an empty cell.
#- '#' is a wall.
#- '@' is the starting point.
#- Lowercase letters represent keys.
#- Uppercase letters represent locks.
#
#You start at the starting point and one move consists of walking one space in
#one of the four cardinal directions. You cannot walk outside the grid, or walk
#into a wall.
#
#If you walk over a key, you can pick it up and you don't have to stop. You cannot
#walk over a lock unless you have the corresponding key.
#
#Return the minimum number of moves to acquire all keys. If it is impossible,
#return -1.
#
#Example 1:
#Input: grid = ["@.a..","###.#","b.A.B"]
#Output: 8
#
#Example 2:
#Input: grid = ["@..aA","..B#.","....b"]
#Output: 6
#
#Example 3:
#Input: grid = ["@Aa"]
#Output: -1
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 30
#    grid[i][j] is either an English letter, '.', '#', or '@'.
#    There is exactly one '@' in the grid.
#    The number of keys in the grid is in the range [1, 6].
#    Each key in the grid is unique.
#    Each lock in the grid has a corresponding key.

from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        """
        BFS with state = (row, col, keys_bitmask).
        """
        m, n = len(grid), len(grid[0])

        # Find start and count keys
        start = None
        num_keys = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    num_keys += 1

        target_keys = (1 << num_keys) - 1

        # BFS: (row, col, keys)
        queue = deque([(start[0], start[1], 0, 0)])  # row, col, keys, steps
        visited = {(start[0], start[1], 0)}

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c, keys, steps = queue.popleft()

            if keys == target_keys:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '#':
                    cell = grid[nr][nc]
                    new_keys = keys

                    # Check if lock without key
                    if cell.isupper():
                        key_bit = 1 << (ord(cell.lower()) - ord('a'))
                        if not (keys & key_bit):
                            continue

                    # Pick up key
                    if cell.islower():
                        new_keys |= (1 << (ord(cell) - ord('a')))

                    state = (nr, nc, new_keys)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, new_keys, steps + 1))

        return -1


class SolutionOptimized:
    """Optimized with tuple states"""

    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        all_keys = 0
        start = None

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == '@':
                    start = (i, j)
                elif c.islower():
                    all_keys |= 1 << (ord(c) - ord('a'))

        queue = deque([(start[0], start[1], 0)])
        visited = {(start[0], start[1], 0)}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c, keys = queue.popleft()

                if keys == all_keys:
                    return steps

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        cell = grid[nr][nc]
                        new_keys = keys

                        if cell == '#':
                            continue
                        if cell.isupper() and not (keys & (1 << (ord(cell) - ord('A')))):
                            continue
                        if cell.islower():
                            new_keys |= 1 << (ord(cell) - ord('a'))

                        if (nr, nc, new_keys) not in visited:
                            visited.add((nr, nc, new_keys))
                            queue.append((nr, nc, new_keys))

            steps += 1

        return -1
