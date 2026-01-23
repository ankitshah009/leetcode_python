#1966. Binary Searchable Numbers in an Unsorted Array
#Medium
#
#Consider a function that implements an algorithm similar to Binary Search. The
#function has two input parameters: sequence is a sequence of integers, and
#target is an integer value. The purpose of the function is to find if the
#target exists in the sequence.
#
#The pseudocode of the function is as follows:
#func(sequence, target)
#  while sequence is not empty
#    randomly choose an element from sequence as pivot
#    if pivot = target, return true
#    else if pivot < target, remove pivot and all elements to its left
#    else, remove pivot and all elements to its right
#  end while
#  return false
#
#When the sequence is sorted, the function works correctly for all values.
#When the sequence is not sorted, the function does not work for all values,
#but may still work for some values.
#
#Given an integer array nums, representing the sequence, that contains unique
#numbers and may or may not be sorted, return the number of values that are
#guaranteed to be found using the function, for every possible pivot selection.
#
#Example 1:
#Input: nums = [7]
#Output: 1
#
#Example 2:
#Input: nums = [2,1]
#Output: 1
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^5 <= nums[i] <= 10^5
#    All the values of nums are unique.

from typing import List

class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        """
        A number is binary searchable if:
        - All numbers to its left are smaller
        - All numbers to its right are larger
        """
        n = len(nums)
        if n == 0:
            return 0

        # prefix_max[i] = max of nums[0..i-1]
        prefix_max = [float('-inf')] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i - 1])

        # suffix_min[i] = min of nums[i+1..n-1]
        suffix_min = [float('inf')] * n
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i + 1])

        # Count numbers that are greater than all left and smaller than all right
        count = 0
        for i in range(n):
            if nums[i] > prefix_max[i] and nums[i] < suffix_min[i]:
                count += 1

        return count


class SolutionOnePass:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        """
        Single pass approach using stack-like logic.
        """
        n = len(nums)
        if n == 0:
            return 0

        # Compute suffix minimums
        suffix_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        count = 0
        prefix_max = float('-inf')

        for i in range(n):
            if nums[i] > prefix_max and nums[i] <= suffix_min[i]:
                count += 1
            prefix_max = max(prefix_max, nums[i])

        return count


class SolutionStack:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        """
        Use monotonic stack to track candidates.
        """
        n = len(nums)
        stack = []  # Stores indices of potential candidates
        max_so_far = float('-inf')

        for i in range(n):
            # Remove candidates that are >= current (can't be searched)
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            # Add current if > all previous
            if nums[i] > max_so_far:
                stack.append(i)

            max_so_far = max(max_so_far, nums[i])

        return len(stack)
