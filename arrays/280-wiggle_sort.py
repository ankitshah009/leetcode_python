#280. Wiggle Sort
#Medium
#
#Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2]
#<= nums[3]....
#
#You may assume the input array always has a valid answer.
#
#Example 1:
#Input: nums = [3,5,2,1,6,4]
#Output: [3,5,1,6,2,4]
#Explanation: [1,6,2,5,3,4] is also accepted.
#
#Example 2:
#Input: nums = [6,6,5,6,3,8]
#Output: [6,6,5,6,3,8]
#
#Constraints:
#    1 <= nums.length <= 5 * 10^4
#    0 <= nums[i] <= 10^4
#    It is guaranteed that there will be an answer for the given input nums.
#
#Follow up: Could you solve the problem in O(n) time without sorting the array?

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One pass approach: O(n) time, O(1) space
        # For odd indices: nums[i] should be >= neighbors
        # For even indices: nums[i] should be <= neighbors

        for i in range(1, len(nums)):
            if i % 2 == 1:
                # Odd index: should be >= previous
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                # Even index: should be <= previous
                if nums[i] > nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

    # Sorting approach: O(n log n)
    def wiggleSortWithSorting(self, nums: List[int]) -> None:
        nums.sort()
        # Swap adjacent pairs starting from index 1
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
