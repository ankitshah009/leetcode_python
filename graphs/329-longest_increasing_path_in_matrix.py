#329. Longest Increasing Path in a Matrix
#Hard
#
#Given an m x n integers matrix, return the length of the longest increasing
#path in matrix.
#
#From each cell, you can either move in four directions: left, right, up, or
#down. You may not move diagonally or move outside the boundary (i.e.,
#wrap-around is not allowed).
#
#Example 1:
#Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
#Output: 4
#Explanation: The longest increasing path is [1, 2, 6, 9].
#
#Example 2:
#Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
#Output: 4
#Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is
#not allowed.
#
#Example 3:
#Input: matrix = [[1]]
#Output: 1
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 200
#    0 <= matrix[i][j] <= 2^31 - 1

from typing import List
from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """DFS with memoization"""
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        @lru_cache(maxsize=None)
        def dfs(row, col):
            max_path = 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[row][col]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            return max_path

        return max(dfs(i, j) for i in range(m) for j in range(n))


class SolutionTopSort:
    """Topological sort approach"""

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        from collections import deque

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Calculate in-degree (count of smaller neighbors)
        indegree = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                        indegree[i][j] += 1

        # Start BFS from cells with 0 in-degree (local minima)
        queue = deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i, j))

        length = 0

        while queue:
            length += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            queue.append((ni, nj))

        return length


class SolutionDP:
    """Bottom-up DP by processing cells in sorted order"""

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Sort cells by value
        cells = [(matrix[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()

        dp = [[1] * n for _ in range(m)]

        for val, i, j in cells:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)

        return max(max(row) for row in dp)
