#1558. Minimum Numbers of Function Calls to Make Target Array
#Medium
#
#You are given an integer array nums. You have an integer array arr of the same
#length with all values set to 0 initially. You also have the following modify
#function:
#
#You want to use the modify function to convert arr to nums using the minimum
#number of calls.
#
#Return the minimum number of function calls to make nums from arr.
#
#The test cases are generated so that the answer fits in a 32-bit signed integer.
#
#modify(arr, op, idx):
#    if op == 0:
#        arr[idx] += 1
#    else:
#        for i in range(len(arr)):
#            arr[i] *= 2
#
#Example 1:
#Input: nums = [1,5]
#Output: 5
#Explanation: Starting from arr = [0,0]:
#call modify(arr, 0, 1): [0,1]
#call modify(arr, 1, _): [0,2]
#call modify(arr, 0, 1): [0,3]
#call modify(arr, 1, _): [0,6]
#call modify(arr, 0, 0): [1,6]
#The final array is [1,5]. Note that it is not valid to call modify(arr, 1, _)
#at first because that would set arr to [0,0] as 2 * 0 = 0.
#
#Example 2:
#Input: nums = [2,2]
#Output: 3
#Explanation: Starting from arr = [0,0]:
#call modify(arr, 0, 0): [1,0]
#call modify(arr, 0, 1): [1,1]
#call modify(arr, 1, _): [2,2]
#
#Example 3:
#Input: nums = [4,2,5]
#Output: 6
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^9

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Think backwards: convert nums to all zeros.
        - Divide all by 2 (shared operation)
        - Subtract 1 from individual elements

        For each number:
        - Count of 1 bits = number of add operations needed
        - Highest bit position = number of multiply operations needed

        Total = sum of add ops + max of multiply ops (shared)
        """
        add_ops = 0
        max_mult_ops = 0

        for num in nums:
            mult_ops = 0
            while num > 0:
                if num % 2 == 1:
                    add_ops += 1
                num //= 2
                if num > 0:
                    mult_ops += 1

            max_mult_ops = max(max_mult_ops, mult_ops)

        return add_ops + max_mult_ops


class SolutionBitCount:
    def minOperations(self, nums: List[int]) -> int:
        """
        Using bit operations.

        Add operations = total number of 1 bits across all numbers
        Multiply operations = maximum bit length - 1 (shared across all)
        """
        add_ops = sum(bin(num).count('1') for num in nums)

        # Find max bit length
        max_val = max(nums) if nums else 0
        mult_ops = max_val.bit_length() - 1 if max_val > 0 else 0

        return add_ops + mult_ops


class SolutionDetailed:
    def minOperations(self, nums: List[int]) -> int:
        """
        Detailed explanation.

        Forward thinking:
        - op=0: Add 1 to one element (individual)
        - op=1: Multiply all by 2 (shared)

        Backward thinking (convert nums to zeros):
        - Subtract 1 from odd numbers (to make even)
        - Divide all by 2 (shared)

        For number n:
        - Number of subtract ops = popcount(n) = number of 1 bits
        - Number of divide ops = floor(log2(n)) = bit_length - 1

        Since divide is shared, we take max across all numbers.
        """
        if not nums:
            return 0

        total_ones = 0
        max_bits = 0

        for num in nums:
            # Count 1 bits
            total_ones += bin(num).count('1')
            # Track max bit length
            max_bits = max(max_bits, num.bit_length())

        # Subtract 1 for divide ops (bit_length counts from 1)
        divide_ops = max_bits - 1 if max_bits > 0 else 0

        return total_ones + divide_ops


class SolutionSimulation:
    def minOperations(self, nums: List[int]) -> int:
        """
        Simulation approach (backward).
        """
        ops = 0
        nums = list(nums)

        while any(n > 0 for n in nums):
            # Make all odd numbers even
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ops += 1

            # If any number > 0, divide all by 2
            if any(n > 0 for n in nums):
                for i in range(len(nums)):
                    nums[i] //= 2
                ops += 1

        return ops


class SolutionMath:
    def minOperations(self, nums: List[int]) -> int:
        """
        Mathematical formula.
        """
        import math

        if not nums:
            return 0

        # Sum of popcount for all numbers
        add_count = sum(bin(x).count('1') for x in nums)

        # Max bit length (number of multiplications needed)
        max_num = max(nums)
        mult_count = int(math.log2(max_num)) if max_num > 0 else 0

        return add_count + mult_count
