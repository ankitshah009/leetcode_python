#1887. Reduction Operations to Make the Array Elements Equal
#Medium
#
#Given an integer array nums, your goal is to make all elements in nums equal.
#To complete one operation, follow these steps:
#
#1. Find the largest value in nums. Let its index be i (0-indexed) and its
#   value be largest. If there are multiple elements with the largest value,
#   pick the smallest i.
#2. Find the next largest value in nums strictly smaller than largest. Let its
#   value be nextLargest.
#3. Reduce nums[i] to nextLargest.
#
#Return the number of operations to make all elements in nums equal.
#
#Example 1:
#Input: nums = [5,1,3]
#Output: 3
#
#Example 2:
#Input: nums = [1,1,1]
#Output: 0
#
#Example 3:
#Input: nums = [1,1,2,2,3]
#Output: 4
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    1 <= nums[i] <= 5 * 10^4

from typing import List
from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        Each unique value needs to be reduced through all values below it.
        Sort unique values and count operations.
        """
        freq = Counter(nums)
        unique_values = sorted(freq.keys(), reverse=True)

        operations = 0
        accumulated = 0

        # Process from largest to second-smallest
        for i in range(len(unique_values) - 1):
            val = unique_values[i]
            accumulated += freq[val]
            operations += accumulated

        return operations


class SolutionSort:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        Sort and count position differences.
        """
        nums.sort()
        n = len(nums)
        operations = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                # All elements from i to n-1 need to pass through this value
                operations += n - i

        return operations


class SolutionExplained:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        Same as sort approach with explanation.

        If we sort: [1, 1, 2, 2, 3]
        - Elements at indices 2,3 (value 2) need 1 operation each to become 1
        - Element at index 4 (value 3) needs 2 operations (3->2->1)

        Pattern: element at position i needs (number of distinct values before it)
        operations to reach the minimum.
        """
        nums.sort()
        result = 0
        distinct_count = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                distinct_count += 1
            result += distinct_count

        return result
