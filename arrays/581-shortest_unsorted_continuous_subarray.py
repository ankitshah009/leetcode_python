#581. Shortest Unsorted Continuous Subarray
#Medium
#
#Given an integer array nums, you need to find one continuous subarray such that if you only
#sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
#
#Return the shortest such subarray and output its length.
#
#Example 1:
#Input: nums = [2,6,4,8,10,9,15]
#Output: 5
#Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array
#sorted in ascending order.
#
#Example 2:
#Input: nums = [1,2,3,4]
#Output: 0
#
#Example 3:
#Input: nums = [1]
#Output: 0
#
#Constraints:
#    1 <= nums.length <= 10^4
#    -10^5 <= nums[i] <= 10^5

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Find left boundary (first element out of order from left)
        left = 0
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            return 0  # Already sorted

        # Find right boundary (first element out of order from right)
        right = n - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Find min and max in the unsorted subarray
        subarray_min = min(nums[left:right + 1])
        subarray_max = max(nums[left:right + 1])

        # Extend left boundary
        while left > 0 and nums[left - 1] > subarray_min:
            left -= 1

        # Extend right boundary
        while right < n - 1 and nums[right + 1] < subarray_max:
            right += 1

        return right - left + 1
