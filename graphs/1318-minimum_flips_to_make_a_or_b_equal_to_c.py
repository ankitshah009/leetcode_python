#1318. Minimum Flips to Make a OR b Equal to c
#Medium
#
#Given 3 positive numbers a, b and c. Return the minimum flips required in some
#bits of a and b to make (a OR b == c). (Bitwise OR operation).
#
#Flip operation consists of changing any single bit 1 to 0 or changing the bit
#0 to 1 in their binary representation.
#
#Example 1:
#Input: a = 2, b = 6, c = 5
#Output: 3
#Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
#
#Example 2:
#Input: a = 4, b = 2, c = 7
#Output: 1
#
#Example 3:
#Input: a = 1, b = 2, c = 3
#Output: 0
#
#Constraints:
#    1 <= a <= 10^9
#    1 <= b <= 10^9
#    1 <= c <= 10^9

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Check each bit position:
        - If c bit is 1: at least one of a,b must be 1
        - If c bit is 0: both a,b must be 0
        """
        flips = 0

        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 1:
                # Need at least one 1 in a or b
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                # Need both to be 0
                flips += bit_a + bit_b

            a >>= 1
            b >>= 1
            c >>= 1

        return flips


class SolutionBitManip:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Using bit manipulation:
        - (a | b) ^ c gives positions where OR doesn't match c
        - For bits where c=0 but (a|b)=1, we might need 2 flips if both a and b are 1
        """
        # XOR shows where the bits differ
        diff = (a | b) ^ c

        # Count bits in diff: these positions need changes
        # But if c bit is 0 and both a,b bits are 1, we need 2 flips
        flips = 0

        while diff > 0 or a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            bit_or = (a | b) & 1

            if bit_or != bit_c:
                if bit_c == 0 and bit_a == 1 and bit_b == 1:
                    flips += 2
                else:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1
            diff >>= 1

        return flips


class SolutionSimple:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """Bit counting approach"""
        # Where OR doesn't match c
        or_diff = (a | b) ^ c

        # Where both a and b are 1 but c is 0 (need extra flip)
        extra = a & b & or_diff

        return bin(or_diff).count('1') + bin(extra).count('1')
