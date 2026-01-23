#540. Single Element in a Sorted Array
#Medium
#
#You are given a sorted array consisting of only integers where every element
#appears exactly twice, except for one element which appears exactly once.
#
#Return the single element that appears only once.
#
#Your solution must run in O(log n) time and O(1) space.
#
#Example 1:
#Input: nums = [1,1,2,3,3,4,4,8,8]
#Output: 2
#
#Example 2:
#Input: nums = [3,3,7,7,10,11,11]
#Output: 10
#
#Constraints:
#    1 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Binary search on even indices.
        Before single element: nums[even] == nums[even + 1]
        After single element: nums[even] == nums[even - 1]
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Single element is on the right
                left = mid + 2
            else:
                # Single element is on the left (including mid)
                right = mid

        return nums[left]


class SolutionXOR:
    """XOR approach - O(n) but simple"""

    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


class SolutionBinarySearchAlt:
    """Alternative binary search"""

    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Check if mid is on the "correct" half
            # XOR with 1 swaps even<->odd
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
