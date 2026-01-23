#1018. Binary Prefix Divisible By 5
#Easy
#
#You are given a binary array nums (0-indexed).
#
#We define xi as the number whose binary representation is the subarray
#nums[0..i] (from most-significant-bit to least-significant-bit).
#
#Return an array of booleans answer where answer[i] is true if xi is divisible
#by 5.
#
#Example 1:
#Input: nums = [0,1,1]
#Output: [true,false,false]
#Explanation: x0 = 0, x1 = 1, x2 = 3
#
#Example 2:
#Input: nums = [1,1,1]
#Output: [false,false,false]
#
#Constraints:
#    1 <= nums.length <= 10^5
#    nums[i] is either 0 or 1.

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        Track running number mod 5.
        """
        result = []
        current = 0

        for bit in nums:
            current = (current * 2 + bit) % 5
            result.append(current == 0)

        return result


class SolutionExplicit:
    """More explicit calculation"""

    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        n = len(nums)
        result = [False] * n

        value = 0
        for i in range(n):
            value = value * 2 + nums[i]
            value %= 5  # Keep small to avoid overflow
            result[i] = (value == 0)

        return result


class SolutionCompact:
    """Compact one-liner style"""

    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        from itertools import accumulate

        # Not directly applicable, but showing iterative approach
        result = []
        val = 0
        for b in nums:
            val = (val << 1 | b) % 5
            result.append(val == 0)
        return result
