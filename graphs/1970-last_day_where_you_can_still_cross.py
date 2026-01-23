#1970. Last Day Where You Can Still Cross
#Hard
#
#There is a 1-indexed binary matrix where 0 represents land and 1 represents
#water. You are given integers row and col representing the number of rows and
#columns in the matrix, respectively.
#
#Initially on day 0, the entire matrix is land. However, each day a new cell
#becomes flooded with water. You are given a 1-indexed 2D array cells, where
#cells[i] = [ri, ci] represents that on day i, the cell on row ri and column ci
#(1-indexed) will be covered with water (i.e., changed to 1).
#
#You want to find the last day that it is possible to walk from the top to the
#bottom by only walking on land cells. You can start from any cell in the top
#row and end at any cell in the bottom row. You can only travel in the four
#cardinal directions (left, right, up, and down).
#
#Return the last day where it is possible to walk from the top to the bottom
#by only walking on land cells.
#
#Example 1:
#Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
#Output: 2
#
#Example 2:
#Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
#Output: 1
#
#Example 3:
#Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
#Output: 3
#
#Constraints:
#    2 <= row, col <= 2 * 10^4
#    4 <= row * col <= 2 * 10^4
#    cells.length == row * col
#    1 <= ri <= row
#    1 <= ci <= col
#    All the values of cells are unique.

from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        Binary search on day + BFS to check connectivity.
        """
        def can_cross(day: int) -> bool:
            # Create grid with first 'day' cells flooded
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            # BFS from top row to bottom row
            queue = deque()
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = 1  # Mark visited

            while queue:
                r, c = queue.popleft()

                if r == row - 1:
                    return True

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

            return False

        lo, hi = 1, len(cells)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_cross(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo


class SolutionUnionFind:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        Reverse process: add land cells and use Union-Find.
        Find first day (from end) when top connects to bottom.
        """
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Virtual nodes for top and bottom
        TOP, BOTTOM = (-1, -1), (-2, -2)
        parent[TOP] = TOP
        parent[BOTTOM] = BOTTOM

        grid = [[1] * col for _ in range(row)]  # Start all water

        # Process in reverse
        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            grid[r][c] = 0
            parent[(r, c)] = (r, c)

            # Connect to top/bottom virtual nodes
            if r == 0:
                union((r, c), TOP)
            if r == row - 1:
                union((r, c), BOTTOM)

            # Connect to adjacent land cells
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    union((r, c), (nr, nc))

            # Check if top connects to bottom
            if find(TOP) == find(BOTTOM):
                return day

        return 0
