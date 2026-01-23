#1039. Minimum Score Triangulation of Polygon
#Medium
#
#You have a convex n-sided polygon where each vertex has an integer value.
#You are given an integer array values where values[i] is the value of the
#ith vertex (i.e., clockwise order).
#
#You will triangulate the polygon into n - 2 triangles. For each triangle,
#the value of that triangle is the product of the values of its vertices,
#and the total score of the triangulation is the sum of these values over
#all n - 2 triangles in the triangulation.
#
#Return the smallest possible total score that you can achieve with some
#triangulation of the polygon.
#
#Example 1:
#Input: values = [1,2,3]
#Output: 6
#Explanation: The polygon is already triangulated, and the score of the
#only triangle is 6.
#
#Example 2:
#Input: values = [3,7,4,5]
#Output: 144
#Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245,
#or 3*4*5 + 3*4*7 = 144. The minimum score is 144.
#
#Example 3:
#Input: values = [1,3,1,4,1,5]
#Output: 13
#Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
#
#Constraints:
#    n == values.length
#    3 <= n <= 50
#    1 <= values[i] <= 100

from typing import List
from functools import lru_cache

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        DP: For edge (i, j), choose vertex k between them.
        Triangle (i, k, j) + triangulate (i, k) + triangulate (k, j)
        """
        n = len(values)

        @lru_cache(maxsize=None)
        def dp(i, j):
            # Base case: adjacent vertices, no triangle possible
            if j - i < 2:
                return 0

            result = float('inf')
            for k in range(i + 1, j):
                score = values[i] * values[k] * values[j]
                score += dp(i, k) + dp(k, j)
                result = min(result, score)

            return result

        return dp(0, n - 1)


class SolutionIterative:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """Bottom-up DP"""
        n = len(values)
        INF = float('inf')
        dp = [[0] * n for _ in range(n)]

        # dp[i][j] = min score to triangulate polygon from i to j
        # Iterate by length of subarray
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = INF
                for k in range(i + 1, j):
                    score = values[i] * values[k] * values[j]
                    score += dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], score)

        return dp[0][n - 1]


class SolutionMemo:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """Explicit memoization"""
        n = len(values)
        memo = {}

        def solve(i, j):
            if j - i < 2:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            result = float('inf')
            for k in range(i + 1, j):
                score = values[i] * values[k] * values[j]
                score += solve(i, k) + solve(k, j)
                result = min(result, score)

            memo[(i, j)] = result
            return result

        return solve(0, n - 1)
