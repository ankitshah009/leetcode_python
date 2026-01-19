#542. 01 Matrix
#Medium
#
#Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
#The distance between two adjacent cells is 1.
#
#Example 1:
#Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
#Output: [[0,0,0],[0,1,0],[0,0,0]]
#
#Example 2:
#Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
#Output: [[0,0,0],[0,1,0],[1,2,1]]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 10^4
#    1 <= m * n <= 10^4
#    mat[i][j] is either 0 or 1.
#    There is at least one 0 in mat.

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Multi-source BFS from all 0s
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    if mat[new_row][new_col] > mat[row][col] + 1:
                        mat[new_row][new_col] = mat[row][col] + 1
                        queue.append((new_row, new_col))

        return mat
