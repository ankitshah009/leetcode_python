#363. Max Sum of Rectangle No Larger Than K
#Hard
#
#Given an m x n matrix matrix and an integer k, return the max sum of a rectangle
#in the matrix such that its sum is no larger than k.
#
#It is guaranteed that there will be a rectangle with a sum no larger than k.
#
#Example 1:
#Input: matrix = [[1,0,1],[0,-2,3]], k = 2
#Output: 2
#Explanation: The sum of rectangle [[0,1],[-2,3]] is 2, which is the max value
#no larger than k.
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
#
#Follow up: What if the number of rows is much larger than the number of columns?

from sortedcontainers import SortedList
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = float('-inf')

        # Fix left and right columns
        for left in range(n):
            # row_sum[i] = sum of matrix[i][left:right+1]
            row_sum = [0] * m

            for right in range(left, n):
                # Update row sums
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                # Find max subarray sum <= k using prefix sum + sorted set
                # prefix_sum[j] - prefix_sum[i] <= k
                # prefix_sum[i] >= prefix_sum[j] - k

                prefix_sums = SortedList([0])
                curr_sum = 0

                for s in row_sum:
                    curr_sum += s

                    # Find smallest prefix_sum >= curr_sum - k
                    idx = prefix_sums.bisect_left(curr_sum - k)
                    if idx < len(prefix_sums):
                        result = max(result, curr_sum - prefix_sums[idx])

                    prefix_sums.add(curr_sum)

        return result

    # Kadane's algorithm for finding max subarray (not constrained by k)
    def maxSumSubmatrixKadane(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Make sure we iterate over the smaller dimension
        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m

        result = float('-inf')

        for left in range(n):
            row_sum = [0] * m

            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                # Find max sum <= k
                prefix_sums = SortedList([0])
                curr_sum = 0

                for s in row_sum:
                    curr_sum += s
                    idx = prefix_sums.bisect_left(curr_sum - k)
                    if idx < len(prefix_sums):
                        result = max(result, curr_sum - prefix_sums[idx])
                    prefix_sums.add(curr_sum)

                if result == k:
                    return k

        return result
