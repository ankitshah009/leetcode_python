#81. Search in Rotated Sorted Array II
#Medium
#
#There is an integer array nums sorted in non-decreasing order (not necessarily
#with distinct values).
#
#Before being passed to your function, nums is rotated at an unknown pivot index k.
#
#Given the array nums after the rotation and an integer target, return true if
#target is in nums, or false if it is not in nums.
#
#You must decrease the overall operation steps as much as possible.
#
#Example 1:
#Input: nums = [2,5,6,0,0,1,2], target = 0
#Output: true
#
#Example 2:
#Input: nums = [2,5,6,0,0,1,2], target = 3
#Output: false
#
#Constraints:
#    1 <= nums.length <= 5000
#    -10^4 <= nums[i] <= 10^4
#    nums is guaranteed to be rotated at some pivot.
#    -10^4 <= target <= 10^4
#
#Follow up: This problem is similar to Search in Rotated Sorted Array, but nums
#may contain duplicates. Would this affect the runtime complexity? How and why?

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Modified binary search handling duplicates.
        Worst case O(n) when all elements are same.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates - can't determine which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
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

        return False


class SolutionLinear:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Linear search - guaranteed O(n).
        """
        return target in nums


class SolutionRecursive:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Recursive binary search.
        """
        def binary_search(left: int, right: int) -> bool:
            if left > right:
                return False

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                return binary_search(left + 1, right - 1)

            # Left half sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binary_search(left, mid - 1)
                return binary_search(mid + 1, right)

            # Right half sorted
            if nums[mid] < target <= nums[right]:
                return binary_search(mid + 1, right)
            return binary_search(left, mid - 1)

        return binary_search(0, len(nums) - 1)
