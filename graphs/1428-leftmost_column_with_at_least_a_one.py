#1428. Leftmost Column with at Least a One
#Medium
#
#A row-sorted binary matrix means that all elements are 0 or 1 and each row of
#the matrix is sorted in non-decreasing order.
#
#Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of
#the leftmost column with a 1 in it. If such an index does not exist, return -1.
#
#You can't access the Binary Matrix directly. You may only access the matrix
#using a BinaryMatrix interface:
#    BinaryMatrix.get(row, col) returns the element of the matrix at index
#    (row, col) (0-indexed).
#    BinaryMatrix.dimensions() returns the dimensions of the matrix as a list
#    of 2 elements [rows, cols], which means the matrix is rows x cols.
#
#Submissions making more than 1000 calls to BinaryMatrix.get will be judged
#Wrong Answer. Also, any solutions that attempt to circumvent the judge will
#result in disqualification.
#
#For custom testing purposes, the input will be the entire binary matrix mat.
#You will not have access to the binary matrix directly.
#
#Example 1:
#Input: mat = [[0,0],[1,1]]
#Output: 0
#
#Example 2:
#Input: mat = [[0,0],[0,1]]
#Output: 1
#
#Example 3:
#Input: mat = [[0,0],[0,0]]
#Output: -1
#
#Constraints:
#    rows == mat.length
#    cols == mat[i].length
#    1 <= rows, cols <= 100
#    mat[i][j] is either 0 or 1.
#    mat[i] is sorted in non-decreasing order.

class BinaryMatrix:
    """Interface definition"""
    def get(self, row: int, col: int) -> int:
        pass

    def dimensions(self) -> list:
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Start from top-right corner.
        If 1, move left (potential answer, look for earlier 1).
        If 0, move down (no 1 in this column for current row).
        O(rows + cols) time.
        """
        rows, cols = binaryMatrix.dimensions()

        # Start from top-right
        r, c = 0, cols - 1
        result = -1

        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                result = c  # Found a 1, record column
                c -= 1      # Move left to find earlier 1
            else:
                r += 1      # Move down

        return result


class SolutionBinarySearch:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Binary search on each row to find first 1.
        O(rows * log(cols)) time.
        """
        rows, cols = binaryMatrix.dimensions()
        result = cols  # Start with invalid column

        for r in range(rows):
            # Binary search for first 1 in this row
            left, right = 0, cols - 1
            while left <= right:
                mid = (left + right) // 2
                if binaryMatrix.get(r, mid) == 1:
                    right = mid - 1
                else:
                    left = mid + 1

            # left is the first 1 in this row (or cols if no 1)
            if left < cols and binaryMatrix.get(r, left) == 1:
                result = min(result, left)

        return result if result < cols else -1


class SolutionBinarySearchOptimized:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Binary search with early termination.
        Only search up to current best.
        """
        rows, cols = binaryMatrix.dimensions()
        result = -1

        for r in range(rows):
            # Binary search in range [0, result-1] or [0, cols-1]
            left = 0
            right = (result - 1) if result != -1 else (cols - 1)

            while left <= right:
                mid = (left + right) // 2
                if binaryMatrix.get(r, mid) == 1:
                    result = mid  # Update result
                    right = mid - 1
                else:
                    left = mid + 1

        return result
