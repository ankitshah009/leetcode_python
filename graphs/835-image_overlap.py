#835. Image Overlap
#Medium
#
#You are given two images, img1 and img2, represented as binary, square matrices
#of size n x n. A binary matrix has only 0s and 1s as values.
#
#We translate one image however we choose by sliding all the 1s left, right, up,
#and/or down any number of units. We then place it on top of the other image.
#We can then calculate the overlap by counting the number of positions that have
#a 1 in both images.
#
#Return the largest possible overlap.
#
#Example 1:
#Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
#Output: 3
#
#Example 2:
#Input: img1 = [[1]], img2 = [[1]]
#Output: 1
#
#Example 3:
#Input: img1 = [[0]], img2 = [[0]]
#Output: 0
#
#Constraints:
#    n == img1.length == img1[i].length
#    n == img2.length == img2[i].length
#    1 <= n <= 30
#    img1[i][j] is either 0 or 1.
#    img2[i][j] is either 0 or 1.

from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        """
        For each pair of 1s (one from each image), compute the translation
        vector. Count most common translation.
        """
        n = len(img1)

        # Get positions of 1s
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        if not ones1 or not ones2:
            return 0

        # Count translations
        translations = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                translations[(r2 - r1, c2 - c1)] += 1

        return max(translations.values())


class SolutionBruteForce:
    """Try all translations"""

    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        def count_overlap(dr, dc):
            """Count overlap when img1 is shifted by (dr, dc)"""
            count = 0
            for r in range(n):
                for c in range(n):
                    r2, c2 = r + dr, c + dc
                    if 0 <= r2 < n and 0 <= c2 < n:
                        if img1[r][c] == 1 and img2[r2][c2] == 1:
                            count += 1
            return count

        max_overlap = 0
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                max_overlap = max(max_overlap, count_overlap(dr, dc))

        return max_overlap


class SolutionConvolution:
    """Using convolution (conceptual)"""

    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        # Pad and convolve
        def convolve(A, B):
            # B is the kernel, slide over A
            max_val = 0
            for dr in range(-n + 1, n):
                for dc in range(-n + 1, n):
                    overlap = 0
                    for r in range(n):
                        for c in range(n):
                            r2, c2 = r - dr, c - dc
                            if 0 <= r2 < n and 0 <= c2 < n:
                                overlap += A[r][c] * B[r2][c2]
                    max_val = max(max_val, overlap)
            return max_val

        return convolve(img2, img1)
