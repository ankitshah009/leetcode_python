#1752. Check if Array Is Sorted and Rotated
#Easy
#
#Given an array nums, return true if the array was originally sorted in
#non-decreasing order, then rotated some number of positions (including zero).
#Otherwise, return false.
#
#There may be duplicates in the original array.
#
#Note: An array A rotated by x positions results in an array B of the same
#length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
#
#Example 1:
#Input: nums = [3,4,5,1,2]
#Output: true
#
#Example 2:
#Input: nums = [2,1,3,4]
#Output: false
#
#Example 3:
#Input: nums = [1,2,3]
#Output: true
#
#Constraints:
#    1 <= nums.length <= 100
#    1 <= nums[i] <= 100

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Count inversions (where nums[i] > nums[i+1]).
        Valid if at most one inversion and nums[-1] <= nums[0].
        """
        n = len(nums)
        inversions = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                inversions += 1
                if inversions > 1:
                    return False

        return True


class SolutionCount:
    def check(self, nums: List[int]) -> bool:
        """
        Count breaks in sorted order.
        """
        n = len(nums)
        breaks = sum(1 for i in range(n) if nums[i] > nums[(i + 1) % n])
        return breaks <= 1


class SolutionFind:
    def check(self, nums: List[int]) -> bool:
        """
        Find rotation point and verify.
        """
        n = len(nums)

        # Find where rotation might have occurred
        rotation_point = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if rotation_point != -1:
                    return False  # More than one break
                rotation_point = i + 1

        # If no rotation or valid rotation
        if rotation_point == -1:
            return True

        # Check that after rotation point, sequence continues correctly
        return nums[-1] <= nums[0]
