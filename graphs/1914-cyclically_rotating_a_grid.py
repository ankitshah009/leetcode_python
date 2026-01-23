#1914. Cyclically Rotating a Grid
#Medium
#
#You are given an m x n integer matrix grid, where m and n are both even
#integers, and an integer k.
#
#The matrix is composed of several layers. A layer is shown in a different
#color in the image.
#
#Each layer is rotated counter-clockwise k times. For example, a 1x1 layer has
#no rotation, and a 2x2 layer has one rotation counter-clockwise.
#
#Return the rotated matrix.
#
#Example 1:
#Input: grid = [[40,10],[30,20]], k = 1
#Output: [[10,20],[40,30]]
#
#Example 2:
#Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
#Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
#
#Constraints:
#    m == grid.length
#    n == grid[i].length
#    2 <= m, n <= 50
#    Both m and n are even integers.
#    1 <= grid[i][j] <= 5000
#    1 <= k <= 10^9

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Extract each layer, rotate, put back.
        """
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        def extract_layer(layer: int) -> List[int]:
            """Extract layer as a list (counter-clockwise order)."""
            elements = []
            r1, c1 = layer, layer
            r2, c2 = m - 1 - layer, n - 1 - layer

            # Top row (left to right)
            for c in range(c1, c2 + 1):
                elements.append(grid[r1][c])
            # Right column (top+1 to bottom)
            for r in range(r1 + 1, r2 + 1):
                elements.append(grid[r][c2])
            # Bottom row (right-1 to left)
            for c in range(c2 - 1, c1 - 1, -1):
                elements.append(grid[r2][c])
            # Left column (bottom-1 to top+1)
            for r in range(r2 - 1, r1, -1):
                elements.append(grid[r][c1])

            return elements

        def put_layer(layer: int, elements: List[int]) -> None:
            """Put elements back into layer."""
            r1, c1 = layer, layer
            r2, c2 = m - 1 - layer, n - 1 - layer
            idx = 0

            # Top row
            for c in range(c1, c2 + 1):
                grid[r1][c] = elements[idx]
                idx += 1
            # Right column
            for r in range(r1 + 1, r2 + 1):
                grid[r][c2] = elements[idx]
                idx += 1
            # Bottom row
            for c in range(c2 - 1, c1 - 1, -1):
                grid[r2][c] = elements[idx]
                idx += 1
            # Left column
            for r in range(r2 - 1, r1, -1):
                grid[r][c1] = elements[idx]
                idx += 1

        for layer in range(layers):
            elements = extract_layer(layer)
            # Rotate counter-clockwise by k (which is same as shifting left by k)
            rot = k % len(elements)
            rotated = elements[rot:] + elements[:rot]
            put_layer(layer, rotated)

        return grid
