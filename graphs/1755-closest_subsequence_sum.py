#1755. Closest Subsequence Sum
#Hard
#
#You are given an integer array nums and an integer goal.
#
#You want to choose a subsequence of nums such that the sum of its elements is
#the closest possible to goal. That is, if the sum of the subsequence's elements
#is s, then you want to minimize abs(s - goal).
#
#Return the minimum possible value of abs(s - goal).
#
#Note that a subsequence of an array is an array formed by removing some elements
#(possibly all or none) of the original array.
#
#Example 1:
#Input: nums = [5,-7,3,5], goal = 6
#Output: 0
#
#Example 2:
#Input: nums = [7,-9,15,-2], goal = -5
#Output: 1
#
#Example 3:
#Input: nums = [1,2,3], goal = -7
#Output: 7
#
#Constraints:
#    1 <= nums.length <= 40
#    -10^7 <= nums[i] <= 10^7
#    -10^9 <= goal <= 10^9

from typing import List
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        Meet in the middle approach.
        Split array in half, compute all subset sums for each half.
        For each sum in first half, binary search for complement in second half.
        """
        n = len(nums)
        half = n // 2

        def all_sums(arr):
            """Generate all possible subset sums."""
            sums = {0}
            for x in arr:
                sums = sums | {s + x for s in sums}
            return sorted(sums)

        left_sums = all_sums(nums[:half])
        right_sums = all_sums(nums[half:])

        result = float('inf')

        # For each left sum, find best right sum
        for left in left_sums:
            target = goal - left

            # Binary search for closest value in right_sums
            idx = bisect.bisect_left(right_sums, target)

            # Check idx and idx-1
            if idx < len(right_sums):
                result = min(result, abs(left + right_sums[idx] - goal))
            if idx > 0:
                result = min(result, abs(left + right_sums[idx - 1] - goal))

            if result == 0:
                return 0

        return result


class SolutionTwoPointer:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """
        Two pointer approach after generating sums.
        """
        n = len(nums)
        half = n // 2

        def get_sums(arr):
            sums = {0}
            for x in arr:
                sums = sums | {s + x for s in sums}
            return sorted(sums)

        left = get_sums(nums[:half])
        right = get_sums(nums[half:])

        result = float('inf')
        i, j = 0, len(right) - 1

        while i < len(left) and j >= 0:
            total = left[i] + right[j]
            result = min(result, abs(total - goal))

            if total < goal:
                i += 1
            elif total > goal:
                j -= 1
            else:
                return 0

        return result
