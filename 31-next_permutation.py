#31. Next Permutation
#Medium
#
#A permutation of an array of integers is an arrangement of its members into a sequence
#or linear order.
#
#The next permutation of an array of integers is the next lexicographically greater permutation
#of its integer.
#
#Given an array of integers nums, find the next permutation of nums.
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

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # Find first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find smallest element greater than nums[i] from right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
