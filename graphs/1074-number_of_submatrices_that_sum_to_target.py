#1074. Number of Submatrices That Sum to Target
#Hard
#
#Given a matrix and a target, return the number of non-empty submatrices
#that sum to target.
#
#A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with
#x1 <= x <= x2 and y1 <= y <= y2.
#
#Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different
#if they have some coordinate that is different: for example, if x1 != x1'.
#
#Example 1:
#Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
#Output: 4
#Explanation: The four 1x1 submatrices that only contain 0.
#
#Example 2:
#Input: matrix = [[1,-1],[-1,1]], target = 0
#Output: 5
#Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus
#the 2x2 submatrix.
#
#Example 3:
#Input: matrix = [[904]], target = 0
#Output: 0
#
#Constraints:
#    1 <= matrix.length <= 100
#    1 <= matrix[0].length <= 100
#    -1000 <= matrix[i][j] <= 1000
#    -10^8 <= target <= 10^8

from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Fix left and right columns, reduce to 1D subarray sum problem.
        Use prefix sum and hash map for O(n) subarray counting.
        """
        m, n = len(matrix), len(matrix[0])
        result = 0

        # Compute prefix sums for each row
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j - 1]

        # Fix left and right columns
        for left in range(n):
            for right in range(left, n):
                # 1D array: sum of elements from column left to right for each row
                prefix_count = defaultdict(int)
                prefix_count[0] = 1
                prefix_sum = 0

                for i in range(m):
                    # Sum of row i from column left to right
                    row_sum = matrix[i][right] - (matrix[i][left - 1] if left > 0 else 0)
                    prefix_sum += row_sum

                    # Count subarrays with sum = target
                    result += prefix_count[prefix_sum - target]
                    prefix_count[prefix_sum] += 1

        return result


class SolutionPrefixMatrix:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """Using 2D prefix sum matrix"""
        m, n = len(matrix), len(matrix[0])

        # Build 2D prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = matrix[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

        def get_sum(r1, c1, r2, c2):
            return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]

        result = 0
        # Fix top and bottom rows
        for r1 in range(m):
            for r2 in range(r1, m):
                count = defaultdict(int)
                count[0] = 1
                for c in range(n):
                    col_sum = get_sum(r1, 0, r2, c)
                    result += count[col_sum - target]
                    count[col_sum] += 1

        return result
