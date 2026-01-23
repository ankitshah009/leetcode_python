#896. Monotonic Array
#Easy
#
#An array is monotonic if it is either monotone increasing or monotone decreasing.
#
#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
#An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
#Given an integer array nums, return true if the given array is monotonic, or
#false otherwise.
#
#Example 1:
#Input: nums = [1,2,2,3]
#Output: true
#
#Example 2:
#Input: nums = [6,5,4,4]
#Output: true
#
#Example 3:
#Input: nums = [1,3,2]
#Output: false
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -10^5 <= nums[i] <= 10^5

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """
        Check if all increasing or all decreasing.
        """
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False

        return increasing or decreasing


class SolutionCompare:
    """Using comparison operators"""

    def isMonotonic(self, nums: list[int]) -> bool:
        return all(a <= b for a, b in zip(nums, nums[1:])) or \
               all(a >= b for a, b in zip(nums, nums[1:]))


class SolutionSorted:
    """Check against sorted versions"""

    def isMonotonic(self, nums: list[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)


class SolutionEarly:
    """Early termination"""

    def isMonotonic(self, nums: list[int]) -> bool:
        direction = 0  # 0: unknown, 1: increasing, -1: decreasing

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if direction == -1:
                    return False
                direction = 1
            elif nums[i] < nums[i - 1]:
                if direction == 1:
                    return False
                direction = -1

        return True
