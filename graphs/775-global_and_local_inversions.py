#775. Global and Local Inversions
#Medium
#
#You are given an integer array nums of length n which represents a permutation
#of all the integers in the range [0, n - 1].
#
#The number of global inversions is the number of the different pairs (i, j)
#where:
#- 0 <= i < j < n
#- nums[i] > nums[j]
#
#The number of local inversions is the number of indices i where:
#- 0 <= i < n - 1
#- nums[i] > nums[i + 1]
#
#Return true if the number of global inversions is equal to the number of local
#inversions.
#
#Example 1:
#Input: nums = [1,0,2]
#Output: true
#Explanation: There is 1 global inversion and 1 local inversion.
#
#Example 2:
#Input: nums = [1,2,0]
#Output: false
#Explanation: There are 2 global inversions and 1 local inversion.
#
#Constraints:
#    n == nums.length
#    1 <= n <= 10^5
#    0 <= nums[i] < n
#    All the integers of nums are unique.
#    nums is a permutation of all the numbers in the range [0, n - 1].

class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        """
        Every local inversion is a global inversion.
        So we need: all global inversions are local (adjacent).
        This means: nums[i] != i implies abs(nums[i] - i) <= 1.
        """
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True


class SolutionMaxPrefix:
    """Track max of prefix, check for non-local global inversions"""

    def isIdealPermutation(self, nums: list[int]) -> bool:
        # If there's a global but non-local inversion:
        # nums[i] > nums[j] where j > i + 1
        # Equivalent to: max(nums[0..i]) > nums[i+2] for some i

        prefix_max = float('-inf')

        for i in range(len(nums) - 2):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max > nums[i + 2]:
                return False

        return True


class SolutionMergeSort:
    """Count inversions using merge sort"""

    def isIdealPermutation(self, nums: list[int]) -> bool:
        def count_global(arr):
            if len(arr) <= 1:
                return 0, arr

            mid = len(arr) // 2
            left_inv, left = count_global(arr[:mid])
            right_inv, right = count_global(arr[mid:])

            merged = []
            inv = left_inv + right_inv
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return inv, merged

        global_inv, _ = count_global(nums)
        local_inv = sum(1 for i in range(len(nums) - 1) if nums[i] > nums[i + 1])

        return global_inv == local_inv
