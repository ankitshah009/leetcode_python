#1253. Reconstruct a 2-Row Binary Matrix
#Medium
#
#Given the following details of a matrix with n columns and 2 rows:
#    The matrix is a binary matrix, which means each element in the matrix can
#    be 0 or 1.
#    The sum of elements of the 0-th(upper) row is given as upper.
#    The sum of elements of the 1-st(lower) row is given as lower.
#    The sum of elements in the i-th column(0-indexed) is colsum[i], which is
#    either 0, 1, or 2.
#
#Your task is to reconstruct the matrix with upper, lower and colsum.
#
#Return it as a 2-D integer array. If there are more than one valid solution,
#any of them will be accepted.
#
#If no valid solution exists, return an empty 2-D array.
#
#Example 1:
#Input: upper = 2, lower = 1, colsum = [1,1,1]
#Output: [[1,1,0],[0,0,1]]
#Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
#
#Example 2:
#Input: upper = 2, lower = 3, colsum = [2,2,1,1]
#Output: []
#
#Example 3:
#Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
#Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
#
#Constraints:
#    1 <= colsum.length <= 10^5
#    0 <= upper, lower <= colsum.length
#    0 <= colsum[i] <= 2

from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """
        Greedy construction:
        1. Handle columns with sum 2 first (both rows must be 1)
        2. Handle columns with sum 1 (place in row with remaining capacity)
        3. Check if valid
        """
        n = len(colsum)
        row0 = [0] * n
        row1 = [0] * n

        # First pass: handle colsum == 2
        for i in range(n):
            if colsum[i] == 2:
                row0[i] = 1
                row1[i] = 1
                upper -= 1
                lower -= 1

        # Check if still valid
        if upper < 0 or lower < 0:
            return []

        # Second pass: handle colsum == 1
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    row0[i] = 1
                    upper -= 1
                elif lower > 0:
                    row1[i] = 1
                    lower -= 1
                else:
                    return []  # Can't place this 1

        # Check if we used exactly the right amount
        if upper != 0 or lower != 0:
            return []

        return [row0, row1]


class SolutionAlt:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        """Alternative approach"""
        n = len(colsum)

        # Quick validation
        if sum(colsum) != upper + lower:
            return []

        twos = sum(1 for x in colsum if x == 2)
        if twos > upper or twos > lower:
            return []

        row0 = []
        row1 = []

        remaining_upper = upper - twos
        remaining_lower = lower - twos

        for i in range(n):
            if colsum[i] == 2:
                row0.append(1)
                row1.append(1)
            elif colsum[i] == 1:
                if remaining_upper > 0:
                    row0.append(1)
                    row1.append(0)
                    remaining_upper -= 1
                else:
                    row0.append(0)
                    row1.append(1)
                    remaining_lower -= 1
            else:
                row0.append(0)
                row1.append(0)

        return [row0, row1]
