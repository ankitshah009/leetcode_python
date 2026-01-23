#1901. Find a Peak Element II
#Medium
#
#A peak element in a 2D grid is an element that is strictly greater than all of
#its adjacent neighbors to the left, right, top, and bottom.
#
#Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find
#any peak element mat[i][j] and return the length 2 array [i,j].
#
#You may assume that the entire matrix is surrounded by an outer perimeter with
#the value -1 in each cell.
#
#You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
#
#Example 1:
#Input: mat = [[1,4],[3,2]]
#Output: [0,1]
#
#Example 2:
#Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
#Output: [1,1]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 500
#    1 <= mat[i][j] <= 10^5
#    No two adjacent cells are equal.

from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        Binary search on rows, find column max in each iteration.
        """
        m, n = len(mat), len(mat[0])
        lo, hi = 0, m - 1

        while lo < hi:
            mid = (lo + hi) // 2

            # Find max column in row mid
            max_col = 0
            for j in range(n):
                if mat[mid][j] > mat[mid][max_col]:
                    max_col = j

            # Compare with adjacent rows
            if mat[mid][max_col] < mat[mid + 1][max_col]:
                lo = mid + 1
            else:
                hi = mid

        # Find max column in row lo
        max_col = 0
        for j in range(n):
            if mat[lo][j] > mat[lo][max_col]:
                max_col = j

        return [lo, max_col]


class SolutionColumn:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        Binary search on columns.
        """
        m, n = len(mat), len(mat[0])
        lo, hi = 0, n - 1

        while lo < hi:
            mid = (lo + hi) // 2

            # Find max row in column mid
            max_row = 0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            # Compare with adjacent columns
            if mat[max_row][mid] < mat[max_row][mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        # Find max row in column lo
        max_row = 0
        for i in range(m):
            if mat[i][lo] > mat[max_row][lo]:
                max_row = i

        return [max_row, lo]
