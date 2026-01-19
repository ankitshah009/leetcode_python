#378. Kth Smallest Element in a Sorted Matrix
#Medium
#
#Given an n x n matrix where each of the rows and columns is sorted in
#ascending order, return the kth smallest element in the matrix.
#
#Note that it is the kth smallest element in the sorted order, not the kth
#distinct element.
#
#You must find a solution with a memory complexity better than O(n^2).
#
#Example 1:
#Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
#Output: 13
#Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
#the 8th smallest number is 13
#
#Example 2:
#Input: matrix = [[-5]], k = 1
#Output: -5
#
#Constraints:
#    n == matrix.length == matrix[i].length
#    1 <= n <= 300
#    -10^9 <= matrix[i][j] <= 10^9
#    All the rows and columns of matrix are guaranteed to be sorted in
#    non-decreasing order.
#    1 <= k <= n^2

from typing import List
import heapq
import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Binary search on value.
        For each mid value, count how many elements are <= mid.
        """
        n = len(matrix)

        def count_less_equal(target):
            """Count elements <= target using staircase search"""
            count = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1  # All elements in this column up to row
                    col += 1
                else:
                    row -= 1

            return count

        left, right = matrix[0][0], matrix[n-1][n-1]

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionHeap:
    """Min heap approach - O(k log n)"""

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # Heap: (value, row, col)
        heap = [(matrix[i][0], i, 0) for i in range(min(n, k))]
        heapq.heapify(heap)

        result = 0
        for _ in range(k):
            result, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return result


class SolutionMergeK:
    """Merge K sorted lists approach"""

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # Merge k sorted lists
        heap = []
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k - 1):
            val, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

        return heap[0][0]
