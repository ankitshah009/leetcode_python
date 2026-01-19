#461. Hamming Distance
#Easy
#
#The Hamming distance between two integers is the number of positions at which
#the corresponding bits are different.
#
#Given two integers x and y, return the Hamming distance between them.
#
#Example 1:
#Input: x = 1, y = 4
#Output: 2
#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#       ↑   ↑
#The above arrows point to positions where the corresponding bits are different.
#
#Example 2:
#Input: x = 3, y = 1
#Output: 1
#
#Constraints:
#    0 <= x, y <= 2^31 - 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """XOR and count bits"""
        return bin(x ^ y).count('1')


class SolutionBitManip:
    """Manual bit counting"""

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0

        while xor:
            count += xor & 1
            xor >>= 1

        return count


class SolutionBrianKernighan:
    """Brian Kernighan's algorithm - O(number of 1s)"""

    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0

        while xor:
            xor &= xor - 1  # Remove lowest set bit
            count += 1

        return count


class SolutionPopcount:
    """Using bit_count() (Python 3.10+)"""

    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
