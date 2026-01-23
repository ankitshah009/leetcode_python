#1337. The K Weakest Rows in a Matrix
#Easy
#
#You are given an m x n binary matrix mat of 1's (representing soldiers) and
#0's (representing civilians). The soldiers are positioned in front of the
#civilians. That is, all the 1's will appear to the left of all the 0's in
#each row.
#
#A row i is weaker than a row j if one of the following is true:
#    The number of soldiers in row i is less than the number of soldiers in row j.
#    Both rows have the same number of soldiers and i < j.
#
#Return the indices of the k weakest rows in the matrix ordered from weakest
#to strongest.
#
#Example 1:
#Input: mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3
#Output: [2,0,3]
#Explanation:
#The number of soldiers in each row is:
#- Row 0: 2
#- Row 1: 4
#- Row 2: 1
#- Row 3: 2
#- Row 4: 5
#The rows ordered from weakest to strongest are [2,0,3,1,4].
#
#Example 2:
#Input: mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], k = 2
#Output: [0,2]
#
#Constraints:
#    m == mat.length
#    n == mat[i].length
#    2 <= n, m <= 100
#    1 <= k <= m
#    matrix[i][j] is either 0 or 1.

from typing import List
import heapq
import bisect

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Count soldiers in each row, sort by (count, index).
        """
        # Count soldiers and pair with row index
        strength = [(sum(row), i) for i, row in enumerate(mat)]

        # Sort by (soldier_count, row_index)
        strength.sort()

        return [idx for _, idx in strength[:k]]


class SolutionBinarySearch:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Use binary search to count soldiers (since 1s are before 0s)"""
        def count_soldiers(row):
            # Binary search for first 0
            left, right = 0, len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left

        strength = [(count_soldiers(row), i) for i, row in enumerate(mat)]
        strength.sort()

        return [idx for _, idx in strength[:k]]


class SolutionHeap:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Use max heap to keep k smallest"""
        # Max heap (negate values for max heap behavior)
        heap = []

        for i, row in enumerate(mat):
            soldiers = sum(row)

            if len(heap) < k:
                heapq.heappush(heap, (-soldiers, -i))
            elif (-soldiers, -i) > heap[0]:
                heapq.heapreplace(heap, (-soldiers, -i))

        # Extract and sort
        result = [(-idx, -soldiers) for soldiers, idx in heap]
        result.sort(key=lambda x: (x[1], x[0]))

        return [idx for idx, _ in result]
