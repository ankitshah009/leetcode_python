#1909. Remove One Element to Make the Array Strictly Increasing
#Easy
#
#Given a 0-indexed integer array nums, return true if it can be made strictly
#increasing after removing exactly one element, or false otherwise. If the
#array is already strictly increasing, return true.
#
#The array nums is strictly increasing if nums[i - 1] < nums[i] for each index
#(1 <= i < nums.length).
#
#Example 1:
#Input: nums = [1,2,10,5,7]
#Output: true
#
#Example 2:
#Input: nums = [2,3,1,2]
#Output: false
#
#Example 3:
#Input: nums = [1,1,1]
#Output: false
#
#Constraints:
#    2 <= nums.length <= 1000
#    1 <= nums[i] <= 1000

from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        """
        Find violation, try removing either element.
        """
        def is_strictly_increasing(arr: List[int]) -> bool:
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # Try removing nums[i] or nums[i-1]
                without_i = nums[:i] + nums[i + 1:]
                without_prev = nums[:i - 1] + nums[i:]
                return is_strictly_increasing(without_i) or is_strictly_increasing(without_prev)

        return True


class SolutionCount:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        """
        Count violations and check if removable.
        """
        violations = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                violations += 1
                if violations > 1:
                    return False

                # Check if removing i or i-1 fixes it
                # Remove i: nums[i-1] < nums[i+1]
                # Remove i-1: nums[i-2] < nums[i]
                can_remove_i = (i + 1 >= len(nums) or nums[i - 1] < nums[i + 1])
                can_remove_prev = (i - 2 < 0 or nums[i - 2] < nums[i])

                if not can_remove_i and not can_remove_prev:
                    return False

        return True


class SolutionOnePass:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        """
        One-pass solution tracking removal.
        """
        removed = False

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if removed:
                    return False
                removed = True

                # Try to "remove" nums[i-1] by skipping it
                # This means nums[i] should be > nums[i-2]
                if i >= 2 and nums[i] <= nums[i - 2]:
                    # Can't remove i-1, must remove i
                    # Simulate by setting nums[i] = nums[i-1]
                    nums[i] = nums[i - 1]

        return True
