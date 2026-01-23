#80. Remove Duplicates from Sorted Array II
#Medium
#
#Given an integer array nums sorted in non-decreasing order, remove some duplicates
#in-place such that each unique element appears at most twice. The relative order
#of the elements should be kept the same.
#
#Return k after placing the final result in the first k slots of nums.
#
#Example 1:
#Input: nums = [1,1,1,2,2,3]
#Output: 5, nums = [1,1,2,2,3,_]
#
#Example 2:
#Input: nums = [0,0,1,1,1,1,2,3,3]
#Output: 7, nums = [0,0,1,1,2,3,3,_,_]
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    -10^4 <= nums[i] <= 10^4
#    nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two pointers - generalized for k allowed duplicates.
        """
        k = 2  # Allow at most k duplicates

        if len(nums) <= k:
            return len(nums)

        write = k

        for read in range(k, len(nums)):
            if nums[read] != nums[write - k]:
                nums[write] = nums[read]
                write += 1

        return write


class SolutionExplicit:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Explicit counting approach.
        """
        if len(nums) <= 2:
            return len(nums)

        write = 1
        count = 1

        for read in range(1, len(nums)):
            if nums[read] == nums[read - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[write] = nums[read]
                write += 1

        return write


class SolutionGeneral:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Generalized solution for any k.
        """
        def remove_duplicates_k(nums: List[int], k: int) -> int:
            if len(nums) <= k:
                return len(nums)

            write = k
            for read in range(k, len(nums)):
                if nums[read] != nums[write - k]:
                    nums[write] = nums[read]
                    write += 1
            return write

        return remove_duplicates_k(nums, 2)
