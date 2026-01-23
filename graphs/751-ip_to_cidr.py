#751. IP to CIDR
#Medium
#
#An IP address is a formatted 32-bit unsigned integer where each group of 8
#bits is printed as a decimal number and the dot character '.' splits the
#groups.
#
#For example, the binary number 00001111 10001000 11111111 01101011 (spaced for
#clarity) formatted as an IP address would be "15.136.255.107".
#
#A CIDR block is a format used to denote a specific set of IP addresses. It is
#a string consisting of a base IP address, followed by a slash, followed by a
#prefix length k. The addresses it covers are all the IPs whose first k bits
#are the same as the base IP address.
#
#For example, "123.45.67.89/20" is a CIDR block with a prefix length of 20.
#Any IP address whose binary representation matches 01111011 00101101 0100xxxx
#xxxxxxxx, where x can be either 0 or 1, is in the set covered by the CIDR block.
#
#You are given a start IP address ip and the number of IP addresses we need to
#cover n. Your goal is to use as few CIDR blocks as possible to cover all the
#IP addresses in the inclusive range [ip, ip + n - 1] exactly.
#
#Return the shortest list of CIDR blocks that covers the range of IP addresses.
#
#Example 1:
#Input: ip = "255.0.0.7", n = 10
#Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
#
#Constraints:
#    7 <= ip.length <= 15
#    ip is a valid IPv4 on the form "a.b.c.d" where a, b, c, and d are integers
#    in the range [0, 255].
#    1 <= n <= 1000
#    Every implied address ip + x (for x < n) will be a valid IPv4 address.

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        """
        Convert to number, greedily pick largest valid CIDR blocks.
        """
        def ip_to_int(ip):
            parts = list(map(int, ip.split('.')))
            return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]

        def int_to_ip(num):
            return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"

        result = []
        start = ip_to_int(ip)

        while n > 0:
            # Find lowest set bit (max block size based on alignment)
            low_bit = start & (-start)
            if low_bit == 0:
                low_bit = 1 << 32

            # Don't exceed remaining n
            while low_bit > n:
                low_bit //= 2

            # Calculate prefix length
            # low_bit IPs = 2^(32-prefix)
            prefix = 32
            temp = low_bit
            while temp > 1:
                prefix -= 1
                temp //= 2

            result.append(f"{int_to_ip(start)}/{prefix}")
            start += low_bit
            n -= low_bit

        return result


class SolutionBitCount:
    """Using bit counting"""

    def ipToCIDR(self, ip: str, n: int) -> list[str]:
        def ip_to_int(ip):
            result = 0
            for part in ip.split('.'):
                result = result * 256 + int(part)
            return result

        def int_to_ip(num):
            return '.'.join(str((num >> (8 * i)) & 255) for i in range(3, -1, -1))

        result = []
        start = ip_to_int(ip)

        while n > 0:
            # Trailing zeros determine max block size from alignment
            trailing_zeros = (start & -start).bit_length() - 1 if start else 32

            # Block size = 2^trailing_zeros, but limited by n
            block_size = 1 << trailing_zeros
            while block_size > n:
                block_size //= 2
                trailing_zeros -= 1

            prefix = 32 - trailing_zeros
            result.append(f"{int_to_ip(start)}/{prefix}")

            start += block_size
            n -= block_size

        return result
