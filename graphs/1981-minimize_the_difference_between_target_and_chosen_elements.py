#1981. Minimize the Difference Between Target and Chosen Elements
#Medium
#
#You are given an m x n integer matrix mat and an integer target.
#
#Choose one integer from each row in the matrix such that the absolute
#difference between target and the sum of the chosen elements is minimized.
#
#Return the minimum absolute difference.
#
#Example 1:
#Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
#Output: 0
#Explanation: One possible choice is: 1 from row 1, 5 from row 2, 7 from row 3.
#Sum = 1 + 5 + 7 = 13, difference = |13 - 13| = 0.
#
#Example 2:
#Input: mat = [[1],[2],[3]], target = 100
#Output: 94
#
#Example 3:
#Input: mat = [[1,2,9,8,7]], target = 6
#Output: 1
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 70
#    1 <= mat[i][j] <= 70
#    1 <= target <= 800

from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        DP with set of reachable sums.
        """
        possible = {0}

        for row in mat:
            new_possible = set()
            for prev_sum in possible:
                for val in row:
                    new_possible.add(prev_sum + val)
            possible = new_possible

        return min(abs(s - target) for s in possible)


class SolutionOptimized:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        Optimized: prune sums that are too large.
        Only keep sums up to target + min possible remainder.
        """
        m, n = len(mat), len(mat[0])

        # Compute minimum sum we can add from remaining rows
        min_remaining = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            min_remaining[i] = min_remaining[i + 1] + min(mat[i])

        possible = {0}

        for i, row in enumerate(mat):
            new_possible = set()
            row_min = min(row)

            for prev_sum in possible:
                for val in row:
                    new_sum = prev_sum + val
                    # Prune if already exceeds target by more than necessary
                    if new_sum <= target or new_sum == prev_sum + row_min:
                        new_possible.add(new_sum)

            possible = new_possible

        return min(abs(s - target) for s in possible)


class SolutionBitmask:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        Use bitmask to track possible sums (faster for dense sets).
        """
        m, n = len(mat), len(mat[0])
        max_sum = m * 70  # Maximum possible sum

        # Bit i is 1 if sum i is achievable
        possible = 1  # Initially sum 0 is achievable

        for row in mat:
            new_possible = 0
            for val in row:
                new_possible |= possible << val
            possible = new_possible

        # Find minimum difference
        min_diff = float('inf')

        for s in range(max_sum + 1):
            if possible & (1 << s):
                min_diff = min(min_diff, abs(s - target))

        return min_diff
