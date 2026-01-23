#598. Range Addition II
#Easy
#
#You are given an m x n matrix M initialized with all 0's and an array of
#operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by
#one for all 0 <= x < ai and 0 <= y < bi.
#
#Count and return the number of maximum integers in the matrix after performing
#all the operations.
#
#Example 1:
#Input: m = 3, n = 3, ops = [[2,2],[3,3]]
#Output: 4
#Explanation: The maximum integer in M is 2, and there are four of it in M.
#
#Example 2:
#Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
#Output: 4
#
#Example 3:
#Input: m = 3, n = 3, ops = []
#Output: 9
#
#Constraints:
#    1 <= m, n <= 4 * 10^4
#    0 <= ops.length <= 10^4
#    ops[i].length == 2
#    1 <= ai <= m
#    1 <= bi <= n

from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        Maximum elements are in the intersection of all operations.
        Find minimum a and minimum b across all operations.
        """
        if not ops:
            return m * n

        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)

        return min_a * min_b


class SolutionExplicit:
    """Explicit loop"""

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n

        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)

        return min_row * min_col
