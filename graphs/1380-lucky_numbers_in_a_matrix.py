#1380. Lucky Numbers in a Matrix
#Easy
#
#Given an m x n matrix of distinct numbers, return all lucky numbers in the
#matrix in any order.
#
#A lucky number is an element of the matrix such that it is the minimum element
#in its row and maximum in its column.
#
#Example 1:
#Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
#Output: [15]
#Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#Example 2:
#Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
#Output: [12]
#
#Example 3:
#Input: matrix = [[7,8],[1,2]]
#Output: [7]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= n, m <= 50
#    1 <= matrix[i][j] <= 10^5
#    All elements in the matrix are distinct.

from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        Find intersection of row minimums and column maximums.
        """
        m, n = len(matrix), len(matrix[0])

        # Find minimum in each row
        row_mins = {min(row) for row in matrix}

        # Find maximum in each column
        col_maxs = {max(matrix[i][j] for i in range(m)) for j in range(n)}

        # Lucky numbers are in both sets
        return list(row_mins & col_maxs)


class SolutionExplicit:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """More explicit approach"""
        m, n = len(matrix), len(matrix[0])

        # Find min in each row with position
        row_mins = []
        for i in range(m):
            min_val = min(matrix[i])
            min_col = matrix[i].index(min_val)
            row_mins.append((min_val, i, min_col))

        # Check if any row minimum is also column maximum
        result = []
        for val, row, col in row_mins:
            col_max = max(matrix[i][col] for i in range(m))
            if val == col_max:
                result.append(val)

        return result


class SolutionSinglePass:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        There can be at most one lucky number.
        Lucky number = max of row minimums = min of column maximums
        """
        row_mins = [min(row) for row in matrix]
        col_maxs = [max(col) for col in zip(*matrix)]

        max_of_row_mins = max(row_mins)
        min_of_col_maxs = min(col_maxs)

        if max_of_row_mins == min_of_col_maxs:
            return [max_of_row_mins]
        return []
