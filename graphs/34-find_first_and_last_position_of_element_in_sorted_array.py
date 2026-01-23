#34. Find First and Last Position of Element in Sorted Array
#Medium
#
#Given an array of integers nums sorted in non-decreasing order, find the starting
#and ending position of a given target value.
#
#If target is not found in the array, return [-1, -1].
#
#You must write an algorithm with O(log n) runtime complexity.
#
#Example 1:
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#
#Example 2:
#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]
#
#Example 3:
#Input: nums = [], target = 0
#Output: [-1,-1]
#
#Constraints:
#    0 <= nums.length <= 10^5
#    -10^9 <= nums[i] <= 10^9
#    nums is a non-decreasing array.
#    -10^9 <= target <= 10^9

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Two binary searches - one for left bound, one for right bound.
        """
        def find_left(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    right = mid - 1  # Continue searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        def find_right(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    left = mid + 1  # Continue searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        return [find_left(nums, target), find_right(nums, target)]


class SolutionBisect:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Using bisect module.
        """
        import bisect

        left = bisect.bisect_left(nums, target)

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect.bisect_right(nums, target) - 1

        return [left, right]


class SolutionUnified:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Unified binary search with direction parameter.
        """
        def binary_search(nums: List[int], target: int, find_first: bool) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    result = mid
                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1

            return result

        first = binary_search(nums, target, True)

        if first == -1:
            return [-1, -1]

        last = binary_search(nums, target, False)

        return [first, last]


class SolutionLinear:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Linear search - O(n) for comparison.
        """
        first = last = -1

        for i, num in enumerate(nums):
            if num == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]
