#2444. Count Subarrays With Fixed Bounds
#Hard
#
#You are given an integer array nums and two integers minK and maxK.
#
#A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#    The minimum value in the subarray is equal to minK.
#    The maximum value in the subarray is equal to maxK.
#
#Return the number of fixed-bound subarrays.
#
#A subarray is a contiguous part of an array.
#
#Example 1:
#Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
#Output: 2
#Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
#
#Example 2:
#Input: nums = [1,1,1,1], minK = 1, maxK = 1
#Output: 10
#Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
#
#Constraints:
#    2 <= nums.length <= 10^5
#    1 <= nums[i], minK, maxK <= 10^6

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        min_pos = -1  # Last position of minK
        max_pos = -1  # Last position of maxK
        bad_pos = -1  # Last position of invalid element

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_pos = i

            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i

            # Number of valid subarrays ending at i
            # Must include both minK and maxK, and no invalid elements
            result += max(0, min(min_pos, max_pos) - bad_pos)

        return result
