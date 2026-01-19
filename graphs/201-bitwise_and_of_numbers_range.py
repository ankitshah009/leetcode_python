#201. Bitwise AND of Numbers Range
#Medium
#
#Given two integers left and right that represent the range [left, right],
#return the bitwise AND of all numbers in this range, inclusive.
#
#Example 1:
#Input: left = 5, right = 7
#Output: 4
#
#Example 2:
#Input: left = 0, right = 0
#Output: 0
#
#Example 3:
#Input: left = 1, right = 2147483647
#Output: 0
#
#Constraints:
#    0 <= left <= right <= 2^31 - 1

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Find the common prefix of left and right in binary.
        The bits after the common prefix will all be zeroed out due to
        numbers in between.
        """
        shift = 0

        # Find common prefix by shifting right until left == right
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Shift back to get the result
        return left << shift


class SolutionBrianKernighan:
    """Using Brian Kernighan's algorithm"""

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Turn off the rightmost 1-bit in right until right <= left.
        The remaining bits are the common prefix.
        """
        while right > left:
            right = right & (right - 1)

        return right


class SolutionBitByBit:
    """Check each bit position"""

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0

        for i in range(31, -1, -1):
            left_bit = (left >> i) & 1
            right_bit = (right >> i) & 1

            if left_bit == right_bit:
                result |= (left_bit << i)
            else:
                # Once bits differ, all subsequent bits will be 0
                break

        return result
