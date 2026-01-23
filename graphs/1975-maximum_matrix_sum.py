#1975. Maximum Matrix Sum
#Medium
#
#You are given an n x n integer matrix. You can do the following operation any
#number of times:
#- Choose any two adjacent elements of matrix and multiply each of them by -1.
#
#Two elements are considered adjacent if and only if they share a border.
#
#Your goal is to maximize the sum of the matrix's elements. Return the maximum
#sum of the matrix's elements using the operation mentioned above.
#
#Example 1:
#Input: matrix = [[1,-1],[-1,1]]
#Output: 4
#Explanation: We can multiply both -1s by -1 to get all 1s. Sum = 4.
#
#Example 2:
#Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
#Output: 16
#
#Constraints:
#    n == matrix.length == matrix[i].length
#    2 <= n <= 250
#    -10^5 <= matrix[i][j] <= 10^5

from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Key insight: We can move negatives around but parity of negative count
        stays the same. If even negatives, make all positive. If odd, leave
        smallest absolute value as negative.
        """
        total = 0
        min_abs = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    negative_count += 1

        # If odd number of negatives, one value must be negative
        if negative_count % 2 == 1:
            total -= 2 * min_abs

        return total


class SolutionExplained:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        Detailed explanation:

        The operation flips signs of two adjacent elements.
        - Flipping twice returns to original
        - We can "move" a negative sign to any position via chain of flips
        - Two negatives can cancel each other out

        So:
        - Even number of negatives: can make all positive
        - Odd number of negatives: exactly one must remain negative
          - Best choice: the element with smallest absolute value

        Answer: sum of absolute values - (2 * min_abs if odd negatives)
        """
        abs_sum = 0
        min_abs = float('inf')
        neg_count = 0

        n = len(matrix)

        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                abs_val = abs(val)

                abs_sum += abs_val
                min_abs = min(min_abs, abs_val)

                if val < 0:
                    neg_count += 1

        if neg_count % 2 == 0:
            return abs_sum
        else:
            # Must keep one negative - choose smallest absolute value
            return abs_sum - 2 * min_abs
