#1765. Map of Highest Peak
#Medium
#
#You are given an integer matrix isWater of size m x n that represents a map of
#land and water cells.
#
#- If isWater[i][j] == 0, cell (i, j) is a land cell.
#- If isWater[i][j] == 1, cell (i, j) is a water cell.
#
#You must assign each cell a height in a way that follows these rules:
#- The height of each cell must be non-negative.
#- If the cell is a water cell, its height must be 0.
#- Any two adjacent cells must have an absolute height difference of at most 1.
#
#Find an assignment of heights such that the maximum height in the matrix is
#maximized.
#
#Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s
#height.
#
#Example 1:
#Input: isWater = [[0,1],[0,0]]
#Output: [[1,0],[2,1]]
#
#Example 2:
#Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
#Output: [[1,1,0],[0,1,1],[1,2,2]]
#
#Constraints:
#    m == isWater.length
#    n == isWater[i].length
#    1 <= m, n <= 1000
#    isWater[i][j] is 0 or 1.
#    There is at least one water cell.

from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        Multi-source BFS from all water cells.
        """
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        queue = deque()

        # Initialize water cells
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny))

        return height


class SolutionDP:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """
        DP approach - two passes.
        """
        m, n = len(isWater), len(isWater[0])
        INF = m + n

        # Initialize
        height = [[0 if isWater[i][j] else INF for j in range(n)] for i in range(m)]

        # First pass: top-left to bottom-right
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 0:
                    if i > 0:
                        height[i][j] = min(height[i][j], height[i - 1][j] + 1)
                    if j > 0:
                        height[i][j] = min(height[i][j], height[i][j - 1] + 1)

        # Second pass: bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if isWater[i][j] == 0:
                    if i < m - 1:
                        height[i][j] = min(height[i][j], height[i + 1][j] + 1)
                    if j < n - 1:
                        height[i][j] = min(height[i][j], height[i][j + 1] + 1)

        return height
