#868. Binary Gap
#Easy
#
#Given a positive integer n, find and return the longest distance between any
#two adjacent 1's in the binary representation of n. If there are no two adjacent
#1's, return 0.
#
#Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
#The distance between two 1's is the absolute difference between their bit positions.
#
#Example 1:
#Input: n = 22
#Output: 2
#Explanation: 22 in binary is "10110". The first pair of 1s has distance 2.
#The second pair has distance 1. The answer is max(2, 1) = 2.
#
#Example 2:
#Input: n = 8
#Output: 0
#Explanation: 8 in binary is "1000". No two 1s, so return 0.
#
#Example 3:
#Input: n = 5
#Output: 2
#Explanation: 5 in binary is "101".
#
#Constraints:
#    1 <= n <= 10^9

class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Track position of previous 1.
        """
        max_gap = 0
        prev = None

        for i in range(32):
            if n & (1 << i):
                if prev is not None:
                    max_gap = max(max_gap, i - prev)
                prev = i

        return max_gap


class SolutionString:
    """Using binary string"""

    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]  # Remove '0b' prefix

        # Find positions of 1s
        ones = [i for i, bit in enumerate(binary) if bit == '1']

        if len(ones) < 2:
            return 0

        return max(ones[i+1] - ones[i] for i in range(len(ones) - 1))


class SolutionDirect:
    """Direct bit manipulation"""

    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_one = -1
        pos = 0

        while n:
            if n & 1:
                if last_one != -1:
                    max_gap = max(max_gap, pos - last_one)
                last_one = pos
            n >>= 1
            pos += 1

        return max_gap


class SolutionCompact:
    """Compact solution"""

    def binaryGap(self, n: int) -> int:
        indices = [i for i, b in enumerate(bin(n)) if b == '1']
        return max([b - a for a, b in zip(indices, indices[1:])], default=0)
