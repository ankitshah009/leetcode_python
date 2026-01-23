#1605. Find Valid Matrix Given Row and Column Sums
#Medium
#
#You are given two arrays rowSum and colSum of non-negative integers where
#rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum
#of the elements of the jth column of a 2D matrix. In other words, you do not
#know the elements of the matrix, but you do know the sums of each row and column.
#
#Find any matrix of non-negative integers of size rowSum.length x colSum.length
#that satisfies the rowSum and colSum requirements.
#
#Return a 2D array representing any matrix that fulfills the requirements. It's
#guaranteed that at least one matrix that fulfills the requirements exists.
#
#Example 1:
#Input: rowSum = [3,8], colSum = [4,7]
#Output: [[3,0],[1,7]]
#Explanation: Row 0: 3 + 0 = 3
#Row 1: 1 + 7 = 8
#Column 0: 3 + 1 = 4
#Column 1: 0 + 7 = 7
#
#Example 2:
#Input: rowSum = [5,7,10], colSum = [8,6,8]
#Output: [[0,5,0],[6,1,0],[2,0,8]]
#
#Constraints:
#    1 <= rowSum.length, colSum.length <= 500
#    0 <= rowSum[i], colSum[i] <= 10^8
#    sum(rowSum) == sum(colSum)

from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        Greedy approach: For each cell (i,j), assign min(rowSum[i], colSum[j])
        and update the remaining sums.
        """
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Assign as much as possible
                val = min(rowSum[i], colSum[j])
                matrix[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val

        return matrix


class SolutionTwoPointers:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        Two pointers approach: Move through rows and columns.
        """
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        i, j = 0, 0

        while i < m and j < n:
            val = min(rowSum[i], colSum[j])
            matrix[i][j] = val
            rowSum[i] -= val
            colSum[j] -= val

            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return matrix


class SolutionDetailed:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        Detailed greedy solution with explanation.

        Key insight: If we greedily fill each cell with the minimum of
        remaining row and column sum, we will always get a valid solution.

        Proof: At each step, we're reducing either the row sum to 0 or
        the column sum to 0 (or both). This ensures we make progress.
        """
        m, n = len(rowSum), len(colSum)

        # Make copies to avoid modifying input
        row_remaining = rowSum[:]
        col_remaining = colSum[:]

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Place the minimum of remaining row and column sums
                value = min(row_remaining[i], col_remaining[j])
                result[i][j] = value

                # Update remaining sums
                row_remaining[i] -= value
                col_remaining[j] -= value

                # Early exit if row is satisfied
                if row_remaining[i] == 0:
                    break

        return result


class SolutionOnePass:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        One-pass diagonal-style filling.
        """
        m, n = len(rowSum), len(colSum)
        result = [[0] * n for _ in range(m)]

        r, c = 0, 0
        while r < m and c < n:
            value = min(rowSum[r], colSum[c])
            result[r][c] = value
            rowSum[r] -= value
            colSum[c] -= value

            # Move to next row or column
            if rowSum[r] == 0:
                r += 1
            else:
                c += 1

        return result
