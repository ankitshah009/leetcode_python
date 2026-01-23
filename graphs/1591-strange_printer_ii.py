#1591. Strange Printer II
#Hard
#
#There is a strange printer with the following two special requirements:
#- On each turn, the printer will print a solid rectangular pattern of a single
#  color on the grid. This will cover up the existing colors in the rectangle.
#- Once the printer has used a color for the above operation, the same color
#  cannot be used again.
#
#You are given a m x n matrix targetGrid, where targetGrid[row][col] is the
#color in the position (row, col) of the grid.
#
#Return true if it is possible to print the matrix targetGrid, otherwise,
#return false.
#
#Example 1:
#Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
#Output: true
#
#Example 2:
#Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
#Output: true
#
#Example 3:
#Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
#Output: false
#Explanation: It's impossible to print because one color's rectangle would
#have to cover another color's rectangle.
#
#Constraints:
#    m == targetGrid.length
#    n == targetGrid[i].length
#    1 <= m, n <= 60
#    1 <= targetGrid[row][col] <= 60

from typing import List
from collections import defaultdict

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        """
        Key insight: A color c1 must be printed before c2 if c2 appears
        inside c1's bounding rectangle but c2 is different from c1.

        This creates a dependency graph. If there's a cycle, it's impossible.
        Use topological sort to detect cycles.
        """
        m, n = len(targetGrid), len(targetGrid[0])

        # Find bounding box for each color
        colors = set()
        for row in targetGrid:
            colors.update(row)

        # min_row, max_row, min_col, max_col for each color
        bounds = {}
        for c in colors:
            min_r, max_r = m, -1
            min_c, max_c = n, -1
            for i in range(m):
                for j in range(n):
                    if targetGrid[i][j] == c:
                        min_r = min(min_r, i)
                        max_r = max(max_r, i)
                        min_c = min(min_c, j)
                        max_c = max(max_c, j)
            bounds[c] = (min_r, max_r, min_c, max_c)

        # Build dependency graph
        # If color c2 appears in c1's bounding box, c1 must be printed before c2
        # i.e., c1 -> c2 (c1 depends on c2 being printed after)
        # Actually, we want: c2 -> c1 (c2 must be printed before c1)
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        for c in colors:
            in_degree[c] = 0

        for c1 in colors:
            min_r, max_r, min_c, max_c = bounds[c1]
            for i in range(min_r, max_r + 1):
                for j in range(min_c, max_c + 1):
                    c2 = targetGrid[i][j]
                    if c2 != c1 and c1 not in graph[c2]:
                        # c2 must be printed after c1
                        # So c1 -> c2 in our "must print before" graph
                        graph[c1].add(c2)
                        in_degree[c2] += 1

        # Topological sort using Kahn's algorithm
        from collections import deque
        queue = deque([c for c in colors if in_degree[c] == 0])
        count = 0

        while queue:
            c = queue.popleft()
            count += 1
            for neighbor in graph[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == len(colors)


class SolutionDFS:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        """
        DFS approach for cycle detection.
        """
        m, n = len(targetGrid), len(targetGrid[0])

        # Find colors and their bounding boxes
        color_bounds = {}
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c not in color_bounds:
                    color_bounds[c] = [i, i, j, j]  # min_r, max_r, min_c, max_c
                else:
                    color_bounds[c][0] = min(color_bounds[c][0], i)
                    color_bounds[c][1] = max(color_bounds[c][1], i)
                    color_bounds[c][2] = min(color_bounds[c][2], j)
                    color_bounds[c][3] = max(color_bounds[c][3], j)

        # Build graph: c1 -> c2 means c1 must be printed before c2
        graph = defaultdict(set)

        for c1, (min_r, max_r, min_c, max_c) in color_bounds.items():
            for i in range(min_r, max_r + 1):
                for j in range(min_c, max_c + 1):
                    c2 = targetGrid[i][j]
                    if c1 != c2:
                        graph[c1].add(c2)

        # DFS for cycle detection
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = {c: 0 for c in color_bounds}

        def has_cycle(node):
            if state[node] == 1:
                return True  # Back edge found
            if state[node] == 2:
                return False  # Already processed

            state[node] = 1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            state[node] = 2
            return False

        for color in color_bounds:
            if has_cycle(color):
                return False

        return True


class SolutionSimulation:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        """
        Simulation approach: Repeatedly remove colors that can be fully covered.
        """
        m, n = len(targetGrid), len(targetGrid[0])
        grid = [row[:] for row in targetGrid]  # Copy

        def get_bounds(color):
            min_r, max_r = m, -1
            min_c, max_c = n, -1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == color:
                        min_r = min(min_r, i)
                        max_r = max(max_r, i)
                        min_c = min(min_c, j)
                        max_c = max(max_c, j)
            return min_r, max_r, min_c, max_c

        def can_erase(color):
            min_r, max_r, min_c, max_c = get_bounds(color)
            if min_r > max_r:
                return False  # Color not found

            # Check if all cells in bounding box are either color or 0 (erased)
            for i in range(min_r, max_r + 1):
                for j in range(min_c, max_c + 1):
                    if grid[i][j] != color and grid[i][j] != 0:
                        return False
            return True

        def erase(color):
            min_r, max_r, min_c, max_c = get_bounds(color)
            for i in range(min_r, max_r + 1):
                for j in range(min_c, max_c + 1):
                    if grid[i][j] == color:
                        grid[i][j] = 0

        colors = set()
        for row in grid:
            colors.update(row)
        colors.discard(0)

        while colors:
            erased = False
            for c in list(colors):
                if can_erase(c):
                    erase(c)
                    colors.remove(c)
                    erased = True
                    break

            if not erased:
                return False

        return True
