#154. Find Minimum in Rotated Sorted Array II
#Hard
#
#Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
#
#Given the sorted rotated array nums that may contain duplicates, return the minimum element
#of this array.
#
#You must decrease the overall operation steps as much as possible.
#
#Example 1:
#Input: nums = [1,3,5]
#Output: 1
#
#Example 2:
#Input: nums = [2,2,2,0,1]
#Output: 0
#
#Constraints:
#    n == nums.length
#    1 <= n <= 5000
#    -5000 <= nums[i] <= 5000
#    nums is sorted and rotated between 1 and n times.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
