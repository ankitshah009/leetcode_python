#1738. Find Kth Largest XOR Coordinate Value
#Medium
#
#You are given a 2D matrix of size m x n, consisting of non-negative integers.
#You are also given an integer k.
#
#The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j]
#where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
#
#Find the kth largest value (1-indexed) of all the coordinates of matrix.
#
#Example 1:
#Input: matrix = [[5,2],[1,6]], k = 1
#Output: 7
#
#Example 2:
#Input: matrix = [[5,2],[1,6]], k = 2
#Output: 5
#
#Example 3:
#Input: matrix = [[5,2],[1,6]], k = 3
#Output: 4
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 1000
#    0 <= matrix[i][j] <= 10^6
#    1 <= k <= m * n

from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """
        Compute prefix XOR matrix and use min heap to track k largest.
        """
        m, n = len(matrix), len(matrix[0])

        # Prefix XOR matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        # Min heap to keep k largest values
        heap = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # XOR formula similar to 2D prefix sum
                prefix[i][j] = (prefix[i - 1][j] ^
                               prefix[i][j - 1] ^
                               prefix[i - 1][j - 1] ^
                               matrix[i - 1][j - 1])

                if len(heap) < k:
                    heapq.heappush(heap, prefix[i][j])
                elif prefix[i][j] > heap[0]:
                    heapq.heapreplace(heap, prefix[i][j])

        return heap[0]


class SolutionSort:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """
        Compute all values and sort.
        """
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        values = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (prefix[i - 1][j] ^
                               prefix[i][j - 1] ^
                               prefix[i - 1][j - 1] ^
                               matrix[i - 1][j - 1])
                values.append(prefix[i][j])

        values.sort(reverse=True)
        return values[k - 1]


class SolutionQuickSelect:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """
        Using quickselect (nthlargest).
        """
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        values = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (prefix[i - 1][j] ^
                               prefix[i][j - 1] ^
                               prefix[i - 1][j - 1] ^
                               matrix[i - 1][j - 1])
                values.append(prefix[i][j])

        return heapq.nlargest(k, values)[-1]
