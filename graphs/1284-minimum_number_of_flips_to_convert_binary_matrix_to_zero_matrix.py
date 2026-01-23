#1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
#Hard
#
#Given a m x n binary matrix mat. In one step, you can choose one cell and flip
#it and all the four neighbors of it if they exist (Flip is changing 1 to 0
#and 0 to 1). A pair of cells are called neighbors if they share one edge.
#
#Return the minimum number of steps required to convert mat to a zero matrix
#or -1 if you cannot.
#
#A binary matrix is a matrix with all cells equal to 0 or 1 only.
#
#A zero matrix is a matrix with all cells equal to 0.
#
#Example 1:
#Input: mat = [[0,0],[0,1]]
#Output: 3
#Explanation: One possible solution is to flip (1, 0) then (0, 1) then (1, 1).
#
#Example 2:
#Input: mat = [[0]]
#Output: 0
#Explanation: Given matrix is a zero matrix. We do not need to change it.
#
#Example 3:
#Input: mat = [[1,0,0],[1,0,0]]
#Output: -1
#Explanation: Given matrix cannot be a zero matrix.
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 3
#    mat[i][j] is either 0 or 1.

from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        """
        BFS with state encoded as bitmask.
        State space is at most 2^9 = 512 (3x3 matrix).
        """
        m, n = len(mat), len(mat[0])

        # Encode initial state as bitmask
        def to_mask(matrix):
            mask = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]:
                        mask |= 1 << (i * n + j)
            return mask

        def flip(mask, r, c):
            """Flip cell (r,c) and its neighbors"""
            for dr, dc in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    mask ^= 1 << (nr * n + nc)
            return mask

        start = to_mask(mat)

        if start == 0:
            return 0

        # BFS
        visited = {start}
        queue = deque([(start, 0)])

        while queue:
            state, steps = queue.popleft()

            # Try flipping each cell
            for i in range(m):
                for j in range(n):
                    new_state = flip(state, i, j)

                    if new_state == 0:
                        return steps + 1

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))

        return -1


class SolutionBitmaskEnum:
    def minFlips(self, mat: List[List[int]]) -> int:
        """
        Enumerate all possible flip combinations.
        Each cell can be flipped at most once (flipping twice cancels out).
        """
        m, n = len(mat), len(mat[0])
        total_cells = m * n

        def flip_result(flip_mask):
            """Apply flip_mask and return resulting matrix state"""
            result = [[mat[i][j] for j in range(n)] for i in range(m)]

            for idx in range(total_cells):
                if flip_mask & (1 << idx):
                    r, c = idx // n, idx % n
                    # Flip cell and neighbors
                    for dr, dc in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            result[nr][nc] ^= 1

            return result

        def is_zero(matrix):
            return all(matrix[i][j] == 0 for i in range(m) for j in range(n))

        min_flips = float('inf')

        for flip_mask in range(1 << total_cells):
            result = flip_result(flip_mask)
            if is_zero(result):
                flips = bin(flip_mask).count('1')
                min_flips = min(min_flips, flips)

        return min_flips if min_flips != float('inf') else -1
