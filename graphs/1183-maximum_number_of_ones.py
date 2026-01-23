#1183. Maximum Number of Ones
#Hard
#
#Consider a matrix M with dimensions width * height, such that every cell has
#value 0 or 1, and any square sub-matrix of M of size sideLength * sideLength
#has at most maxOnes ones.
#
#Return the maximum possible number of ones that the matrix M can have.
#
#Example 1:
#Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
#Output: 4
#Explanation:
#In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
#The best solution is:
#[1,0,1]
#[0,0,0]
#[1,0,1]
#
#Example 2:
#Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
#Output: 6
#Explanation:
#[1,0,1]
#[1,0,1]
#[1,0,1]
#
#Constraints:
#    1 <= width, height <= 100
#    1 <= sideLength <= width, height
#    0 <= maxOnes <= sideLength * sideLength

import heapq

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """
        Key insight: Positions (i, j) and (i + sideLength, j) are in different
        square sub-matrices, so they can both be 1.

        Group positions by (i % sideLength, j % sideLength).
        Each group can have at most maxOnes positions be 1 across all squares.

        Actually, within each sideLength x sideLength tile, placing a 1 at
        position (r, c) means all positions (r, c), (r + s, c), (r, c + s), etc.
        will be 1.

        Count how many times each position in the tile pattern appears in
        the full matrix, then greedily pick top maxOnes positions.
        """
        # For each position (r, c) in the sideLength x sideLength tile,
        # count how many times it appears in the full matrix
        counts = []

        for r in range(sideLength):
            for c in range(sideLength):
                # How many times does position (r, c) repeat?
                # Rows: (height - r - 1) // sideLength + 1
                # Cols: (width - c - 1) // sideLength + 1
                row_count = (height - r - 1) // sideLength + 1
                col_count = (width - c - 1) // sideLength + 1
                counts.append(row_count * col_count)

        # Pick top maxOnes positions
        counts.sort(reverse=True)
        return sum(counts[:maxOnes])


class SolutionHeap:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """Using heap for top k selection"""
        # Min heap of size maxOnes for top k
        heap = []

        for r in range(sideLength):
            for c in range(sideLength):
                row_count = (height - r - 1) // sideLength + 1
                col_count = (width - c - 1) // sideLength + 1
                count = row_count * col_count

                if len(heap) < maxOnes:
                    heapq.heappush(heap, count)
                elif count > heap[0]:
                    heapq.heapreplace(heap, count)

        return sum(heap)


class SolutionDirect:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """Direct calculation"""
        s = sideLength

        # Full tiles in each dimension
        full_h = height // s
        full_w = width // s

        # Remaining rows and cols
        rem_h = height % s
        rem_w = width % s

        # Count appearances of each position in tile
        counts = []

        for r in range(s):
            for c in range(s):
                # Base count from full tiles
                count = full_h * full_w

                # Add from partial row at bottom
                if r < rem_h:
                    count += full_w

                # Add from partial column at right
                if c < rem_w:
                    count += full_h

                # Add corner if in both partial regions
                if r < rem_h and c < rem_w:
                    count += 1

                counts.append(count)

        counts.sort(reverse=True)
        return sum(counts[:maxOnes])
