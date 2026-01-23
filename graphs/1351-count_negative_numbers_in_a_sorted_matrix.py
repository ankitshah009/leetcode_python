#1351. Count Negative Numbers in a Sorted Matrix
#Easy
#
#Given a m x n matrix grid which is sorted in non-increasing order both row-wise
#and column-wise, return the number of negative numbers in grid.
#
#Example 1:
#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.
#
#Example 2:
#Input: grid = [[3,2],[1,0]]
#Output: 0
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 100
#    -100 <= grid[i][j] <= 100

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Start from bottom-left corner.
        Move right if negative, up if non-negative.
        O(m + n) time.
        """
        m, n = len(grid), len(grid[0])
        count = 0
        row, col = m - 1, 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # All elements to the right are also negative
                count += n - col
                row -= 1
            else:
                col += 1

        return count


class SolutionBinarySearch:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """Binary search for first negative in each row"""
        import bisect

        count = 0
        for row in grid:
            # bisect_left for 0 finds first element < 0 in reversed sense
            # Since row is sorted descending, find first negative
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1
            count += len(row) - left

        return count


class SolutionBruteForce:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """O(m*n) brute force"""
        return sum(1 for row in grid for val in row if val < 0)


class SolutionNumpyStyle:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """Pythonic one-liner"""
        return sum(val < 0 for row in grid for val in row)
