#1289. Minimum Falling Path Sum II
#Hard
#
#Given an n x n integer matrix grid, return the minimum sum of a falling path
#with non-zero shifts.
#
#A falling path with non-zero shifts is a choice of exactly one element from
#each row of grid such that no two elements chosen in adjacent rows are in the
#same column.
#
#Example 1:
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
#Output: 13
#Explanation:
#The possible falling paths are:
#[1,5,9], [1,5,7], [1,6,7], [1,6,8],
#[2,4,8], [2,4,9], [2,6,7], [2,6,8],
#[3,4,8], [3,4,9], [3,5,7], [3,5,9]
#The falling path with the smallest sum is [1,5,7], so the answer is 13.
#
#Example 2:
#Input: grid = [[7]]
#Output: 7
#
#Constraints:
#    n == grid.length == grid[i].length
#    1 <= n <= 200
#    -99 <= grid[i][j] <= 99

from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        Track minimum and second minimum for each row.
        O(n^2) time, O(1) extra space.
        """
        n = len(grid)
        if n == 1:
            return grid[0][0]

        # First row initialization
        prev_min1 = prev_min2 = float('inf')
        prev_min1_col = -1

        for j in range(n):
            if grid[0][j] < prev_min1:
                prev_min2 = prev_min1
                prev_min1 = grid[0][j]
                prev_min1_col = j
            elif grid[0][j] < prev_min2:
                prev_min2 = grid[0][j]

        # Process remaining rows
        for i in range(1, n):
            curr_min1 = curr_min2 = float('inf')
            curr_min1_col = -1

            for j in range(n):
                # Add minimum from previous row (different column)
                if j != prev_min1_col:
                    val = grid[i][j] + prev_min1
                else:
                    val = grid[i][j] + prev_min2

                # Update current row minimums
                if val < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = val
                    curr_min1_col = j
                elif val < curr_min2:
                    curr_min2 = val

            prev_min1, prev_min2, prev_min1_col = curr_min1, curr_min2, curr_min1_col

        return prev_min1


class SolutionDP:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """Standard DP with O(n^2) space"""
        n = len(grid)
        dp = [row[:] for row in grid]

        for i in range(1, n):
            for j in range(n):
                # Find minimum from previous row excluding column j
                dp[i][j] += min(dp[i - 1][k] for k in range(n) if k != j)

        return min(dp[n - 1])
