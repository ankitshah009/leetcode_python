#26. Remove Duplicates from Sorted Array
#Easy
#
#Given an integer array nums sorted in non-decreasing order, remove the duplicates
#in-place such that each unique element appears only once. The relative order of
#the elements should be kept the same. Then return the number of unique elements
#in nums.
#
#Consider the number of unique elements of nums to be k, to get accepted, you need
#to do the following things:
#
#- Change the array nums such that the first k elements of nums contain the unique
#  elements in the order they were present in nums initially.
#- Return k.
#
#Example 1:
#Input: nums = [1,1,2]
#Output: 2, nums = [1,2,_]
#
#Example 2:
#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#
#Constraints:
#    1 <= nums.length <= 3 * 10^4
#    -100 <= nums[i] <= 100
#    nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two pointers - one for reading, one for writing.
        """
        if not nums:
            return 0

        write_idx = 1

        for read_idx in range(1, len(nums)):
            if nums[read_idx] != nums[read_idx - 1]:
                nums[write_idx] = nums[read_idx]
                write_idx += 1

        return write_idx


class SolutionAlternative:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Alternative two pointer approach.
        """
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


class SolutionSet:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Using set to track seen values.
        Note: This modifies the array but not strictly in-place as per problem.
        """
        seen = set()
        write_idx = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[write_idx] = num
                write_idx += 1

        return write_idx
