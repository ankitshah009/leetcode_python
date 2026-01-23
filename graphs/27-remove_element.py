#27. Remove Element
#Easy
#
#Given an integer array nums and an integer val, remove all occurrences of val in
#nums in-place. The order of the elements may be changed. Then return the number
#of elements in nums which are not equal to val.
#
#Consider the number of elements in nums which are not equal to val be k, to get
#accepted, you need to do the following things:
#
#- Change the array nums such that the first k elements of nums contain the
#  elements which are not equal to val.
#- Return k.
#
#Example 1:
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]
#
#Example 2:
#Input: nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3,_,_,_]
#
#Constraints:
#    0 <= nums.length <= 100
#    0 <= nums[i] <= 50
#    0 <= val <= 100

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two pointers - write index and read index.
        """
        write_idx = 0

        for num in nums:
            if num != val:
                nums[write_idx] = num
                write_idx += 1

        return write_idx


class SolutionSwap:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Swap with end - useful when elements to remove are rare.
        """
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return right


class SolutionAlternative:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Alternative two pointer approach from both ends.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return left
