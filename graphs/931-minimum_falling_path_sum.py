#931. Minimum Falling Path Sum
#Medium
#
#Given an n x n array of integers matrix, return the minimum sum of any falling
#path through matrix.
#
#A falling path starts at any element in the first row and chooses the element
#in the next row that is either directly below or diagonally left/right. The
#next element must be in the column range [c-1, c+1].
#
#Example 1:
#Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
#Output: 13
#Explanation: Paths: 1->5->7=13, 1->4->8=13, 1->4->9=14
#
#Example 2:
#Input: matrix = [[-19,57],[-40,-5]]
#Output: -59
#
#Constraints:
#    n == matrix.length == matrix[i].length
#    1 <= n <= 100
#    -100 <= matrix[i][j] <= 100

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        """
        DP: dp[i][j] = min path sum ending at (i, j)
        """
        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                # Previous row: can come from j-1, j, or j+1
                above = matrix[i - 1][j]
                above_left = matrix[i - 1][j - 1] if j > 0 else float('inf')
                above_right = matrix[i - 1][j + 1] if j < n - 1 else float('inf')

                matrix[i][j] += min(above, above_left, above_right)

        return min(matrix[-1])


class SolutionExtraSpace:
    """Using extra space"""

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [row[:] for row in matrix]

        for i in range(1, n):
            for j in range(n):
                candidates = [dp[i - 1][j]]
                if j > 0:
                    candidates.append(dp[i - 1][j - 1])
                if j < n - 1:
                    candidates.append(dp[i - 1][j + 1])
                dp[i][j] = matrix[i][j] + min(candidates)

        return min(dp[-1])


class SolutionMemo:
    """Top-down memoization"""

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        from functools import lru_cache

        n = len(matrix)

        @lru_cache(maxsize=None)
        def dp(row: int, col: int) -> int:
            if col < 0 or col >= n:
                return float('inf')
            if row == 0:
                return matrix[0][col]

            return matrix[row][col] + min(
                dp(row - 1, col - 1),
                dp(row - 1, col),
                dp(row - 1, col + 1)
            )

        return min(dp(n - 1, j) for j in range(n))
