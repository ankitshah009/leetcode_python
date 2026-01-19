#338. Counting Bits
#Easy
#
#Given an integer n, return an array ans of length n + 1 such that for each i
#(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
#
#Example 1:
#Input: n = 2
#Output: [0,1,1]
#Explanation:
#0 --> 0
#1 --> 1
#2 --> 10
#
#Example 2:
#Input: n = 5
#Output: [0,1,1,2,1,2]
#Explanation:
#0 --> 0
#1 --> 1
#2 --> 10
#3 --> 11
#4 --> 100
#5 --> 101
#
#Constraints:
#    0 <= n <= 10^5
#
#Follow up:
#- It is very easy to come up with a solution with a runtime of O(n log n). Can
#  you do it in linear time O(n) and possibly in a single pass?
#- Can you do it without using any built-in function (i.e., like
#  __builtin_popcount in C++)?

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        DP with last set bit relationship.
        dp[i] = dp[i >> 1] + (i & 1)
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


class SolutionLastBit:
    """DP with last set bit removal"""

    def countBits(self, n: int) -> List[int]:
        # dp[i] = dp[i & (i-1)] + 1
        # i & (i-1) removes the last set bit
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp


class SolutionOffset:
    """DP with power of 2 offset"""

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = dp[i - offset] + 1

        return dp


class SolutionBuiltin:
    """Using built-in function"""

    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]


class SolutionBitCount:
    """Manual bit counting"""

    def countBits(self, n: int) -> List[int]:
        def popcount(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1
            return count

        return [popcount(i) for i in range(n + 1)]
