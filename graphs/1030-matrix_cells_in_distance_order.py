#1030. Matrix Cells in Distance Order
#Easy
#
#You are given four integers row, cols, rCenter, and cCenter. There is a
#rows x cols matrix and you are on the cell with the coordinates (rCenter,
#cCenter).
#
#Return the coordinates of all cells in the matrix, sorted by their distance
#from (rCenter, cCenter) from the smallest distance to the largest distance.
#You may return the answer in any order that satisfies this condition.
#
#The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
#
#Example 1:
#Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
#Output: [[0,0],[0,1]]
#Explanation: The distances from (0, 0) to other cells are: [0,1]
#
#Example 2:
#Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
#Output: [[0,1],[0,0],[1,1],[1,0]]
#Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
#
#Example 3:
#Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
#Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
#Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
#
#Constraints:
#    1 <= rows, cols <= 100
#    0 <= rCenter < rows
#    0 <= cCenter < cols

from typing import List
from collections import deque

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        Simple sort by Manhattan distance.
        """
        cells = [[r, c] for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return cells


class SolutionBFS:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        BFS from center cell - naturally returns cells in distance order.
        """
        result = []
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(rCenter, cCenter)])
        visited[rCenter][cCenter] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            result.append([r, c])

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return result


class SolutionBucketSort:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        """
        Bucket sort: group cells by distance.
        Max distance is (rows-1) + (cols-1).
        """
        max_dist = rows + cols - 2
        buckets = [[] for _ in range(max_dist + 1)]

        for r in range(rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                buckets[dist].append([r, c])

        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result
