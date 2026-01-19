#163. Missing Ranges
#Easy
#
#You are given an inclusive range [lower, upper] and a sorted unique integer
#array nums, where all elements are in the inclusive range.
#
#A number x is considered missing if x is in the range [lower, upper] and x
#is not in nums.
#
#Return the smallest sorted list of ranges that cover every missing number
#exactly. That is, no element of nums is in any of the ranges, and each missing
#number is in one of the ranges.
#
#Example 1:
#Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
#Output: [[2, 2], [4, 49], [51, 74], [76, 99]]
#
#Example 2:
#Input: nums = [-1], lower = -1, upper = -1
#Output: []
#
#Example 3:
#Input: nums = [], lower = 1, upper = 1
#Output: [[1, 1]]

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        prev = lower - 1

        # Add upper + 1 as sentinel to handle the last range
        nums_with_sentinel = nums + [upper + 1]

        for num in nums_with_sentinel:
            if num - prev >= 2:
                result.append([prev + 1, num - 1])
            prev = num

        return result


class SolutionAlternative:
    """Without sentinel, explicit handling of boundaries"""

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []

        if not nums:
            return [[lower, upper]]

        # Check for missing range before first element
        if nums[0] > lower:
            result.append([lower, nums[0] - 1])

        # Check for missing ranges between elements
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                result.append([nums[i-1] + 1, nums[i] - 1])

        # Check for missing range after last element
        if nums[-1] < upper:
            result.append([nums[-1] + 1, upper])

        return result


class SolutionOldFormat:
    """Returns string format (older LeetCode format)"""

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def format_range(lo, hi):
            if lo == hi:
                return str(lo)
            return f"{lo}->{hi}"

        result = []
        prev = lower - 1

        for num in nums + [upper + 1]:
            if num - prev >= 2:
                result.append(format_range(prev + 1, num - 1))
            prev = num

        return result
