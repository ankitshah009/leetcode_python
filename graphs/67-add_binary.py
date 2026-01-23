#67. Add Binary
#Easy
#
#Given two binary strings a and b, return their sum as a binary string.
#
#Example 1:
#Input: a = "11", b = "1"
#Output: "100"
#
#Example 2:
#Input: a = "1010", b = "1011"
#Output: "10101"
#
#Constraints:
#    1 <= a.length, b.length <= 10^4
#    a and b consist only of '0' or '1' characters.
#    Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Simulate binary addition with carry.
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))


class SolutionBuiltin:
    def addBinary(self, a: str, b: str) -> str:
        """
        Using Python's int conversion (not for interview).
        """
        return bin(int(a, 2) + int(b, 2))[2:]


class SolutionBitwise:
    def addBinary(self, a: str, b: str) -> str:
        """
        Bitwise operations on integers.
        """
        x, y = int(a, 2), int(b, 2)

        while y:
            # XOR gives sum without carry
            # AND gives carry positions
            x, y = x ^ y, (x & y) << 1

        return bin(x)[2:]


class SolutionPadding:
    def addBinary(self, a: str, b: str) -> str:
        """
        Pad to equal length first.
        """
        # Pad with zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = []
        carry = 0

        for i in range(max_len - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        return ''.join(reversed(result))
