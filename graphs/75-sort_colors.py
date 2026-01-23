#75. Sort Colors
#Medium
#
#Given an array nums with n objects colored red, white, or blue, sort them
#in-place so that objects of the same color are adjacent, with the colors in the
#order red, white, and blue.
#
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
#respectively.
#
#You must solve this problem without using the library's sort function.
#
#Example 1:
#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
#
#Example 2:
#Input: nums = [2,0,1]
#Output: [0,1,2]
#
#Constraints:
#    n == nums.length
#    1 <= n <= 300
#    nums[i] is either 0, 1, or 2.
#
#Follow up: Could you come up with a one-pass algorithm using only constant extra
#space?

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag algorithm - one pass, O(1) space.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


class SolutionTwoPass:
    def sortColors(self, nums: List[int]) -> None:
        """
        Two pass - count then fill.
        """
        count = [0, 0, 0]

        for num in nums:
            count[num] += 1

        idx = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[idx] = color
                idx += 1


class SolutionPartition:
    def sortColors(self, nums: List[int]) -> None:
        """
        Two-pointer partition approach.
        """
        n = len(nums)

        # First pass: move all 0s to front
        zero_idx = 0
        for i in range(n):
            if nums[i] == 0:
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                zero_idx += 1

        # Second pass: move all 1s after 0s
        one_idx = zero_idx
        for i in range(one_idx, n):
            if nums[i] == 1:
                nums[one_idx], nums[i] = nums[i], nums[one_idx]
                one_idx += 1


class SolutionThreeWay:
    def sortColors(self, nums: List[int]) -> None:
        """
        Three-way partitioning around pivot 1.
        """
        i, j, k = 0, 0, len(nums)

        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1
