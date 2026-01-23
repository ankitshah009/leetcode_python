#1863. Sum of All Subset XOR Totals
#Easy
#
#The XOR total of an array is defined as the bitwise XOR of all its elements,
#or 0 if the array is empty.
#
#Given an array nums, return the sum of all XOR totals for every subset of nums.
#
#Note: Subsets with the same elements should be counted multiple times.
#
#Example 1:
#Input: nums = [1,3]
#Output: 6
#Explanation: Subsets: [], [1], [3], [1,3]
#XOR totals: 0, 1, 3, 2
#Sum = 0 + 1 + 3 + 2 = 6
#
#Example 2:
#Input: nums = [5,1,6]
#Output: 28
#
#Example 3:
#Input: nums = [3,4,5,6,7,8]
#Output: 480
#
#Constraints:
#    1 <= nums.length <= 12
#    1 <= nums[i] <= 20

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Math insight: each bit contributes to exactly 2^(n-1) subsets.
        """
        n = len(nums)
        # OR of all numbers gives bits that appear in at least one number
        # Each such bit contributes 2^(n-1) times
        or_all = 0
        for num in nums:
            or_all |= num

        return or_all * (1 << (n - 1))


class SolutionRecursive:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Recursive subset enumeration.
        """
        def helper(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor

            # Include or exclude nums[index]
            return (helper(index + 1, current_xor ^ nums[index]) +
                    helper(index + 1, current_xor))

        return helper(0, 0)


class SolutionIterative:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Iterate through all subsets using bitmask.
        """
        n = len(nums)
        total = 0

        for mask in range(1 << n):
            xor_val = 0
            for i in range(n):
                if mask & (1 << i):
                    xor_val ^= nums[i]
            total += xor_val

        return total


class SolutionDP:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        DP approach tracking XOR values.
        """
        xor_sums = {0: 1}  # XOR value -> count of subsets

        for num in nums:
            new_sums = {}
            for xor_val, count in xor_sums.items():
                # Not including num
                new_sums[xor_val] = new_sums.get(xor_val, 0) + count
                # Including num
                new_xor = xor_val ^ num
                new_sums[new_xor] = new_sums.get(new_xor, 0) + count
            xor_sums = new_sums

        return sum(xor_val * count for xor_val, count in xor_sums.items())
