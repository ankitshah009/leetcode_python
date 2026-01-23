#1314. Matrix Block Sum
#Medium
#
#Given a m x n matrix mat and an integer k, return a matrix answer where each
#answer[i][j] is the sum of all elements mat[r][c] for:
#    i - k <= r <= i + k,
#    j - k <= c <= j + k, and
#    (r, c) is a valid position in the matrix.
#
#Example 1:
#Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
#Output: [[12,21,16],[27,45,33],[24,39,28]]
#
#Example 2:
#Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
#Output: [[45,45,45],[45,45,45],[45,45,45]]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n, k <= 100
#    1 <= mat[i][j] <= 100

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        Use 2D prefix sum for O(1) range queries.
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        def get_sum(r1, c1, r2, c2):
            """Get sum of submatrix from (r1,c1) to (r2,c2) inclusive, 0-indexed"""
            # Clamp to valid range
            r1, c1 = max(0, r1), max(0, c1)
            r2, c2 = min(m - 1, r2), min(n - 1, c2)
            # Convert to 1-indexed for prefix sum
            return prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]

        # Build result
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = get_sum(i - k, j - k, i + k, j + k)

        return result


class SolutionBruteForce:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """O(m*n*k^2) brute force approach"""
        m, n = len(mat), len(mat[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                for r in range(max(0, i - k), min(m, i + k + 1)):
                    for c in range(max(0, j - k), min(n, j + k + 1)):
                        total += mat[r][c]
                result[i][j] = total

        return result
