#31. Next Permutation
#Medium
#
#A permutation of an array of integers is an arrangement of its members into a
#sequence or linear order.
#
#The next permutation of an array of integers is the next lexicographically
#greater permutation of its integer.
#
#If such arrangement is not possible, the array must be rearranged as the lowest
#possible order (i.e., sorted in ascending order).
#
#The replacement must be in place and use only constant extra memory.
#
#Example 1:
#Input: nums = [1,2,3]
#Output: [1,3,2]
#
#Example 2:
#Input: nums = [3,2,1]
#Output: [1,2,3]
#
#Example 3:
#Input: nums = [1,1,5]
#Output: [1,5,1]
#
#Constraints:
#    1 <= nums.length <= 100
#    0 <= nums[i] <= 100

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        1. Find largest i where nums[i] < nums[i+1] (first decreasing from right)
        2. Find largest j > i where nums[i] < nums[j]
        3. Swap nums[i] and nums[j]
        4. Reverse suffix after position i
        """
        n = len(nums)

        # Step 1: Find first decreasing element from right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find element just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class SolutionAlternative:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Alternative implementation with helper functions.
        """
        def reverse(arr: List[int], start: int, end: int):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)

        # Find pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            # Entire array is descending
            reverse(nums, 0, n - 1)
            return

        # Find successor
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break

        # Reverse suffix
        reverse(nums, pivot + 1, n - 1)


class SolutionBinarySearch:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Using binary search to find the successor.
        """
        import bisect

        n = len(nums)

        # Find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Binary search for successor in reversed suffix
            # Suffix is in descending order, so we search in reversed manner
            suffix = nums[i + 1:][::-1]
            j = bisect.bisect_right(suffix, nums[i])
            # Convert back to original index
            swap_idx = n - 1 - j
            nums[i], nums[swap_idx] = nums[swap_idx], nums[i]

        # Reverse suffix
        nums[i + 1:] = nums[i + 1:][::-1]
