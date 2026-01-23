#1486. XOR Operation in an Array
#Easy
#
#You are given an integer n and an integer start.
#
#Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
#
#Return the bitwise XOR of all elements of nums.
#
#Example 1:
#Input: n = 5, start = 0
#Output: 8
#Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
#Where "^" corresponds to bitwise XOR operator.
#
#Example 2:
#Input: n = 4, start = 3
#Output: 8
#Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
#
#Constraints:
#    1 <= n <= 1000
#    0 <= start <= 1000

from functools import reduce

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Compute XOR of arithmetic sequence: start, start+2, start+4, ..., start+2*(n-1)
        """
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result


class SolutionReduce:
    def xorOperation(self, n: int, start: int) -> int:
        """Using reduce"""
        from operator import xor
        return reduce(xor, (start + 2 * i for i in range(n)))


class SolutionComprehension:
    def xorOperation(self, n: int, start: int) -> int:
        """Using comprehension"""
        result = 0
        for x in [start + 2 * i for i in range(n)]:
            result ^= x
        return result


class SolutionMath:
    def xorOperation(self, n: int, start: int) -> int:
        """
        Mathematical approach using XOR properties.

        nums[i] = start + 2*i = 2*(start//2 + i) + (start & 1)

        Let's transform: if start is even, we XOR 2k, 2k+2, ..., 2k+2(n-1)
        which equals 2 * (k XOR k+1 XOR ... XOR k+n-1)

        Use the property: XOR of [0..n-1] has a pattern every 4 numbers.
        """
        # Use helper function to compute XOR from 0 to x
        def xor_to_n(x: int) -> int:
            """Returns 0 XOR 1 XOR 2 XOR ... XOR x"""
            if x < 0:
                return 0
            mod = x % 4
            if mod == 0:
                return x
            elif mod == 1:
                return 1
            elif mod == 2:
                return x + 1
            else:
                return 0

        # Transform the problem
        # nums[i] = start + 2*i
        # Let last = start + 2*(n-1) = start + 2n - 2

        # XOR of start, start+2, ..., last
        # = 2 * (start//2 XOR start//2+1 XOR ... XOR last//2) if start is even
        # Need to handle odd/even cases

        last = start + 2 * (n - 1)

        # If start is odd, all elements are odd, so LSB of result is n % 2
        # Otherwise all elements are even, so LSB is 0

        # Divide everything by 2 and multiply result by 2, then fix LSB
        # XOR(start, start+2, ..., last) = 2 * XOR(start//2, ..., last//2) [approximately]

        # Simpler: just use the loop for this problem size
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result


class SolutionGenerator:
    def xorOperation(self, n: int, start: int) -> int:
        """Using generator expression with functools"""
        return reduce(lambda x, y: x ^ y, (start + 2 * i for i in range(n)))
