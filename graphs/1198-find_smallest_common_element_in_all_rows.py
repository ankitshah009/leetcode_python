#1198. Find Smallest Common Element in All Rows
#Medium
#
#Given an m x n matrix mat where every row is sorted in strictly increasing
#order, return the smallest common element in all rows.
#
#If there is no common element, return -1.
#
#Example 1:
#Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
#Output: 5
#
#Example 2:
#Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
#Output: 2
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    1 <= m, n <= 500
#    1 <= mat[i][j] <= 10^4
#    mat[i] is sorted in strictly increasing order.

from typing import List
from collections import Counter

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Count occurrences across all rows.
        First element that appears in all m rows is the answer.
        """
        m = len(mat)
        count = Counter()

        for row in mat:
            for num in row:
                count[num] += 1

        # Find smallest element appearing in all rows
        for num in sorted(count.keys()):
            if count[num] == m:
                return num

        return -1


class SolutionBinarySearch:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Binary search for each element in first row across other rows.
        """
        import bisect

        m, n = len(mat), len(mat[0])

        for num in mat[0]:
            found = True
            for i in range(1, m):
                # Binary search for num in row i
                idx = bisect.bisect_left(mat[i], num)
                if idx >= n or mat[i][idx] != num:
                    found = False
                    break

            if found:
                return num

        return -1


class SolutionPointers:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Use pointers for each row, advance smallest pointer.
        When all pointers point to same value, that's the answer.
        """
        m, n = len(mat), len(mat[0])
        pointers = [0] * m

        while True:
            # Check if all pointers point to same value
            current_values = [mat[i][pointers[i]] for i in range(m)]
            max_val = max(current_values)

            if all(v == max_val for v in current_values):
                return max_val

            # Advance pointers that are less than max_val
            for i in range(m):
                while pointers[i] < n and mat[i][pointers[i]] < max_val:
                    pointers[i] += 1

                if pointers[i] >= n:
                    return -1

        return -1
