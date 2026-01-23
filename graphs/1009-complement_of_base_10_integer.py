#1009. Complement of Base 10 Integer
#Easy
#
#The complement of an integer is the integer you get when you flip all the 0's
#to 1's and all the 1's to 0's in its binary representation.
#
#Given an integer n, return its complement.
#
#Example 1:
#Input: n = 5
#Output: 2
#Explanation: 5 is "101" in binary, its complement is "010" which is 2.
#
#Example 2:
#Input: n = 7
#Output: 0
#Explanation: 7 is "111" in binary, its complement is "000" which is 0.
#
#Example 3:
#Input: n = 10
#Output: 5
#Explanation: 10 is "1010" in binary, its complement is "0101" which is 5.
#
#Constraints:
#    0 <= n < 10^9

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """
        XOR with all 1s of same length.
        """
        if n == 0:
            return 1

        # Find number of bits
        bits = n.bit_length()

        # Create mask of all 1s
        mask = (1 << bits) - 1

        return n ^ mask


class SolutionBitByBit:
    """Build complement bit by bit"""

    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        result = 0
        power = 1

        while n > 0:
            bit = n & 1
            result += (1 - bit) * power
            power *= 2
            n >>= 1

        return result


class SolutionString:
    """String manipulation"""

    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        binary = bin(n)[2:]  # Remove '0b' prefix
        complement = ''.join('1' if b == '0' else '0' for b in binary)
        return int(complement, 2)
