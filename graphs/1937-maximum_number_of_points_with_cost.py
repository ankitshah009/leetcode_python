#1937. Maximum Number of Points with Cost
#Medium
#
#You are given an m x n integer matrix points (0-indexed). Starting with 0
#points, you want to maximize the number of points you can get from the matrix.
#
#To gain points, you must pick one cell in each row. Picking the cell at
#coordinates (r, c) will add points[r][c] to your score.
#
#However, you will lose points if you pick a cell too far from the cell that
#you picked in the previous row. For every two adjacent rows r and r + 1 (where
#0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will
#subtract abs(c1 - c2) from your score.
#
#Return the maximum number of points you can achieve.
#
#Example 1:
#Input: points = [[1,2,3],[1,5,1],[3,1,1]]
#Output: 9
#
#Example 2:
#Input: points = [[1,5],[2,3],[4,2]]
#Output: 11
#
#Constraints:
#    m == points.length
#    n == points[r].length
#    1 <= m, n <= 10^5
#    1 <= m * n <= 10^5
#    0 <= points[r][c] <= 10^5

from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        DP with optimization using prefix max from left and right.
        """
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for i in range(1, m):
            # Left max: max(dp[j] + j) for j <= c
            left = [0] * n
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])

            # Right max: max(dp[j] - j) for j >= c
            right = [0] * n
            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])

            # Update dp
            for c in range(n):
                dp[c] = points[i][c] + max(left[c], right[c])

        return max(dp)


class SolutionExplained:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Detailed explanation:

        Naive: dp[i][c] = points[i][c] + max(dp[i-1][j] - |c-j|) for all j
        This is O(m*n^2).

        Optimization:
        Split into two cases: j <= c and j > c

        For j <= c: max(dp[j] - (c - j)) = max(dp[j] + j) - c
        For j > c: max(dp[j] - (j - c)) = max(dp[j] - j) + c

        Use prefix/suffix max to compute these in O(n).
        """
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for i in range(1, m):
            new_dp = [0] * n

            # Compute left[c] = max(dp[j] + j) for j in [0, c]
            # Then contribution from left = left[c] - c
            running_max = float('-inf')
            for c in range(n):
                running_max = max(running_max, dp[c] + c)
                new_dp[c] = running_max - c

            # Compute right[c] = max(dp[j] - j) for j in [c, n-1]
            # Then contribution from right = right[c] + c
            running_max = float('-inf')
            for c in range(n - 1, -1, -1):
                running_max = max(running_max, dp[c] - c)
                new_dp[c] = max(new_dp[c], running_max + c)

            # Add current row points
            for c in range(n):
                new_dp[c] += points[i][c]

            dp = new_dp

        return max(dp)
