#1329. Sort the Matrix Diagonally
#Medium
#
#A matrix diagonal is a diagonal line of cells starting from some cell in
#either the topmost row or leftmost column and going in the bottom-right
#direction until reaching the matrix's end.
#
#Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
#order and return the resulting matrix.
#
#Example 1:
#Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
#Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#
#Example 2:
#Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
#Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 100
#    1 <= mat[i][j] <= 100

from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Group elements by diagonal (same i-j value), sort, and place back.
        """
        m, n = len(mat), len(mat[0])

        # Group by diagonal (i - j is constant for each diagonal)
        diagonals = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])

        # Sort each diagonal
        for key in diagonals:
            diagonals[key].sort(reverse=True)  # Reverse so we can pop from end

        # Place back
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()

        return mat


class SolutionExplicit:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """Extract, sort, and place each diagonal explicitly"""
        m, n = len(mat), len(mat[0])

        def sort_diagonal(start_row, start_col):
            """Sort diagonal starting at (start_row, start_col)"""
            diagonal = []
            r, c = start_row, start_col

            # Extract diagonal
            while r < m and c < n:
                diagonal.append(mat[r][c])
                r += 1
                c += 1

            # Sort
            diagonal.sort()

            # Place back
            r, c = start_row, start_col
            for val in diagonal:
                mat[r][c] = val
                r += 1
                c += 1

        # Sort all diagonals starting from first column
        for i in range(m):
            sort_diagonal(i, 0)

        # Sort all diagonals starting from first row (except [0,0] already done)
        for j in range(1, n):
            sort_diagonal(0, j)

        return mat


class SolutionHeap:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """Using heapq for sorting"""
        import heapq

        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for i in range(m):
            for j in range(n):
                heapq.heappush(diagonals[i - j], mat[i][j])

        for i in range(m):
            for j in range(n):
                mat[i][j] = heapq.heappop(diagonals[i - j])

        return mat
