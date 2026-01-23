#33. Search in Rotated Sorted Array
#Medium
#
#There is an integer array nums sorted in ascending order (with distinct values).
#
#Prior to being passed to your function, nums is possibly rotated at an unknown
#pivot index k (1 <= k < nums.length) such that the resulting array is
#[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
#
#Given the array nums after the possible rotation and an integer target, return
#the index of target if it is in nums, or -1 if it is not in nums.
#
#You must write an algorithm with O(log n) runtime complexity.
#
#Example 1:
#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
#
#Example 2:
#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1
#
#Example 3:
#Input: nums = [1], target = 0
#Output: -1
#
#Constraints:
#    1 <= nums.length <= 5000
#    -10^4 <= nums[i] <= 10^4
#    All values of nums are unique.
#    nums is an ascending array that is possibly rotated.
#    -10^4 <= target <= 10^4

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified binary search - O(log n).
        Determine which half is sorted and whether target is in that half.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


class SolutionFindPivot:
    def search(self, nums: List[int], target: int) -> int:
        """
        Find pivot first, then binary search in correct half.
        """
        def find_pivot(nums: List[int]) -> int:
            left, right = 0, len(nums) - 1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

            return left

        def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        n = len(nums)
        pivot = find_pivot(nums)

        # Array is not rotated
        if pivot == 0:
            return binary_search(nums, 0, n - 1, target)

        # Target is in left sorted portion
        if target >= nums[0]:
            return binary_search(nums, 0, pivot - 1, target)
        # Target is in right sorted portion
        else:
            return binary_search(nums, pivot, n - 1, target)


class SolutionOnePass:
    def search(self, nums: List[int], target: int) -> int:
        """
        Alternative one-pass approach with clear conditions.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if target is in the sorted portion
            if nums[left] <= nums[mid]:
                # Left portion is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right portion is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
