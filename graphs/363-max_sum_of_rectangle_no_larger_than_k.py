#363. Max Sum of Rectangle No Larger Than K
#Hard
#
#Given an m x n matrix matrix and an integer k, return the max sum of a
#rectangle in the matrix such that its sum is no larger than k.
#
#It is guaranteed that there will be a rectangle with a sum no larger than k.
#
#Example 1:
#Input: matrix = [[1,0,1],[0,-2,3]], k = 2
#Output: 2
#Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
#and 2 is the max number no larger than k (k = 2).
#
#Example 2:
#Input: matrix = [[2,2,-1]], k = 3
#Output: 3
#
#Constraints:
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 100
#    -100 <= matrix[i][j] <= 100
#    -10^5 <= k <= 10^5

from typing import List
from sortedcontainers import SortedList
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Reduce 2D problem to 1D using column prefix sums.
        For each pair of rows, find max subarray sum <= k.
        """
        m, n = len(matrix), len(matrix[0])
        result = float('-inf')

        # Iterate over all pairs of columns
        for left in range(n):
            # Running sum for each row
            row_sum = [0] * m

            for right in range(left, n):
                # Update row sums
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                # Find max subarray sum <= k in row_sum
                # Using sorted list and binary search
                prefix_sums = SortedList([0])
                current_sum = 0

                for s in row_sum:
                    current_sum += s
                    # Find smallest prefix_sum where current_sum - prefix_sum <= k
                    # i.e., prefix_sum >= current_sum - k
                    idx = prefix_sums.bisect_left(current_sum - k)

                    if idx < len(prefix_sums):
                        result = max(result, current_sum - prefix_sums[idx])

                    prefix_sums.add(current_sum)

        return result


class SolutionBruteForce:
    """O(m²n²) brute force with prefix sums"""

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Compute 2D prefix sums
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (matrix[i-1][j-1] +
                               prefix[i-1][j] +
                               prefix[i][j-1] -
                               prefix[i-1][j-1])

        result = float('-inf')

        # Try all rectangles
        for r1 in range(m):
            for r2 in range(r1, m):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        total = (prefix[r2+1][c2+1] -
                                prefix[r1][c2+1] -
                                prefix[r2+1][c1] +
                                prefix[r1][c1])
                        if total <= k:
                            result = max(result, total)

        return result


class SolutionOptimized:
    """Optimized for specific matrix dimensions"""

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Optimize by iterating over the smaller dimension
        if m > n:
            # Transpose
            matrix = list(map(list, zip(*matrix)))
            m, n = n, m

        result = float('-inf')

        for left in range(n):
            row_sum = [0] * m

            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                # Find max subarray <= k using Kadane's + binary search
                current_sum = 0
                max_sum = float('-inf')

                # Kadane's for quick check
                kadane_sum = 0
                for s in row_sum:
                    kadane_sum = max(s, kadane_sum + s)
                    max_sum = max(max_sum, kadane_sum)

                if max_sum <= k:
                    result = max(result, max_sum)
                else:
                    # Need to use sorted list
                    prefix_sums = SortedList([0])
                    current_sum = 0
                    for s in row_sum:
                        current_sum += s
                        idx = prefix_sums.bisect_left(current_sum - k)
                        if idx < len(prefix_sums):
                            result = max(result, current_sum - prefix_sums[idx])
                        prefix_sums.add(current_sum)

        return result
