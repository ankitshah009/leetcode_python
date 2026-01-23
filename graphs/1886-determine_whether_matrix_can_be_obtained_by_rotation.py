#1886. Determine Whether Matrix Can Be Obtained By Rotation
#Easy
#
#Given two n x n binary matrices mat and target, return true if it is possible
#to make mat equal to target by rotating mat in 90-degree increments, or false
#otherwise.
#
#Example 1:
#Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
#Output: true
#
#Example 2:
#Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
#Output: false
#
#Example 3:
#Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
#Output: true
#
#Constraints:
#    n == mat.length == target.length
#    n == mat[i].length == target[i].length
#    1 <= n <= 10
#    mat[i][j] and target[i][j] are either 0 or 1.

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Try all 4 rotations (0, 90, 180, 270 degrees).
        """
        def rotate90(matrix: List[List[int]]) -> List[List[int]]:
            """Rotate matrix 90 degrees clockwise."""
            n = len(matrix)
            return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]

        current = mat
        for _ in range(4):
            if current == target:
                return True
            current = rotate90(current)

        return False


class SolutionTranspose:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Rotate using transpose + reverse.
        """
        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            n = len(matrix)
            # Transpose
            transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
            # Reverse each row
            for row in transposed:
                row.reverse()
            return transposed

        current = [row[:] for row in mat]
        for _ in range(4):
            if current == target:
                return True
            current = rotate(current)

        return False


class SolutionZip:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Using zip for rotation.
        """
        for _ in range(4):
            if mat == target:
                return True
            # Rotate 90 degrees: transpose and reverse
            mat = [list(row) for row in zip(*mat[::-1])]

        return False


class SolutionAllAtOnce:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Check all rotations without modifying.
        """
        n = len(mat)

        def matches_rotation(k: int) -> bool:
            """Check if mat rotated k times (90 degrees each) equals target."""
            for i in range(n):
                for j in range(n):
                    # After k rotations, (i,j) in original goes to:
                    # k=0: (i, j)
                    # k=1: (j, n-1-i)
                    # k=2: (n-1-i, n-1-j)
                    # k=3: (n-1-j, i)
                    if k == 0:
                        ni, nj = i, j
                    elif k == 1:
                        ni, nj = j, n - 1 - i
                    elif k == 2:
                        ni, nj = n - 1 - i, n - 1 - j
                    else:
                        ni, nj = n - 1 - j, i

                    if mat[i][j] != target[ni][nj]:
                        return False
            return True

        return any(matches_rotation(k) for k in range(4))
