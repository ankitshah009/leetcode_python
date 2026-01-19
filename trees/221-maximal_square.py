#221. Maximal Square
#Medium
#
#Given an m x n binary matrix filled with 0's and 1's, find the largest square
#containing only 1's and return its area.
#
#Example 1:
#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4
#
#Example 2:
#Input: matrix = [["0","1"],["1","0"]]
#Output: 1
#
#Example 3:
#Input: matrix = [["0"]]
#Output: 0
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 300
#    matrix[i][j] is '0' or '1'.

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        DP: dp[i][j] = side length of largest square ending at (i,j)
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 if matrix[i][j] == '1'
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


class SolutionOptimized:
    """Space optimized - O(n) space"""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)
        max_side = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
                    max_side = max(max_side, curr[j])
            prev = curr

        return max_side * max_side


class SolutionSingleRow:
    """Even more optimized - single row with prev variable"""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        max_side = 0
        prev = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return max_side * max_side
