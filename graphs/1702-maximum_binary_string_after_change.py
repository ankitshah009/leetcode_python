#1702. Maximum Binary String After Change
#Medium
#
#You are given a binary string binary consisting of only 0's or 1's. You can
#apply each of the following operations any number of times:
#
#- Operation 1: If the number contains the substring "00", you can replace it
#  with "10".
#- Operation 2: If the number contains the substring "10", you can replace it
#  with "01".
#
#Return the maximum binary string you can obtain after any number of operations.
#
#Example 1:
#Input: binary = "000110"
#Output: "111011"
#
#Example 2:
#Input: binary = "01"
#Output: "01"
#
#Constraints:
#    1 <= binary.length <= 10^5
#    binary consists only of '0' and '1'.

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        Key insight: All 0s can be moved together, then converted to 1s except one.
        Result has at most one 0, positioned at (first_zero_index + zero_count - 1).
        """
        n = len(binary)

        # Find first zero
        first_zero = binary.find('0')
        if first_zero == -1:
            return binary  # All 1s already

        # Count zeros from first_zero onwards
        zero_count = binary[first_zero:].count('0')

        # Result: all 1s except one 0 at position (first_zero + zero_count - 1)
        zero_pos = first_zero + zero_count - 1

        return '1' * zero_pos + '0' + '1' * (n - zero_pos - 1)


class SolutionExplained:
    def maximumBinaryString(self, binary: str) -> str:
        """
        Step by step explanation:
        1. Leading 1s cannot be changed (no 0 to their left)
        2. All 0s can be collected together using "10" -> "01"
        3. Consecutive 0s become "111...10" using "00" -> "10"
        4. Final result has exactly one 0
        """
        n = len(binary)
        ones_prefix = 0

        # Count leading ones
        while ones_prefix < n and binary[ones_prefix] == '1':
            ones_prefix += 1

        if ones_prefix == n:
            return binary

        # Count remaining zeros
        zeros = binary[ones_prefix:].count('0')

        # Position of single zero in result
        zero_position = ones_prefix + zeros - 1

        # Build result
        result = ['1'] * n
        result[zero_position] = '0'

        return ''.join(result)
