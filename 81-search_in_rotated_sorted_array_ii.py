#81. Search in Rotated Sorted Array II
#Medium
#
#There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
#
#Before being passed to your function, nums is rotated at an unknown pivot index k.
#
#Given the array nums after the rotation and an integer target, return true if target is in
#nums, or false if it is not in nums.
#
#You must decrease the overall operation steps as much as possible.
#
#Example 1:
#Input: nums = [2,5,6,0,0,1,2], target = 0
#Output: true
#
#Example 2:
#Input: nums = [2,5,6,0,0,1,2], target = 3
#Output: false
#
#Constraints:
#    1 <= nums.length <= 5000
#    -10^4 <= nums[i] <= 10^4
#    nums is guaranteed to be rotated at some pivot.
#    -10^4 <= target <= 10^4

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
