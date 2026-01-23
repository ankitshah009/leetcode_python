#35. Search Insert Position
#Easy
#
#Given a sorted array of distinct integers and a target value, return the index
#if the target is found. If not, return the index where it would be if it were
#inserted in order.
#
#You must write an algorithm with O(log n) runtime complexity.
#
#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2
#
#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1
#
#Example 3:
#Input: nums = [1,3,5,6], target = 7
#Output: 4
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^4 <= nums[i] <= 10^4
#    nums contains distinct values sorted in ascending order.
#    -10^4 <= target <= 10^4

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary search - returns leftmost insertion point.
        """
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


class SolutionAlternative:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Alternative binary search implementation.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


class SolutionBisect:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Using bisect module.
        """
        import bisect
        return bisect.bisect_left(nums, target)


class SolutionLinear:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Linear search - O(n) for comparison.
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
