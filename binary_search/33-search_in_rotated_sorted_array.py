#33. Search in Rotated Sorted Array
#Medium
#
#There is an integer array nums sorted in ascending order (with distinct values).
#
#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k.
#
#Given the array nums after the possible rotation and an integer target, return the index
#of target if it is in nums, or -1 if it is not in nums.
#
#You must write an algorithm with O(log n) runtime complexity.
#
#Example 1:
#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
#
#Example 2:
#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1
#
#Example 3:
#Input: nums = [1], target = 0
#Output: -1
#
#Constraints:
#    1 <= nums.length <= 5000
#    -10^4 <= nums[i] <= 10^4
#    All values of nums are unique.
#    nums is an ascending array that is possibly rotated.
#    -10^4 <= target <= 10^4

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
