#1680. Concatenation of Consecutive Binary Numbers
#Medium
#
#Given an integer n, return the decimal value of the binary string formed by
#concatenating the binary representations of 1 to n in order, modulo 10^9 + 7.
#
#Example 1:
#Input: n = 1
#Output: 1
#Explanation: "1" in binary corresponds to the decimal value 1.
#
#Example 2:
#Input: n = 3
#Output: 27
#Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", "11".
#After concatenating: "11011" = 27.
#
#Example 3:
#Input: n = 12
#Output: 505379714
#Explanation: The concatenation results in "1101110010111011110001001101010111100".
#The decimal value of that is 118505380540 modulo 10^9 + 7 = 505379714.
#
#Constraints:
#    1 <= n <= 10^5

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Build result by shifting and adding.
        For each number, shift result left by its bit length and add.
        """
        MOD = 10**9 + 7
        result = 0

        for i in range(1, n + 1):
            # Get number of bits in i
            bits = i.bit_length()
            # Shift result left and add i
            result = ((result << bits) | i) % MOD

        return result


class SolutionBitTracking:
    def concatenatedBinary(self, n: int) -> int:
        """
        Track bit length as we go (power of 2 detection).
        """
        MOD = 10**9 + 7
        result = 0
        length = 0

        for i in range(1, n + 1):
            # Check if i is a power of 2 (bit length increases)
            if i & (i - 1) == 0:
                length += 1

            result = ((result << length) + i) % MOD

        return result


class SolutionString:
    def concatenatedBinary(self, n: int) -> int:
        """
        String-based approach (may be slower for large n).
        """
        MOD = 10**9 + 7

        # Build binary string
        binary_str = ''.join(bin(i)[2:] for i in range(1, n + 1))

        # Convert to decimal with modulo
        result = 0
        for bit in binary_str:
            result = (result * 2 + int(bit)) % MOD

        return result


class SolutionMath:
    def concatenatedBinary(self, n: int) -> int:
        """
        Mathematical formulation using bit operations.
        """
        MOD = 10**9 + 7
        result = 0
        shift = 0

        for i in range(1, n + 1):
            # Update shift when we cross power of 2
            if i & (i - 1) == 0:
                shift += 1

            result = ((result << shift) | i) % MOD

        return result


class SolutionOptimized:
    def concatenatedBinary(self, n: int) -> int:
        """
        Optimized version with precomputed powers.
        """
        MOD = 10**9 + 7
        result = 0
        bit_len = 1

        for i in range(1, n + 1):
            # Check if we need more bits
            if i == 1 << bit_len:
                bit_len += 1

            result = ((result << bit_len) + i) % MOD

        return result
