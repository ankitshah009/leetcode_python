#1829. Maximum XOR for Each Query
#Medium
#
#You are given a sorted array nums of n non-negative integers and an integer
#maximumBit. You want to perform the following query n times:
#
#1. Find a non-negative integer k < 2^maximumBit such that
#   nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized.
#   k is the answer to the ith query.
#2. Remove the last element from the current array nums.
#
#Return an array answer, where answer[i] is the answer to the ith query.
#
#Example 1:
#Input: nums = [0,1,1,3], maximumBit = 2
#Output: [0,3,2,3]
#
#Example 2:
#Input: nums = [2,3,4,7], maximumBit = 3
#Output: [5,2,6,5]
#
#Example 3:
#Input: nums = [0,1,2,2,5,7], maximumBit = 3
#Output: [4,3,6,4,6,7]
#
#Constraints:
#    nums.length == n
#    1 <= n <= 10^5
#    1 <= maximumBit <= 20
#    0 <= nums[i] < 2^maximumBit
#    nums is sorted in ascending order.

from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        To maximize XOR with k, flip all bits of current XOR.
        k = (2^maximumBit - 1) XOR current_xor
        """
        n = len(nums)
        mask = (1 << maximumBit) - 1  # All 1s for maximumBit bits

        # Compute cumulative XOR
        xor_val = 0
        for num in nums:
            xor_val ^= num

        result = []

        for i in range(n - 1, -1, -1):
            # Best k is complement of current XOR within mask
            k = mask ^ xor_val
            result.append(k)
            # Remove last element
            xor_val ^= nums[i]

        return result


class SolutionPrefix:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        Using prefix XOR array.
        """
        n = len(nums)
        mask = (1 << maximumBit) - 1

        # Build prefix XOR
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]

        # For query i, we use first (n-i) elements
        result = []
        for i in range(n):
            xor_val = prefix_xor[n - i]
            result.append(mask ^ xor_val)

        return result


class SolutionSimple:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        Direct approach computing XOR each time.
        """
        from functools import reduce
        from operator import xor

        mask = (1 << maximumBit) - 1
        total_xor = reduce(xor, nums)

        result = []
        for num in reversed(nums):
            result.append(mask ^ total_xor)
            total_xor ^= num

        return result
