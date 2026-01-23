#832. Flipping an Image
#Easy
#
#Given an n x n binary matrix image, flip the image horizontally, then invert
#it, and return the resulting image.
#
#To flip an image horizontally means that each row of the image is reversed.
#To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#
#Example 1:
#Input: image = [[1,1,0],[1,0,1],[0,0,0]]
#Output: [[1,0,0],[0,1,0],[1,1,1]]
#Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#Then, invert: [[1,0,0],[0,1,0],[1,1,1]].
#
#Example 2:
#Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
#Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#Constraints:
#    n == image.length
#    n == image[i].length
#    1 <= n <= 20
#    images[i][j] is either 0 or 1.

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        """
        Reverse and invert in one pass using two pointers.
        """
        n = len(image)

        for row in image:
            left, right = 0, n - 1
            while left <= right:
                # Swap and invert
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1

        return image


class SolutionOneLiner:
    """One-liner using list comprehension"""

    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[1 - x for x in row[::-1]] for row in image]


class SolutionXOR:
    """Using XOR for inversion"""

    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] ^= 1
        return image


class SolutionOptimized:
    """Optimized: only process when values differ"""

    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)

        for row in image:
            for i in range((n + 1) // 2):
                j = n - 1 - i
                # If values are same, both flip to opposite
                # If values differ, they swap then flip back to original
                if row[i] == row[j]:
                    row[i] = row[j] = 1 - row[i]
                # else: values differ, no change after flip+invert

        return image
