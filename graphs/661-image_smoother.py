#661. Image Smoother
#Easy
#
#An image smoother is a filter of the size 3 x 3 that can be applied to each
#cell of an image by rounding down the average of the cell and the eight
#surrounding cells (i.e., the average of the nine cells in the blue smoother).
#If one or more of the surrounding cells of a cell is not present, we do not
#consider it in the average (i.e., the average of the four cells in the red smoother).
#
#Given an m x n integer matrix img representing the grayscale of an image,
#return the image after applying the smoother on each cell of it.
#
#Example 1:
#Input: img = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[0,0,0],[0,0,0],[0,0,0]]
#
#Example 2:
#Input: img = [[100,200,100],[200,50,200],[100,200,100]]
#Output: [[137,141,137],[141,138,141],[137,141,137]]
#
#Constraints:
#    m == img.length
#    n == img[i].length
#    1 <= m, n <= 200
#    0 <= img[i][j] <= 255

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        Simple iteration over each cell and its neighbors.
        """
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = count = 0

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1

                result[i][j] = total // count

        return result


class SolutionPrefixSum:
    """Using 2D prefix sum for O(1) per query"""

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        # Build prefix sum with padding
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (img[i][j] + prefix[i][j + 1] +
                                        prefix[i + 1][j] - prefix[i][j])

        def get_sum(r1, c1, r2, c2):
            """Get sum of rectangle from (r1,c1) to (r2,c2) inclusive"""
            r1, c1 = max(0, r1), max(0, c1)
            r2, c2 = min(m - 1, r2), min(n - 1, c2)
            return (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] -
                    prefix[r2 + 1][c1] + prefix[r1][c1])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - 1), max(0, j - 1)
                r2, c2 = min(m - 1, i + 1), min(n - 1, j + 1)

                total = get_sum(i - 1, j - 1, i + 1, j + 1)
                count = (r2 - r1 + 1) * (c2 - c1 + 1)

                result[i][j] = total // count

        return result


class SolutionInPlace:
    """In-place modification using bit manipulation"""

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        for i in range(m):
            for j in range(n):
                total = count = 0

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            # Original value is in lower 8 bits
                            total += img[ni][nj] & 0xFF
                            count += 1

                # Store smoothed value in upper bits
                img[i][j] |= (total // count) << 8

        # Extract smoothed values
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8

        return img
