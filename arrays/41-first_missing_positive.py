#41. First Missing Positive
#Hard
#
#Given an unsorted integer array nums, return the smallest missing positive integer.
#
#You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
#Example 1:
#Input: nums = [1,2,0]
#Output: 3
#Explanation: The numbers in the range [1,2] are all in the array.
#
#Example 2:
#Input: nums = [3,4,-1,1]
#Output: 2
#Explanation: 1 is in the array but 2 is missing.
#
#Example 3:
#Input: nums = [7,8,9,11,12]
#Output: 1
#Explanation: The smallest positive integer 1 is missing.
#
#Constraints:
#    1 <= nums.length <= 10^5
#    -2^31 <= nums[i] <= 2^31 - 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each number in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Find first position where number doesn't match
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
