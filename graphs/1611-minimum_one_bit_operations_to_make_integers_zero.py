#1611. Minimum One Bit Operations to Make Integers Zero
#Hard
#
#Given an integer n, you must transform it into 0 using the following operations
#any number of times:
#- Change the rightmost (0th) bit in the binary representation of n.
#- Change the ith bit in the binary representation of n if the (i-1)th bit is
#  set to 1 and the (i-2)th through 0th bits are set to 0.
#
#Return the minimum number of operations to transform n into 0.
#
#Example 1:
#Input: n = 3
#Output: 2
#Explanation: The binary representation of 3 is "11".
#"11" -> "01" with the 2nd operation since the 0th bit is 1.
#"01" -> "00" with the 1st operation.
#
#Example 2:
#Input: n = 6
#Output: 4
#Explanation: The binary representation of 6 is "110".
#"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th is 0.
#"010" -> "011" with the 1st operation.
#"011" -> "001" with the 2nd operation since the 0th bit is 1.
#"001" -> "000" with the 1st operation.
#
#Constraints:
#    0 <= n <= 10^9

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        This is related to Gray code. The operations are exactly Gray code increment.

        Key insight: The minimum operations to go from n to 0 equals the
        inverse Gray code of n (i.e., position of n in Gray code sequence).

        To convert Gray code back to binary: result ^= result >> 1 (repeated)
        """
        result = n
        while n > 0:
            n >>= 1
            result ^= n
        return result


class SolutionRecursive:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Recursive approach.

        f(n) = number of operations to reduce n to 0
        f(0) = 0
        f(2^k) = 2^(k+1) - 1  (takes this many ops to reduce 1 followed by k zeros to 0)

        For general n with highest bit at position k:
        f(n) = f(2^k) - f(n - 2^k)
             = 2^(k+1) - 1 - f(n XOR 2^k)
        """
        if n == 0:
            return 0

        # Find highest bit position
        k = n.bit_length() - 1

        # f(2^k) = 2^(k+1) - 1
        return (1 << (k + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << k))


class SolutionIterative:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Iterative version using Gray code conversion.
        """
        # Gray code to binary conversion
        ans = 0
        while n:
            ans ^= n
            n >>= 1
        return ans


class SolutionMath:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Mathematical approach with alternating signs.

        If n has bits at positions b1 > b2 > b3 > ..., then:
        f(n) = (2^(b1+1) - 1) - (2^(b2+1) - 1) + (2^(b3+1) - 1) - ...
        """
        result = 0
        sign = 1

        while n > 0:
            # Find position of highest bit
            k = n.bit_length() - 1

            # Add or subtract (2^(k+1) - 1)
            result += sign * ((1 << (k + 1)) - 1)

            # Remove highest bit
            n ^= (1 << k)

            # Alternate sign
            sign = -sign

        return result
