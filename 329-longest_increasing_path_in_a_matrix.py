#329. Longest Increasing Path in a Matrix
#Hard
#
#Given an m x n integers matrix, return the length of the longest increasing path in matrix.
#
#From each cell, you can either move in four directions: left, right, up, or down. You may not
#move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
#
#Example 1:
#Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
#Output: 4
#Explanation: The longest increasing path is [1, 2, 6, 9].
#
#Example 2:
#Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
#Output: 4
#Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
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

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            max_length = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_length = max(max_length, 1 + dfs(ni, nj))

            memo[(i, j)] = max_length
            return max_length

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
