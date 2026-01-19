#371. Sum of Two Integers
#Medium
#
#Given two integers a and b, return the sum of the two integers without using
#the operators + and -.
#
#Example 1:
#Input: a = 1, b = 2
#Output: 3
#
#Example 2:
#Input: a = 2, b = 3
#Output: 5
#
#Constraints:
#    -1000 <= a, b <= 1000

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Bit manipulation approach.
        XOR gives sum without carry.
        AND gives carry positions, shift left for next iteration.

        In Python, we need to handle negative numbers with masking.
        """
        # 32-bit mask
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # Sum without carry
            sum_without_carry = (a ^ b) & MASK
            # Carry
            carry = ((a & b) << 1) & MASK

            a = sum_without_carry
            b = carry

        # Handle negative numbers
        return a if a <= MAX_INT else ~(a ^ MASK)


class SolutionRecursive:
    """Recursive version"""

    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        if b == 0:
            return a if a <= MAX_INT else ~(a ^ MASK)

        return self.getSum((a ^ b) & MASK, ((a & b) << 1) & MASK)


class SolutionSimple:
    """Simple Python approach (for reference)"""

    def getSum(self, a: int, b: int) -> int:
        # Using bit_length to calculate without +/-
        # This is more of a workaround than true bit manipulation
        return sum([a, b])
