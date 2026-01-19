#525. Contiguous Array
#Medium
#
#Given a binary array nums, return the maximum length of a contiguous subarray with an equal
#number of 0 and 1.
#
#Example 1:
#Input: nums = [0,1]
#Output: 2
#Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#
#Example 2:
#Input: nums = [0,1,0]
#Output: 2
#Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    nums[i] is either 0 or 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Convert to prefix sum: 0 -> -1, 1 -> 1
        # Equal 0s and 1s means prefix sum = 0 in that range
        count_to_idx = {0: -1}
        count = 0
        max_length = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in count_to_idx:
                max_length = max(max_length, i - count_to_idx[count])
            else:
                count_to_idx[count] = i

        return max_length
