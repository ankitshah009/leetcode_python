#1150. Check If a Number Is Majority Element in a Sorted Array
#Easy
#
#Given an integer array nums sorted in non-decreasing order and an integer
#target, return true if target is a majority element, or false otherwise.
#
#A majority element in an array nums is an element that appears more than
#nums.length / 2 times in the array.
#
#Example 1:
#Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
#Output: true
#Explanation: The value 5 appears 5 times and the length of the array is 9.
#Thus, 5 is a majority element because 5 > 9/2 is true.
#
#Example 2:
#Input: nums = [10,100,101,101], target = 101
#Output: false
#Explanation: The value 101 appears 2 times and the length of the array is 4.
#Thus, 101 is not a majority element because 2 > 4/2 is false.
#
#Constraints:
#    1 <= nums.length <= 1000
#    1 <= nums[i], target <= 10^9
#    nums is sorted in non-decreasing order.

from typing import List
import bisect

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """
        Binary search for first and last occurrence.
        Count = last - first + 1
        """
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        return (right - left) > len(nums) // 2


class SolutionManual:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """Manual binary search"""
        def first_occurrence(arr, t):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def last_occurrence(arr, t):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] <= t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo - 1

        first = first_occurrence(nums, target)
        if first >= len(nums) or nums[first] != target:
            return False

        last = last_occurrence(nums, target)
        return (last - first + 1) > len(nums) // 2


class SolutionCheck:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        """Check middle element trick"""
        n = len(nums)
        # If target is majority, it must be at index n//2
        if nums[n // 2] != target:
            return False

        # Count occurrences
        first = bisect.bisect_left(nums, target)
        return first + n // 2 < n and nums[first + n // 2] == target
