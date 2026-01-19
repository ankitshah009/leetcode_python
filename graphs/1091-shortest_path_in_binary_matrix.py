#1091. Shortest Path in Binary Matrix
#Medium
#
#Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
#If there is no clear path, return -1.
#
#A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the
#bottom-right cell (i.e., (n - 1, n - 1)) such that:
#    All the visited cells of the path are 0.
#    All the adjacent cells of the path are 8-directionally connected (i.e., they are different
#    and they share an edge or a corner).
#
#The length of a clear path is the number of visited cells of this path.
#
#Example 1:
#Input: grid = [[0,1],[1,0]]
#Output: 2
#
#Example 2:
#Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
#Output: 4
#
#Example 3:
#Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
#Output: -1
#
#Constraints:
#    n == grid.length
#    n == grid[i].length
#    1 <= n <= 100
#    grid[i][j] is 0 or 1

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8 directions (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited

        while queue:
            row, col, length = queue.popleft()

            if row == n - 1 and col == n - 1:
                return length

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1  # Mark as visited
                    queue.append((new_row, new_col, length + 1))

        return -1
