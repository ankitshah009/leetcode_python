#566. Reshape the Matrix
#Easy
#
#In MATLAB, there is a handy function called reshape which can reshape an m x n
#matrix into a new one with a different size r x c keeping its original data.
#
#You are given an m x n matrix mat and two integers r and c representing the number
#of rows and the number of columns of the wanted reshaped matrix.
#
#The reshaped matrix should be filled with all the elements of the original matrix
#in the same row-traversing order as they were.
#
#If the reshape operation with given parameters is possible and legal, output the
#new reshaped matrix; Otherwise, output the original matrix.
#
#Example 1:
#Input: mat = [[1,2],[3,4]], r = 1, c = 4
#Output: [[1,2,3,4]]
#
#Example 2:
#Input: mat = [[1,2],[3,4]], r = 2, c = 4
#Output: [[1,2],[3,4]]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 100
#    -1000 <= mat[i][j] <= 1000
#    1 <= r, c <= 300

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """Flatten and reshape"""
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        # Flatten
        flat = [mat[i][j] for i in range(m) for j in range(n)]

        # Reshape
        return [flat[i * c:(i + 1) * c] for i in range(r)]


class SolutionIndexMapping:
    """Direct index mapping without flattening"""

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(m * n):
            result[i // c][i % c] = mat[i // n][i % n]

        return result


class SolutionGenerator:
    """Using generator"""

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        def elements():
            for row in mat:
                for val in row:
                    yield val

        gen = elements()
        return [[next(gen) for _ in range(c)] for _ in range(r)]


class SolutionNumpy:
    """Using numpy (for reference)"""

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np

        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        return np.array(mat).reshape(r, c).tolist()
