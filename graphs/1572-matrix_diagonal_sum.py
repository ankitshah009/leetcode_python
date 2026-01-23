#1572. Matrix Diagonal Sum
#Easy
#
#Given a square matrix mat, return the sum of the matrix diagonals.
#
#Only include the sum of all the elements on the primary diagonal and all the
#elements on the secondary diagonal that are not part of the primary diagonal.
#
#Example 1:
#Input: mat = [[1,2,3],
#              [4,5,6],
#              [7,8,9]]
#Output: 25
#Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
#Notice that element mat[1][1] = 5 is counted only once.
#
#Example 2:
#Input: mat = [[1,1,1,1],
#              [1,1,1,1],
#              [1,1,1,1],
#              [1,1,1,1]]
#Output: 8
#
#Example 3:
#Input: mat = [[5]]
#Output: 5
#
#Constraints:
#    n == mat.length == mat[i].length
#    1 <= n <= 100
#    1 <= mat[i][j] <= 100

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Sum both diagonals, subtract center if n is odd.
        """
        n = len(mat)
        total = 0

        for i in range(n):
            # Primary diagonal
            total += mat[i][i]
            # Secondary diagonal
            total += mat[i][n - 1 - i]

        # If n is odd, center element was counted twice
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total


class SolutionSingleLoop:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Single loop with condition for center.
        """
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]  # Primary
            if i != n - 1 - i:  # Avoid double counting center
                total += mat[i][n - 1 - i]  # Secondary

        return total


class SolutionComprehension:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Using list comprehension.
        """
        n = len(mat)
        primary = sum(mat[i][i] for i in range(n))
        secondary = sum(mat[i][n - 1 - i] for i in range(n))
        center = mat[n // 2][n // 2] if n % 2 == 1 else 0

        return primary + secondary - center


class SolutionNumpy:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Using numpy (if available).
        """
        try:
            import numpy as np
            arr = np.array(mat)
            primary = np.trace(arr)
            secondary = np.trace(np.fliplr(arr))
            n = len(mat)
            center = arr[n // 2][n // 2] if n % 2 == 1 else 0
            return int(primary + secondary - center)
        except ImportError:
            return Solution().diagonalSum(mat)
