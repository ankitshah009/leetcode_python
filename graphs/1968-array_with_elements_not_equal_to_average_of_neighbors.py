#1968. Array With Elements Not Equal to Average of Neighbors
#Medium
#
#You are given a 0-indexed array nums of distinct integers. You want to
#rearrange the elements in the array such that every element in the rearranged
#array is not equal to the average of its neighbors.
#
#More formally, the rearranged array should have the property such that for
#every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is
#not equal to nums[i].
#
#Return any rearrangement of nums that meets the requirements.
#
#Example 1:
#Input: nums = [1,2,3,4,5]
#Output: [1,2,4,5,3]
#
#Example 2:
#Input: nums = [6,2,0,9,7]
#Output: [9,7,6,2,0]
#
#Constraints:
#    3 <= nums.length <= 10^5
#    0 <= nums[i] <= 10^5

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Wiggle sort: place elements in zigzag pattern.
        Sort and interleave small and large elements.
        """
        nums.sort()
        n = len(nums)
        result = [0] * n

        # Place smaller half at even indices, larger half at odd indices
        left, right = 0, (n + 1) // 2
        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[left]
                left += 1
            else:
                result[i] = nums[right]
                right += 1

        return result


class SolutionSwap:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Simple swap approach to create zigzag.
        """
        nums.sort()
        n = len(nums)

        # Swap adjacent pairs at odd indices
        for i in range(1, n - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


class SolutionGreedy:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Greedy fix violations.
        """
        nums.sort()

        # Create alternating peaks and valleys
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums


class SolutionMedian:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Place elements alternating from two halves.
        """
        nums.sort()
        result = []
        n = len(nums)

        # Interleave from front and back of sorted array
        left, right = 0, n - 1

        while left <= right:
            result.append(nums[left])
            left += 1
            if left <= right:
                result.append(nums[right])
                right -= 1

        return result
