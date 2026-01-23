#1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#Medium
#
#Given a m x n matrix mat and an integer threshold, return the maximum
#side-length of a square with a sum less than or equal to threshold or return
#0 if there is no such square.
#
#Example 1:
#Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
#Output: 2
#Explanation: The maximum side length of square with sum less than 4 is 2.
#
#Example 2:
#Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
#Output: 0
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 300
#    0 <= mat[i][j] <= 10^4
#    0 <= threshold <= 10^5

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Use prefix sum and binary search on answer.
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        def get_sum(r1, c1, r2, c2):
            """Get sum of submatrix [r1,c1] to [r2,c2] (0-indexed)"""
            return prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]

        def can_find_square(side):
            """Check if there exists a square of given side with sum <= threshold"""
            for i in range(m - side + 1):
                for j in range(n - side + 1):
                    if get_sum(i, j, i + side - 1, j + side - 1) <= threshold:
                        return True
            return False

        # Binary search on side length
        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if can_find_square(mid):
                left = mid
            else:
                right = mid - 1

        return left


class SolutionLinear:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Linear approach: only check next size if current size passes.
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        def get_sum(r1, c1, r2, c2):
            return prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]

        result = 0
        for i in range(m):
            for j in range(n):
                # Only try to extend if possible
                while result + 1 <= min(m - i, n - j):
                    if get_sum(i, j, i + result, j + result) <= threshold:
                        result += 1
                    else:
                        break

        return result
