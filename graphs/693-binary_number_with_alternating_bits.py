#693. Binary Number with Alternating Bits
#Easy
#
#Given a positive integer, check whether it has alternating bits: namely, if
#two adjacent bits will always have different values.
#
#Example 1:
#Input: n = 5
#Output: true
#Explanation: The binary representation of 5 is: 101
#
#Example 2:
#Input: n = 7
#Output: false
#Explanation: The binary representation of 7 is: 111.
#
#Example 3:
#Input: n = 11
#Output: false
#Explanation: The binary representation of 11 is: 1011.
#
#Constraints:
#    1 <= n <= 2^31 - 1

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        XOR with shifted version: if alternating, result is all 1s.
        Then check if result + 1 is power of 2.
        """
        # n ^ (n >> 1) should be all 1s if alternating
        xor = n ^ (n >> 1)
        # Check if xor is all 1s: xor & (xor + 1) == 0
        return (xor & (xor + 1)) == 0


class SolutionIterative:
    """Check each adjacent pair of bits"""

    def hasAlternatingBits(self, n: int) -> bool:
        prev_bit = n & 1
        n >>= 1

        while n:
            curr_bit = n & 1
            if curr_bit == prev_bit:
                return False
            prev_bit = curr_bit
            n >>= 1

        return True


class SolutionString:
    """Convert to binary string and check"""

    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]  # Remove '0b' prefix
        return '00' not in binary and '11' not in binary


class SolutionDivision:
    """Using division operations"""

    def hasAlternatingBits(self, n: int) -> bool:
        prev = n % 2
        n //= 2

        while n > 0:
            curr = n % 2
            if curr == prev:
                return False
            prev = curr
            n //= 2

        return True
