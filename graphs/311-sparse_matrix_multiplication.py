#311. Sparse Matrix Multiplication
#Medium
#
#Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return
#the result of mat1 x mat2. You may assume that multiplication is always possible.
#
#Example 1:
#Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
#Output: [[7,0,0],[-7,0,3]]
#
#Example 2:
#Input: mat1 = [[0]], mat2 = [[0]]
#Output: [[0]]
#
#Constraints:
#    m == mat1.length
#    k == mat1[i].length == mat2.length
#    n == mat2[i].length
#    1 <= m, n, k <= 100
#    -100 <= mat1[i][j], mat2[i][j] <= 100

from typing import List
from collections import defaultdict

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """Sparse matrix multiplication - skip zeros"""
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:  # Skip zero elements
                    for l in range(n):
                        if mat2[j][l] != 0:  # Skip zero elements
                            result[i][l] += mat1[i][j] * mat2[j][l]

        return result


class SolutionCompressed:
    """Using compressed sparse representation"""

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        # Compress mat1: for each row, store (col, val) pairs
        sparse1 = []
        for i in range(m):
            row = [(j, mat1[i][j]) for j in range(k) if mat1[i][j] != 0]
            sparse1.append(row)

        # Compress mat2: for each column, store (row, val) pairs
        sparse2 = [[] for _ in range(n)]
        for i in range(k):
            for j in range(n):
                if mat2[i][j] != 0:
                    sparse2[j].append((i, mat2[i][j]))

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for col1, val1 in sparse1[i]:
                for j in range(n):
                    for row2, val2 in sparse2[j]:
                        if col1 == row2:
                            result[i][j] += val1 * val2

        return result


class SolutionDict:
    """Using dictionary for sparse representation"""

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        # Store mat1 as {row: {col: val}}
        sparse1 = defaultdict(dict)
        for i in range(m):
            for j in range(k):
                if mat1[i][j]:
                    sparse1[i][j] = mat1[i][j]

        # Store mat2 as {col: {row: val}}
        sparse2 = defaultdict(dict)
        for i in range(k):
            for j in range(n):
                if mat2[i][j]:
                    sparse2[j][i] = mat2[i][j]

        result = [[0] * n for _ in range(m)]

        for i in sparse1:
            for j in sparse2:
                total = 0
                for idx in sparse1[i]:
                    if idx in sparse2[j]:
                        total += sparse1[i][idx] * sparse2[j][idx]
                result[i][j] = total

        return result
